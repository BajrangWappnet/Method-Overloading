from multipledispatch import dispatch

class Overloading:
    
    # Printing below statement whenever object creates ::
    def __init__(self):
        print("Initializing Overload class")
     
    # Defining a method to take 2 parameters and return sum
    @dispatch(int,int)
    def area(self,a,b):
        print("Area is : ",a*b)
        
    # Overloading the sum method to take 3 parameters and return sum
    @dispatch(int,int,int)
    def area(self,a,b,c):
        print("Area is : ",a*b*c)


