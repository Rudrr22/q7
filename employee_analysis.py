# employee_analysis.py
# Author: 24f2004315@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import inspect

# ----------------------
# Load dataset
# ----------------------
df = pd.read_csv("employees.csv")

# Count R&D employees
rd_count = (df["Department"] == "R&D").sum()
print("Employees in R&D:", rd_count)

# ----------------------
# Create histogram
# ----------------------
plt.figure(figsize=(8, 5))
df["Department"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")

# Convert plot to Base64 image
buf = BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
img64 = base64.b64encode(buf.read()).decode("utf-8")

# ----------------------
# Get Python source code
# ----------------------
python_code = inspect.getsource(inspect.getmodule(inspect.currentframe()))

# ----------------------
# Generate HTML
# ----------------------
html = f"""
<html>
<body>
<h1>Employee Visualization</h1>
<p><b>Author:</b> 24f2004315@ds.study.iitm.ac.in</p>

<h2>R&D Department Count</h2>
<p><b>{rd_count}</b> employees work in R&D.</p>

<h2>Department Histogram</h2>
<img src="data:image/png;base64,{img64}">

<h2>Python Code Used</h2>
<pre><code>
{python_code}
</code></pre>

</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html)

print("employee_analysis.html successfully created with embedded Python code!")
