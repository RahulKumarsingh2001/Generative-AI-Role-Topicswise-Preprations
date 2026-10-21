# A decorator in Python is a function that adds extra functionality 
# to another function or method without changing its original code.



def mydecorator(fun):
    def wapper():
        print('Before....')
        fun()
        print('After.....')
    return wapper    


@mydecorator
def greet():
    print('hey buddy')
    
greet();    


def greet():
    print('hey buddy')
    
greet = mydecorator(greet()) 