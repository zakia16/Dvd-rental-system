import datetime

class borrowDvd:
    def __init__(self,listofdvds):
        self.availableDvds = listofdvds

    def showInventory(self):
        #print(f"We have total {self.availableDvds} dvds for rent.")
        for dvd in self.availableDvds:
                         print(dvd)
        return len(self.availableDvds)

    def rentDvds(self, requestedBook):
        now = datetime.datetime.now()

        if requestedBook in self.availableDvds:
                  print(f"Thank you for renting {requestedBook} dvd(s) with a charge of $2 per dvd per day.")
                  self.availableDvds.remove(requestedBook)
        else:
                  print("Sorry the book you have requested is currently not in the library")
        #self.availableDvds = self.availableDvds-n
        return now

    def returnDvds(self, request):
        rentalTime, returnedDvd = request
        self.availableDvds.append(returnedDvd)

        if rentalTime:
            #self.availableDvds += numOfDvds
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
            bill = round(rentalPeriod.days) * 2
            print(f"Your total bill is ${bill}")
        else:
            print("Sorry! You have not rented Dvds with us")
            return None
