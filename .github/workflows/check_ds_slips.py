from pathlib import Path
import os
import tempfile
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[2]
temp = tempfile.TemporaryDirectory()
os.chdir(temp.name)

n = list(range(30))
pd.DataFrame({"likes": [50 + i * 10 for i in n], "views": [1000 + i * 250 for i in n]}).to_csv("USvideos.csv", index=False)
pd.DataFrame({"YearsExperience": [0.5 + i * 0.4 for i in n], "Salary": [18000 + i * 3000 for i in n]}).to_csv("Salary_Data.csv", index=False)
pd.DataFrame({"Time on App": [2.0 + (i % 10) * 0.3 for i in n], "Length of Membership": [1.0 + (i % 8) * 0.4 for i in n]}).to_csv("Ecommerce Customers.csv", index=False)
pd.DataFrame({"Training_Hours_Per_Week": [5 + i % 12 for i in n], "Performance_Score": [40 + i % 60]}).to_csv("collegiate_athlete_injury_dataset.csv", index=False)
marks = [25, 35, 45, 55, 65, 70, 80, 90, 98] * 4
pd.DataFrame({"Student_ID": list(range(1, 37)), "Student_Name": [f"S{i}" for i in range(36)], "Study_Hours": [1 + i % 8 for i in range(36)], "Attendance": [50 + (i * 7) % 50 for i in range(36)], "Marks": marks}).to_csv("student_dataset_v2.csv", index=False)
pd.DataFrame({"id": list(range(40)), "battery_power": [800 + (i * 17) % 1000 for i in range(40)], "ram": [1000 + (i * 151) % 6000 for i in range(40)], "int_memory": [8 + i % 64 for i in range(40)], "price_range": [i % 4 for i in range(40)]}).to_csv("train.csv", index=False)
pd.DataFrame({"longitude": [-120 + i for i in n], "latitude": [30 + i % 10 for i in n], "housing_median_age": [10 + i % 30 for i in n], "total_rooms": [1000 + 20 * i for i in n], "total_bedrooms": [200 + 5 * i for i in n], "population": [800 + 30 * i for i in n], "households": [100 + 4 * i for i in n], "median_income": [2 + i * 0.1 for i in n], "ocean_proximity": ["NEAR BAY" if i % 2 else "INLAND" for i in n], "median_house_value": [50000 + 3000 * i for i in n]}).to_csv("housing.csv", index=False)
pd.DataFrame([[i % 20, i % 7, i % 9, i % 2] for i in range(80)]).to_csv("spambase.csv", index=False, header=False)
pd.DataFrame({"Alcohol": [8 + i % 9 for i in range(60)], "Malic_Acid": [1 + (i % 10) * 0.2 for i in range(60)], "Ash": [1 + (i % 4) * 0.3 for i in range(60)], "Wine_Class": [i % 3 for i in range(60)]}).to_csv("Wine.csv", index=False)
pd.DataFrame({"Pclass": [1 + i % 3 for i in range(40)], "Survived": [i % 2 for i in range(40)]}).to_csv("titanic.csv", index=False)
pd.DataFrame({"Sales": [100 + i * 5 for i in range(30)]}).to_csv("sales.csv", index=False)
pd.DataFrame({"Training_Hours_Per_Week": [5 + i % 12 for i in range(40)], "Performance_Score": [40 + (i * 3) % 60]}).to_csv("collegiate_athlete_injury_dataset.csv", index=False)
pd.DataFrame({"Student_ID": list(range(1, 61)), "Study_Hours": [1 + i % 8 for i in range(60)], "Attendance": [50 + i % 50 for i in range(60)], "Marks": [20 + (i * 13) % 80 for i in range(60)], "Grade": [["A", "B", "C"][i % 3] for i in range(60)]}).to_csv("Students_Grading_Dataset.csv", index=False)
pd.DataFrame({"Year": [2005 + i % 20 for i in range(50)], "Present_Price": [2 + i * 0.4 for i in range(50)], "Kms_Driven": [1000 + 500 * i for i in range(50)], "Selling_Price": [1 + i * 0.3 for i in range(50)]}).to_csv("car data.csv", index=False)
pd.DataFrame({"Temperature": [20 + i % 15 for i in range(30)], "Humidity": [40 + (i * 3) % 50 for i in range(30)], "Rainfall": [i % 20 for i in range(30)], "Wind Speed": [2 + i % 10 for i in range(30)]}).to_csv("weather.csv", index=False)
pd.DataFrame({"rainfall_mm": [500 + i * 20 for i in range(40)], "crop_yield": [2 + i * 0.1 for i in range(40)]}).to_csv("crop_yield_data.csv", index=False)

passed = []
for number in range(1, 26):
    path = root / "ds" / f"slip{number}"
    source = path.read_text(encoding="utf-8")
    source_lines = [line for line in source.splitlines() if line.strip() not in {f"slip{number}", "Q1:", "Q2:"}]
    source = "\n".join(source_lines)
    compile(source, str(path), "exec")
    namespace = {"__name__": "__main__"}
    exec(source, namespace)
    plt.close("all")
    passed.append(path.name)
    print(f"PASS {path.name}")

print(f"PASSED: {len(passed)}/25 slip programs executed.")
temp.cleanup()
