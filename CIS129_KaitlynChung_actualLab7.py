#Kaitlyn Chung
#10/24/24
#CIS129 Lab 7 (actual lab 7)

nameA = 'A'
ticketsA = 0 #Initialize the number of tickets sold in section A
maxA = 300 #Maximum number of seats in section A
priceA = 20 #Price of a seat in section A
nameB = 'B'
ticketsB = 0 #Initialize the number of tickets sold in section B
maxB = 500 #Maximum number of seats in section B
priceB = 15 #Price of a seat in section B
nameC = 'C'
ticketsC = 0 #Initialize the number of tickets sold in section C
maxC = 200 #Maximum number of seats in section C
priceC = 10 #Price of a seat in section C

def ticketsSold(sectionName, maximum): #Determines the number of tickets sold in the inputted section
    print(f'How many tickets were sold in section {sectionName}?')
    tickets = input()
    while not tickets.isnumeric() or int(tickets) < 0 or int(tickets) > maximum:
        print('Invalid entry. Number of tickets is not in the approved range or not an integer.')
        print(f'How many tickets were sold in section {sectionName}?')
        tickets = input()
    return int(tickets)

ticketsA = ticketsSold(nameA, maxA)
ticketsB = ticketsSold(nameB, maxB)
ticketsC = ticketsSold(nameC, maxC)

sales = ticketsA * priceA + ticketsB * priceB + ticketsC * priceC

print('$',sales, 'were made from ticket sales')
    