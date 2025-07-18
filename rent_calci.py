persons=int(input(" Enter the number of persons in your flat "))
rent = int(input(" Enter your flat rent "))
food = int(input(" Enter your food expenses "))
electricity = int(input(" Enter your electricity expenses "))
charge_per_unit = int(input(" Enter your charge per unit ="))

total_bill = electricity * charge_per_unit

output = (total_bill + food + rent)

print("The total bill for the flat is:", output, "and bill per person is", output / persons)



   
