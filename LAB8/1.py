# define a class Counter
class Counter:
    # initialize the counter value using constructor
    def __init__(self, value=0):
        self.value = value
    
    # define a method to increment the counter by 1
    def increment(self):
        self.value += 1
    
    # define a method to clear the counter to 0
    def clear(self):
        self.value = 0
    
    # define a method to display the current counter value
    def disp_value(self):
        print(f"Counter value: {self.value}")

# derive a class DecrementingCounter from Counter
class DecrementingCounter(Counter):
    # define a method to decrement the counter by 1
    def decrement(self):
        self.value -= 1

# create an object of DecrementingCounter class with initial value 10
dc = DecrementingCounter(10)

# call the methods on the object
dc.disp_value() # output: Counter value: 10
dc.increment() # increase by 1
dc.disp_value() # output: Counter value: 11
dc.decrement() # decrease by 1
dc.disp_value() # output: Counter value: 10
dc.clear() # reset to 0
dc.disp_value() # output: Counter value: 0