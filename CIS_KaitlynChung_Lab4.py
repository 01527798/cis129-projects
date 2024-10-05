#Module 4 Lab-4
#Kaitlyn Chung
#10.05.2024
#This program determines bonuses given to employees based on the monthly sales and percent sale increase

#Declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
prompt = 'What are the monthly sales?' # prompt will be a string literal

#This code gets the monthly sales
monthlySales = float(input(prompt))

#Thise code determines the storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else: 
    storeAmount = 0

#This code gets the percent of increase in sales
salesIncrease = float(input('Please enter the percent of sales increase: '))
salesIncrease = salesIncrease / 100

#This code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#This code prints the bonus information
print("The store bonus amount is $",  storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')
