#Name: Shahida Hoque
#Email: shahida.hoque03@myhunter.cuny.edu
#Date: April 21, 2020

def computePrice(ageGroup, ticketType):

    price = 0
    if ageGroup == "adult" and ticketType == "admission":
        price = 23
    elif ageGroup == "child" and  ticketType == "admission":
        price = 13
    elif ageGroup == "senior" and  ticketType == "admission":
        price = 18
    elif ageGroup == "adult" and  ticketType == "+exhibitions":
        price = 33 
    elif ageGroup == "child" and  ticketType == "+exhibitions":
        price = 20
    elif ageGroup == "senior" and  ticketType == "+exhibitions":
        price = 27
    else:
        price = -1
    return(price)

def main():
     a = input('Enter the age group (child, adult, senior): ')
     t = input('Enter the ticket type (admission / +exhibitions): ').lower()
     price = computePrice(a,t)
     print('The price of your ticket is', price)

#Allow script to be run directly:
if __name__ == "__main__":
     main()

