# employee_analysis.py
# Author: 24f2004315@ds.study.iitm.ac.in
# Python script to load dataset, count R&D employees, and create a histogram

import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# ------------------------------
# 1. Load the employee dataset
# ------------------------------

# Example CSV path — replace with the correct CSV file location
# Ensure your CSV has columns: EmployeeID, Name, Department, Region, etc.
df = pd.read_csv("employees.csv")

# ------------------------------
# 2. Calculate frequency count for "R&D" department
# ------------------------------

rd_count = (df["Department"] == "R&D").sum()

print("Number of employees in R&D:", rd_count)

# ------------------------------
# 3. Create histogram of department distribution
# ------------------------------

plt.figure(figsize=(8, 5))
df["Department"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Department Distribution Histogram")
plt.xlabel("Department")
plt.ylabel("Count")

# Save plot to buffer
buf = BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)

# Convert to base64 for embedding inside HTML
encoded = base64.b64encode(buf.read()).decode("utf-8")

# ------------------------------
# 4. Save everything in an HTML file
# ------------------------------

html_content = f"""
<html>
<head>
<title>Employee Analysis</title>
</head>
<body>
<h1>Employee Department Analysis</h1>
<p><b>Author:</b> 24f2004315@ds.study.iitm.ac.in</p>

<h2>Frequency Count for R&D Department</h2>
<p>Number of employees in R&D: <b>{rd_count}</b></p>

<h2>Department Distribution Histogram</h2>
<img src="data:image/png;base64,{encoded}" alt="Histogram">

</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file 'employee_analysis.html' successfully created!")
