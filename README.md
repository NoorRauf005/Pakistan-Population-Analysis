# 📊 Pakistan Population Analysis (1960–2022) 🇵🇰

A **Python-based analytical system** designed to process, manage, analyze, and visualize over **60 years of Pakistan’s demographic data**.  
This project showcases strong foundations in **Software Engineering, Data Engineering, CRUD architecture, file handling, CLI visualization, and algorithmic logic**.

---

## 🎯 Project Objectives

- Implement complete **Data Life Cycle Management**
- Apply **Software Engineering principles** on real demographic data
- Build a **CRUD-based population management system**
- Create a **data transformation pipeline**
- Deliver **CLI visualization and analytics**
- Practice efficient Python **file handling and data structures**

---

## ⚠️ Disclaimer

This system was developed as part of a **Programming Fundamentals (PF) academic assignment** to demonstrate:

- Data Transformation  
- CRUD Operations  
- File Handling & Persistence  
- CLI-based Visualization  
- Data Analysis

---

## 🔗 Project Links

**GitHub Profile:**  
https://github.com/NoorRauf005

**Project Repository:**  
https://github.com/NoorRauf005/Pakistan-Population-Analysis

**Dataset Source**  
World Bank Open Data (Pakistan Demographics)  
https://data.worldbank.org/

---

## 📁 Repository Structure


Pakistan-Population-Analysis/
├── pakistan_population.csv
├── population_data.txt
├── converter.py
├── main.py
├── visualization.py
├── README.md


---

## ✨ Key Features

### ⚙️ Data Engineering Pipeline

#### 📌 Automated Data Conversion
- Converts the original `.csv` file into an optimized `.txt` format
- Enhances file I/O performance

#### 📌 Feature Engineering Calculations

```python
Male Population = Total Population - Female Population

Supports fields:

Total Population

Male Population

Female Population

Urban Population

Rural Population

Year

🛠️ CRUD Management System

The system supports full CRUD operations:

✔ Create

Add new yearly population records

✔ Read

View and filter data by year

✔ Update

Modify existing records with synchronization to the file

✔ Delete

Remove incorrect or outdated entries

✔ Search Performance
Time Complexity: O(n)
📈 Advanced Analytics
📊 Population Growth Rate Formula
Growth Rate (%) = ((New Population - Old Population) / Old Population) * 100

Features:

Calculates annual growth percentages

Handles missing data

Zero-division error protection

📊 CLI Visualization

Custom ASCII histogram output:

1960 | ██████████████
1970 | ██████████████████
1980 | ███████████████████████
1990 | ██████████████████████████
2000 | ███████████████████████████████
2010 | ████████████████████████████████████
2020 | █████████████████████████████████████████

Scaling:

1 Block (█) = 10 Million People
🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/NoorRauf005/Pakistan-Population-Analysis.git
cd Pakistan-Population-Analysis
2️⃣ Convert Dataset
python converter.py

This generates:

population_data.txt
3️⃣ Launch Main System
python main.py
🧠 Technical Details
🛠 Language

Python 3

📌 Concepts Used

File I/O

List of Dictionaries

CRUD Architecture

CLI Visualization

Error Handling

Feature Engineering

📦 Python Modules
csv
os
sys
📦 Data Structure Example

Each record is stored like:

{
  "year": 2020,
  "total": 220892331,
  "male": 112789321,
  "female": 108102010,
  "urban": 84358123,
  "rural": 136534208
}
⚡ Performance & Scalability

System supports:

10,000+ records

Fast file read/write

Efficient ordering and search

Low-memory operations

❗ Troubleshooting
🔹 File Not Found

Ensure the following exists:

pakistan_population.csv
🔹 Permission Errors

Run terminal as:

Administrator (Windows)

or

sudo (Linux/Mac)
🔹 ZeroDivisionError

Handled inside growth rate calculation.

💼 Skills Demonstrated

Python Programming

Data Engineering

CRUD System Design

Algorithmic Logic

CLI Visualization

Software Architecture

👤 Author

Noor Rauf

📍 Pakistan
📱 +92 03706783699
💼 LinkedIn: https://linkedin.com/in/noor-rauf-b38a7838b

💻 GitHub: https://github.com/NoorRauf005

⭐ Support This Project

If you find this useful, please ⭐ the repo and follow for more projects!
