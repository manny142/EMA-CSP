price = float(input("what is the cost of the item:"))

tax_rate = float(input("what is the tax percent in youre state:"))

tax_rate_decimal = tax_rate/100

total = round(price(1 + tax_rate_decimal))

rounded_total = round(total2)

print(price*(1 + tax_rate_decimal))