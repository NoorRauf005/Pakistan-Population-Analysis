import csv
import os

def run_converter():
    print("🚀 Starting Data Conversion...")
    csv_file = "pakistan_population.csv"
    output_file = "population_data.txt"
    
    if not os.path.exists(csv_file):
        print("❌ CSV not found!")
        return

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            with open(output_file, 'w') as out:
                out.write("area,year,male,female,urban,rural,total\n")
                for row in reader:
                    year = int(row['Year'])
                    total = int(float(row['Population, total']))
                    female = int(float(row['Population, female']))
                    urban = int(float(row['Urban population']))
                    rural = int(float(row['Rural population']))
                    male = total - female
                    out.write(f"Pakistan,{year},{male},{female},{urban},{rural},{total}\n")
            
        print(f"✅ Created {output_file} with Gender and Urban/Rural data!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_converter()