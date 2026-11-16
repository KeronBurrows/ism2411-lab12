# REFLECTION
#
# 1. Python and Excel can both organize, calculate, and analyze data.
# Python makes it easier to automate repetitive tasks, process large amounts of data, and save results to files.
# Excel is better for quickly viewing data, creating charts, and making manual changes.
#
# 2. A business could use an append-mode log to track customer orders as they are processed.
# Append mode is useful because it adds each new order without deleting previous records, creating a continuous history.
import csv

# EXERCISE 2: Read and print raw rows
print("EXERCISE 2: Raw Rows")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3: Skip the header
print("\nEXERCISE 3: Skip Header")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: Compute totals
print("\nEXERCISE 4: Compute Totals")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")
# EXERCISE 5: Filter and write
print("\nEXERCISE 5: Filter and Write")

rows_written = 0
original_rows = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                rows_written += 1

print(f"Rows written: {rows_written}")
print(f"Original rows: {original_rows}")
# EXERCISE 6: csv.DictReader
print("\nEXERCISE 6: DictReader")

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader total revenue: ${dict_total_revenue:.2f}")

# csv.reader accesses columns using numerical indexes, while DictReader uses column names.
# DictReader is preferable when column names make the code easier to understand.
# EXERCISE 7: Sales summary by product
print("\nEXERCISE 7: Sales Summary")

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")
# EXERCISE 8: Append mode log
from datetime import datetime

print("\nEXERCISE 8: Append Mode Log")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")

print("Run log updated successfully.")