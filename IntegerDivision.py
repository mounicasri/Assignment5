from random import randrange

print("Integer Divisions")
while(True):
    quit_option=input("Please enter q to quit or enter any other input")
    if(quit_option=="q"):
        break
    a=randrange(5)
    b=randrange(5)
    try:
        query=int(input("what is the value of "+str(a)+"/"+str(b)+"="))

        if(query==int(a/b)):
            print("Correct!")
        else:
            print("Incorrect!")
    except ZeroDivisionError:
        print("Number can't be Divided by zero")
    except ValueError:
        print("Please enter only integers")


##Integer Divisions
##Please enter q to quit or enter any other inputa
##what is the value of 2/1=2
##Correct!
##Please enter q to quit or enter any other inputa
##what is the value of 4/4=1
##Correct!
##Please enter q to quit or enter any other inputa
##what is the value of 1/4=4
##Incorrect!
##Please enter q to quit or enter any other inputa
##what is the value of 1/0=1
##Number can't be Divided by zero
##Please enter q to quit or enter any other inputa
##what is the value of 3/4=w
##Please enter only integers
##Please enter q to quit or enter any other inputq
