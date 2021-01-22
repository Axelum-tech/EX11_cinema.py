# importing (add more functionality) "system"
from os import system

cinema=[0, 0, 1, 2, 0, 0, 0]
menu ="MENU\n0. Exit\n1. Show the map\n2. Book ticket\n3. Confirm booking"
option=-1


while option!=0:
    system("cls")    
    print(menu)
    option= int(input("your choice> "))

    if option ==0:
        print("Byeee!")


    elif option==1:
        print("CINEMA MAP")
        for n in range(1, len(cinema)+1,1):
            print("",n,end="  ")
        print()
        
        free_seats=0
        booked_seats=0
        sold_tickets=0
        for seat in cinema:
            if seat==0:
                print("[ ]", end=" ")
                free_seats+=1
            elif seat==1:
                print("[R]", end=" ")
                booked_seats+=1
            elif seat==2:
                print("[X]", end=" ")
                sold_tickets+=1

        print()
        print("Free seats:  ", free_seats)
        print("Booked seats:",booked_seats)
        print("Sold tickets:",sold_tickets)
        print()
        input(" >>>To return in main menu PRESS ENTER<<<")

    elif option==2:
        seat=int(input("Which seat?"))
        if cinema[seat-1]==1:
            print("Already booked!")
        elif cinema[seat-1]==2:
            print("Already sold!")
        else:
            cinema[seat-1]=1
            print("Ok, we have booked your seat")
        input(" >>>To return in main menu PRESS ENTER<<<")

    elif option==3:
        seat=int(input("Which seat do you want to confirm?"))
        if cinema[seat-1]==1:
            cinema[seat-1]=2
            print("Ok, your seat is confirmed")
        elif cinema[seat-1]==2:
            print("The place is already sold")
        else:
            print("You should book a place first!")
                     
        input(" >>>To return in main menu PRESS ENTER<<<")
       