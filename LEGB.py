# Varaible scope is where a variable is visible and acessable 
#   Scope resolution flows an order LEGB(Local, enclosed, global and built-in)

#Local scope 
def firstname():
    fn = "Ifeoma"
    print(fn)

def lastname():
    ln = "Ezeka"
    print(ln)

firstname()
lastname()

#print(ln)# This code will not work because local variables only work inside the function or object or class they were declare in 
def firstname():
    x = "Ifeoma"
    print(x)

def lastname():
    x = "Ezeka"
    print(x)

firstname()
lastname()
#This wouldnt normally work based on the fact that two variables cannot have the same name but here, they are not in the same function to rephrase that statement "Two variables in the same function,class or object can be given the same name unless you want to reassign that variable to be something else"

#Enclosed scope 
def firstname():
    x = "Ifeoma" #Enclosed variable 
    def lastname():
        x = "Ezeka"#Local variable
        print(x)#This will print out "Ezeka" normal 
    lastname()


firstname()

def firstname():
    x = "Ifeoma" #Enclosed variable 
    def lastname():
       # x = "Ezeka"#Local variable
        print(x)#This will print out "Ifeoma" Why? Well now, there is no more "local variable" the complier will now move to the next step look for an "Enclosed Varaible" 
    lastname()


firstname()

#Global scope
def firstname():
    print(x)#This will print names

def lastname():
        print(x)#This will also print names

x = "Names"
firstname()
lastname()

def firstname():
    x = "Ezeka"
    print(x)#This will print "Ezeka"

def lastname():
        x = "Ifeoma"
        print(x)#This will print "Ifeoma"

x = "Names"
firstname()
lastname()
#Why ? Remember the LEGB order, thats exactly the reason your compiler first of looks for a local variable, if it doesnt find one it the looks for an eclosed variable , if it doesnt it just uses the global variable.


#Built-in
from math import pi
#Pi is built-in
print(pi)#This will print out the value of PI 


def funcpi():
     print(pi)#This wll print out 34 because it has been over-written by 34 Remember this ? "Two variables in the same function,class or object can be given the same name unless you want to reassign that variable to be something else"

pi = 34
funcpi()