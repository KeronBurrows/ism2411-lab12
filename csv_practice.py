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