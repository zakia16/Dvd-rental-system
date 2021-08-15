from borrow import borrowDvd
from customer import Customer

def main():

    print("\t♦♦♦ WELCOME TO DVD Rentals ♦♦♦")
    print("""
        1. Show available number of dvds for renting
        2. Press 2 to rent a dvd
        3. Press 3 to Return a dvd
        4. Exit""")

    shop = borrowDvd(["The Quiet Place","Godzilla","Jumanji"])
    people = Customer()

    while True:
        option  = int(input("Enter option: "))

        if option  == 1:
            shop.showInventory()
        elif option  == 2:
            #shop = borrowDvd(1000)
            people.rentalTime = shop.rentDvds(people.requestDvds())
        elif option  == 3:
            people.rentalTime = shop.returnDvds(people.returnDvds())
            #people = Customer()
        elif option == 4:
            break
        else:
            print("Please enter valid option")
    print("Thank you. Have a nice day.")

main()
