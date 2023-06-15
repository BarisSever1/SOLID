import time
from abc import abstractmethod, ABC

# Applications should be open to development but closed to change. Whenever we want to create a new class,
# we want to create this class comfortably. OOP already supports extensibility. However, it is necessary to establish
# the architecture in the classes created during this expansion so that no modification is required. For exaple lets
# think of a simple payment app, in this app we enter the total amount as an input and the app prints it with the
# payment company. In the Payments class we take input and print the payment copmpany related to if-else structures.
# However, the architecture in this scenario is contrary to this principle. If we want to follow this principle,
# we should define a method in an abstract class and use this method by overriding it in the classroom we will open
# for each payment company . In this way, I will not make a change in my existing classes for every payment company.
# With the help of the abstract class, we have kept our lower classes closed to change by setting rules


class Payments(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class Visa(Payments):
    def process(self, amount):
        print(f'Your summary is total {amount}$')
        print("Paying with Visa ...")
        time.sleep(1)
        print("Your payment has been recieved.")


class MasterCard(Payments):
    def process(self, amount):
        print(f'Your summary is total {amount}$')
        print("Paying with MasterCard ...")
        time.sleep(1)
        print("Your payment has been recieved.")


class AmericanExpress(Payments):
    def process(self, amount):
        print(f'Your summary is total {amount}$')
        print("Paying with American Express ...")
        time.sleep(1)
        print("Your payment has been recieved.")


class UnionPay(Payments):
    def process(self, amount):
        print(f'Your summary is total {amount}$')
        print("Paying with Union Pay ...")
        time.sleep(1)
        print("Your payment has been recieved.")



