#welcome statement
print("WELCOME TO THE RESTAURANT")

#Input
FoodAmount = int(input("ENTER YOUR20 AMOUNT"))

NOofPerson = int(input("ENTER TOTAL NUMBER OF PERSON"))

TipPercentage = int(input("ENTER TIP`S PERCENTAGE"))

#Calculation

TipPercentage = FoodAmount*2/100

TotalAmount = FoodAmount+TipPercentage

PerPersonBill = TotalAmount/NOofPerson

#output

print(TotalAmount)
print(PerPersonBill)






