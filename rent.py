money = float(input("how much do you earn in a month: $"))
rent = float(input("how much is ypure rent?: $"))
utilities = float(input("how ,much do you spend on utilities?: $"))
groceries = float(input("how much is do you spend on groceries: $"))
transportation = float(input("how much do you spend on transportion?: $"))

save = money*0.10
left = money - rent - utilities - groceries - transportation
remt = rent/money*100
print(f"youre rent is ${rent} and that is {remt}% of you income")    
print(f"Your utilities are ${utilities} and that is 7 % of your income.")
print(f"Your groceries are ${groceries} and that is 8 % of your income.")                    
print(f"Your transportation is ${transportation} and that is 17 % of your income.")    
print(f"You should save ${save} a month, that is 10 % of your income.") 
print(f"You have {left}% of spending money each month! ")   