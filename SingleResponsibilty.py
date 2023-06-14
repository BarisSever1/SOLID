# A class should have one and only one reason to change, meaning that a class should only have one job.
# For example, let's assume that we have a simple application that logs every customers info, expenses
# and calculates daily endersoment. We can carry out these operations in a single class.
# If we do this in this way, we would be at odds with this principle.
# To comply with this principle, we need to handle all these processes in separate classes.
# Each class should have only one responsibility.
# For example, a class should be used for creating a new customer,
# a class for logging and a class for calculating endorsement.


class NewCustomer:
    customers = []

    def __init__(self, full_name: str, spent, product):
        self.full_name = full_name.strip()
        self.spent = spent
        self.product = product
        NewCustomer.customers.append(self.full_name.strip())


class LogCustomer:
    def log_create(self):
        log = open(file="daily_log.txt", mode="w", encoding="utf-8")
        log.close()

    def logger(self, full_name: str, spent, product):
        log = open(file="daily_log.txt", mode="a", encoding="utf-8")
        log.write(f"{full_name} --> {product} {spent}$")


class DailyEndorsement:
    def endersoment_calculator(self):
        res = 0
        log = open(file="daily_log.txt", mode="r", encoding="utf-8")
        for i in log.readlines():
            x = i.split(" --> ")[1].split(" ")[1].replace("$", "")
            res += int(x)
        print(res)










