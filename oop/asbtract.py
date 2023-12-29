from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input("how much you donate?")
        return a

donations = []

john = Donation()
donations.append(john.donate())
donations.append(john.donate())

print(donations)


