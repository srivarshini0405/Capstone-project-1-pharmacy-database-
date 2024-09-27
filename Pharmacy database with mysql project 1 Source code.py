import pymysql

# Establishing the connection to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='rama123',
    database='pharmacy_dp'
)

cursor = connection.cursor()

# Function to add medicine details
def add_medicine():
    medicine_name = input("Enter Medicine_Name: ")
    category = input("Enter the Category: ")
    price = input("Enter the price: ")
    stock = input("Enter the stock: ")
    sql = "INSERT INTO Medicine(medicine_name, category, price, stock) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (medicine_name, category, price, stock))
    connection.commit()
    print("Medicine added successfully!")

# Function to display medicine details
def display_medicine():
    sql = "SELECT * FROM Medicine"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(f"Medicine_Name: {row[0]}, Category: {row[1]}, price: {row[2]}, stock: {row[3]}")

# Function to list medicine by category
def list_medicine_by_category():
    category = input("Enter category Name: ")
    sql = "SELECT * FROM Medicine WHERE category = %s"
    cursor.execute(sql, (category,))
    for row in cursor.fetchall():
        print(f"Medicine_Name: {row[0]}, Category: {row[1]}, price: {row[2]}, stock: {row[3]}")

# Function to count the number of medicines
def count_medicine():
    sql = "SELECT COUNT(*) FROM Medicine"
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    print(f"Total number of medicines: {count}")

# Main menu
def main():
    while True:
        print("\nApolla Pharmacy System")
        print("1. Add medicine details")
        print("2. Display medicine details")
        print("3. List medicine by category")
        print("4. Count the number of medicines")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_medicine()
        elif choice == '2':
            display_medicine()
        elif choice == '3':
            list_medicine_by_category()
        elif choice == '4':
            count_medicine()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    # Closing the connection
    connection.close()
