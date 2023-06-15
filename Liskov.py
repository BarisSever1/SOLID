import random
from abc import abstractmethod, ABC
from builtins import print, input, int
from pprint import pprint
from random import randint
import builtins

# It expects that objects consisting of subclasses behave the same when they are replaced by objects of the parent
# class, such that the objects formed in the subclasses must be interchangeable with the objects of the upper
# classes. For example, we have an application, and it has a parent class called SendOTP and two child classes called
# SMSOTP and EmailOTP. When we initialize an object with parent class, it takes two arguments: otp and email. It
# works great while using EmailOTP. However, when we want to use SMSOTP we enter a phone number instead of email. We
# will be disoriented from the logic and purpose of the ancestral classes , and we are going against this principle.
# To fix this error, we need to create a class that contains common functions and arguments of OTP
# sending methods.

# Not applying Liskov Substitution Principle

# from abc import ABC, abstractmethod
#
#
# class SendOTP(ABC):
#     @abstractmethod
#     def notify(self, message, email):
#         pass
#
#
# class EmailOTP(SendOTP):
#     def notify(self, message, email):
#         print(f'Send {message} to {email}')
#
#
# class SMSOTP(SendOTP):
#     def notify(self, message, phone):
#         print(f'Send {message} to {phone}')

# Applying Liskov Substitution Principle


class SendOTP:
    @abstractmethod
    def otp_send(self, otp):
        pass

    def set_otp(self):
        pass


class EmailOTP(SendOTP):
    def __init__(self, email):
        self.email = email

    def otp_send(self, otp):
        print(f"Sending {otp} to the email -> {self.email}")

    def set_otp(self):
        return random.randint(1000, 9999)


class SMSOTP(SendOTP):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def otp_send(self, otp):
        print(f"Sending {otp} to the number -> {self.phone_number}")

    def set_otp(self):
        return random.randint(1000, 9999)


user = SMSOTP("053345689689")
user.otp_send(user.set_otp())
