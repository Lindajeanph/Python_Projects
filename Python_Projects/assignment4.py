from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
        @abstractmethod
        def payment(self, amount):
            pass

        
class DebitCardPayment(car):
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))
obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")


#the abstraction class

class variable(ABC):
    def print(self, y):
        print("passed value:", y)
    @abstractmethod
    def task(self):
        print("This is the task section")

class example_class(variable):
    def task(self):
        print("This is the example task")

example_obj = example_class()
example_obj.task()
example_obj.print(200)

