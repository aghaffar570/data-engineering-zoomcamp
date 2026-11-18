import sys
import pandas as pd

print('sys arg:', sys.argv)

print("sys.executable:",sys.executable)
print("sys.version:",sys.version)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())
