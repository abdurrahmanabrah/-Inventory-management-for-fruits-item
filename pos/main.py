import csv
fh=open("inventoryforFruitsitem.csv","w+",newline="")
w=csv.writer(fh)
# fruits name, unit price, quantity and total price
header=["Fruits Name","Unit Price","quantity","total price"]
w.writerow(header)
data=[]
#Take item data from the user
while True:
    try:
        n=int(input("How many insert Fruits Record:?"))
    except ValueError:
        print("Fruits Record are Number Please again Entered!")
        continue
    else:
        break
for i in range(n):
    print("Enter Fruit record (0):",i+1)
    fruitsname=input("Enter Fruits Name: ")
    while True:
        try:
            unitprice=float(input("Enter Unit Price: "))
        except ValueError:
            print("Invalid Unit price Please Entered Again")
            continue
        else:
            break
    while True:
        try:
            quantity=int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity Please Entered Again")
            continue
        else:
            break
    totalprice = unitprice*quantity
    # Store items data into CSV(comma-separated values) file
    rec=[fruitsname,unitprice,quantity,totalprice]
    data.append(rec)
w.writerows(data)
fh.close()
#Print fruits items summary data from stored CSV file
print("Print fruits items summary data from stored CSV file")
fh=open("inventoryforFruitsitem.csv","r")
r=csv.reader(fh)
for i in r:
    print(i)
fh.close()

"""
import csv

filename = "inventoryforFruitsitem.csv"

header=["Fruits Name","Unit Price","quantity","total price"]

data=[]

while True:
    try:
        n=int(input("How many fruits records do you want to insert? "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        continue
    else:
        break

for i in range(n):
    print(f"Enter Fruit record ({i+1}):")
    fruitsname=input("Enter Fruits Name: ")
    while True:
        try:
            unitprice=float(input("Enter Unit Price: "))
            if unitprice <= 0:
                raise ValueError
        except ValueError:
            print("Invalid Unit price. Please enter a positive number.")
            continue
        else:
            break
    while True:
        try:
            quantity=int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Please enter a positive integer.")
            continue
        else:
            break
    totalprice = unitprice*quantity
    # Store items data into CSV(comma-separated values) file
    rec={"fruitsname": fruitsname, "unitprice": unitprice, "quantity": quantity, "totalprice": totalprice}
    data.append(rec)

# Write data to CSV file
with open(filename, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=header)
    w.writeheader()
    w.writerows(data)

# Print fruits items summary data from stored CSV file
print("Fruits items summary data:")
with open(filename, "r") as fh:
    r = csv.DictReader(fh)
    for row in r:
        print(row["Fruits Name"], row["Unit Price"], row["quantity"], row["total price"])
"""