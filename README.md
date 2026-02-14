📊 Pakistan Population Management System (1960-2022)
A Python-based project developed for my Programming Fundamentals (PF) course. This application processes historical demographic data to provide insights into population growth, gender distribution, and urbanization in Pakistan.

🚀 Key Features
Data Transformation: A custom converter.py script that cleans raw CSV data and calculates missing fields like male population and urban/rural splits.
Management System (CRUD): Users can add new records, view specific years, update existing data, and delete entries.
Analytics: Automatically calculates the annual growth rate between years.
CLI Visualization: Built-in histogram generator that creates visual bar charts directly in the terminal to show population surges over the decades.

🛠️ Tech Stack
Language: Python 3
Modules: os, csv
Data Handling: File I/O (Text and CSV processing)

📂 How to Run the Project
Run python converter.py to generate the processed data file.
Run python population_system.py to launch the interactive menu.

📈 Sample Output (Visualization)
The system generates terminal-based charts like this:
1960 | █ 45,954,226
2022 | █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 235,824,862
