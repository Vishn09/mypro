import sys

def addi(a,b):

    s=a+b
    return s

def subti(a,b):

    subt=a-b
    return subt


def divi(a,b):

    try:
        d=a/b
    except ZeroDivisionError:

        print("Plase enter values properly")

    



a=int(input("enter a :"))
b=int(input("enter b: "))
operation=input(("enter operation:"))


if operation=="add":
    output=addi(a,b)
    print(output)
if operation=="div":
    output=divi(a,b)
    print(output)
if operation=="s":
    output=subti(a,b)
    print(output)

else:
    print("Enter a valid option")
   