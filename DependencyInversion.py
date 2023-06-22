# In object-oriented design, the dependency inversion principle is a specific form of decoupling software modules.
# When following this principle, the conventional dependency relationships established from high-level,
# policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent
# of the low-level module implementation details. The principle states:

# High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g.
# interfaces).Abstractions should not depend on details. Details (concrete implementations) should depend on
# abstractions. By dictating that both high-level and low-level objects must depend on the same abstraction,
# this design principle inverts the way some people may think about object-oriented programming.[2]

# The idea behind points A and B of this principle is that when designing the interaction between a high-level module
# and a low-level one, the interaction should be thought of as an abstract interaction between them. This not only
# has implications on the design of the high-level module, but also on the low-level one: the low-level one should be
# designed with the interaction in mind and it may be necessary to change its usage interface.

# In many cases, thinking about the interaction in itself as an abstract concept allows the coupling of the
# components to be reduced without introducing additional coding patterns, allowing only a lighter and less
# implementation-dependent interaction schema.

# When the discovered abstract interaction schema(s) between two modules is/are generic and generalization makes
# sense, this design principle also leads to the following dependency inversion coding pattern.

import time
from abc import ABC, abstractmethod


class PaymentMethods(ABC):
    @abstractmethod
    def payment(self):
        pass


class Contactless(PaymentMethods):

    def payment(self):
        print("Please scan your card.")
        print("Processing your payment ...")
        time.sleep(1)
        print("Your payment have been confirmed, have a nice day!")


class PIN(PaymentMethods):

    def payment(self):
        print("Please insert your card.")
        input("Enter your PIN: ")
        print("Correct password.")
        print("Processing your payment ...")
        time.sleep(1)
        print("Your payment have been confirmed, have a nice day!")


class IBAN(PaymentMethods):
    def payment(self):
        print("Send money to DE89370400440532013000")
        print("Processing your transfer ...")
        time.sleep(1)
        print("Your payment have been confirmed, have a nice day!")


class PaymentProcessor:
    def __init__(self, payment: PaymentMethods):
        self.payment = payment

    def pay(self):
        self.payment.payment()


pay = Contactless()
process = PaymentProcessor(pay)
process.pay()
















