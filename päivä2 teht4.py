#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
summa = float(input("What was the total bill? $"))
tippi = int(input("What percentage tip would you like to give? "))
hlö = int(input("How many people to split the bill? "))
kerroin = tippi/100+1
yht = summa*kerroin
osuus = yht/hlö
pyör_osuus = ("{:.2f}".format(round(osuus,2)))
print(f"each person should pay {pyör_osuus} $")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60