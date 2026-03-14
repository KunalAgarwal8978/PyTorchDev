

#calculator program
input1= float(input("Please proivde input 1 which needs to numeric"))
input2=float(input("Please proivde input 2 which needs to numeric"))

operator=(input("please provide the kind of operation you want to perform:  + add, -:for subtract, *: for multiply, / :for divide)"))
x=6

if(operator=="+"):
     print("addition", input1+input2)
elif(operator=="-"):
     print("substraction", input2-input1)
elif(operator=="*"):
     print("multiply: ", input1*input2)
elif(operator=="/"):
     print("divide: ", input1/input2)
else:
     print("Invalid operator, please verify")


print("------ Welcome to the Shop ------")
print("1. Rice  - ₹50 per kg")
print("2. Sugar - ₹40 per kg")
print("3. Oil   - ₹120 per liter")
print("4. Milk  - ₹30 per packet")

choice = int(input("Enter product number: "))
qty = int(input("Enter quantity: "))

total = 0

if choice == 1:
    total = qty * 50
    item = "Rice"
elif choice == 2:
    total = qty * 40
    item = "Sugar"
elif choice == 3:
    total = qty * 120
    item = "Oil"
elif choice == 4:
    total = qty * 30
    item = "Milk"
else:
    print("Invalid choice")

if total > 0:
    print("\n----- BILL -----")
    print("Item:", item)
    print("Quantity:", qty)
    print("Total Price: ₹", total)

    if total > 500:
        discount = total * 0.10
        total = total - discount
        print("Discount Applied: ₹", discount)

    print("Final Amount: ₹", total)













price_of_house=True
size_of_the_house=True
Amenities=False
swimming=True
supermarket=False



if(Amenities):
     print("I will buy the house")
elif(swimming and supermarket):
     print("I will buy the house")
elif(swimming and supermarket):
     print("I will buy the house")
elif(swimming and supermarket):
     print("I will buy the house")
else:
     print("I will not buy the house")

















