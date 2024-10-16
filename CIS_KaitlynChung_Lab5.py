#Kaitlyn Chung
#10-15-24
#Lab 5: The Bottle Return Program
#A script that takes customer inputs for number of bottles collected throughout a week and outputs the total number of bottles and the payout for these bottles.

#Declaring and initializing variables below
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = 'y'

#Loop to run program again
while keep_going == 'y':
    counter = 1
    total_bottles = 0
    #getBottles code
    while counter <= 7:
        today_bottles = input(f'Enter number of bottles returned for day #{counter}: ')
        total_bottles = int(today_bottles) + int(total_bottles)
        counter += 1
    #calcPayout code
    PAYOUT_PER_BOTTLE = .10
    total_payout = PAYOUT_PER_BOTTLE*total_bottles
    #printInfo code
    print('\nThe total number of bottles collected is', total_bottles)
    print('The total paid out is $', format(total_payout,".2f"))
    print("\nDo you want to enter another week's worth of data?")
    keep_going = input('Enter y or n: ')
    print(' ')