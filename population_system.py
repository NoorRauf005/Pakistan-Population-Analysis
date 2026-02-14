import os

DATA_FILE = "population_data.txt"

def load_data():
    records = []
    if not os.path.exists(DATA_FILE):
        print("⚠️  Warning: Data file not found. Please run converter.py first!")
        return records
    with open(DATA_FILE, "r") as f:
        next(f) 
        for line in f:
            p = line.strip().split(",")
            if len(p) == 7:
                records.append({
                    'area': p[0], 'year': int(p[1]), 'male': int(p[2]),
                    'female': int(p[3]), 'urban': int(p[4]), 'rural': int(p[5]),
                    'total': int(p[6])
                })
    return records

def show_growth_rate(data):
    """Calculates and displays the population growth rate between consecutive years"""
    if len(data) < 2:
        print("❌ Not enough data to calculate growth rate.")
        return
    
    sorted_data = sorted(data, key=lambda x: x['year'])
    print("\n" + "📈" + "—"*45 + "📈")
    print(f"{'Year Range':<15} | {'Population Change':<20} | {'Growth Rate'}")
    print(" " + "—"*45)
    
    # Calculate rate: ((New - Old) / Old) * 100
    for i in range(1, len(sorted_data)):
        old_pop = sorted_data[i-1]['total']
        new_pop = sorted_data[i]['total']
        year_prev = sorted_data[i-1]['year']
        year_curr = sorted_data[i]['year']
        
        change = new_pop - old_pop
        rate = (change / old_pop) * 100
        
        # Add a + sign for positive growth
        symbol = "+" if rate > 0 else ""
        print(f"{year_prev}-{year_curr:<5} | {change:<20,} | {symbol}{rate:.2f}%")
    print("📈" + "—"*45 + "📈")

def show_report_view(data):
    """Detailed Report View for a single year"""
    try:
        y = int(input("📄 Enter Year for Detailed Report: "))
        found = False
        for r in data:
            if r['year'] == y:
                print("\n" + "📜" + "—"*40 + "📜")
                print(f"       POPULATION REPORT: {y}")
                print(" " + "—"*40)
                print(f"🌍 Region:           {r['area']}")
                print(f"👥 Total Population: {r['total']:,}")
                print(f"👨 Male population:  {r['male']:,}")
                print(f"👩 Female population:{r['female']:,}")
                print(f"🏢 Urban Area:       {r['urban']:,}")
                print(f"🚜 Rural Area:       {r['rural']:,}")
                print(" " + "—"*40)
                u_per = (r['urban']/r['total'])*100
                print(f"💡 Analysis: {u_per:.1f}% of people live in cities.")
                print("📜" + "—"*40 + "📜")
                found = True
                break
        if not found:
            print("❌ No data found for that year.")
    except ValueError:
        print("❌ Please enter a valid year number.")

def show_table(data):
    """Full Table View including Rural and Urban"""
    if not data: return
    sorted_data = sorted(data, key=lambda x: x['year'])
    print("\n" + "═"*115)
    print(f"║ {'Year':<6} ║ {'Total Population':<18} ║ {'Male':<15} ║ {'Female':<15} ║ {'Urban':<15} ║ {'Rural':<15} ║")
    print("╠" + "═"*113 + "╣")
    for r in sorted_data:
        print(f"║ {r['year']:<6} ║ {r['total']:<18,} ║ {r['male']:<15,} ║ {r['female']:<15,} ║ {r['urban']:<15,} ║ {r['rural']:<15,} ║")
    print("═"*115)

def update_record(data):
    try:
        year = int(input("📝 Enter year to update: "))
        for r in data:
            if r['year'] == year:
                r['male'] = int(input("  New Male Pop: "))
                r['female'] = int(input("  New Female Pop: "))
                r['urban'] = int(input("  New Urban Pop: "))
                r['rural'] = int(input("  New Rural Pop: "))
                r['total'] = r['male'] + r['female']
                print("✅ Update Complete!")
                return data
        print("❌ Not found.")
    except ValueError:
        print("❌ Invalid input.")
    return data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        f.write("area,year,male,female,urban,rural,total\n")
        for r in sorted(data, key=lambda x: x['year']):
            f.write(f"{r['area']},{r['year']},{r['male']},{r['female']},{r['urban']},{r['rural']},{r['total']}\n")
    print("💾 Progress Saved!")

def main_menu():
    data = load_data()
    while True:
        print("\n🌟 " + "="*43 + " 🌟")
        print("    PAKISTAN POPULATION MANAGEMENT SYSTEM")
        print("🌟 " + "="*43 + " 🌟")
        print("1. 📋 View Full Table       2. 🔍 Search Year")
        print("3. 📊 Quick Stats           4. 📉 Growth Graph")
        print("5. 🆕 Add Record            6. 📝 Update Record")
        print("7. 🗑️  Delete Record         8. 💾 Save Progress")
        print("9. 📄 REPORT VIEW           10.📈 GROWTH RATE")
        print("11.🚪 Exit")
        
        choice = input("\n👉 Select Option: ")
        
        if choice == '1': show_table(data)
        elif choice == '2':
            y = int(input("Search Year: "))
            for r in data:
                if r['year'] == y: print(f"✅ Found: {r}")
        elif choice == '3':
            if data:
                latest = max(data, key=lambda x: x['year'])
                print(f"\n📊 --- LATEST DATA ({latest['year']}) ---")
                print(f"Total: {latest['total']:,} | Urban: {latest['urban']:,}")
        elif choice == '4':
            # --- MODIFIED PART START ---
            print("\n📈 POPULATION GROWTH VISUALIZATION")
            print("Each █ represents approx. 10 Million people")
            print("-" * 65)
            for r in sorted(data, key=lambda x: x['year']):
                bar = "█" * (r['total'] // 10000000)
                # Added numerical label next to the bar
                print(f"{r['year']} | {bar:<25} {r['total']:,}")
            print("-" * 65)
            # --- MODIFIED PART END ---
        elif choice == '5':
            y = int(input("Year: ")); m = int(input("M: ")); f = int(input("F: "))
            u = int(input("U: ")); ru = int(input("R: "))
            data.append({'area':'Pakistan','year':y,'male':m,'female':f,'urban':u,'rural':ru,'total':m+f})
        elif choice == '6': data = update_record(data)
        elif choice == '7':
            y = int(input("Delete Year: "))
            data = [r for r in data if r['year'] != y]
        elif choice == '8': save_data(data)
        elif choice == '9': show_report_view(data)
        elif choice == '10': show_growth_rate(data)
        elif choice == '11': break

if __name__ == "__main__":
    main_menu()