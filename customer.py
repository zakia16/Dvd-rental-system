
class Customer:
    def __init__(self):
        self.flag_dvd = 0
        self.rentalTime = 0

    def __del__(self):
        print('Destructor called, Customer deleted.')

    def requestDvds(self):
        print("Which dvd would you like to rent?")
        self.dvd=input()
        self.flag_dvd = 1
        return self.dvd

    def returnDvds(self):
        #dvds = input("Which dvd would you like to return?")
        print("Which dvd would you like to return?")
        self.dvds=input()
        if self.flag_dvd:
            return self.rentalTime, self.dvds
        else:
            return 0,0
