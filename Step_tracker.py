#Fitness tracker
#Allow the user to enter data about their steps per any given time
def functioninput():
    totalsteps = int(0)
    days = int(input("How many days would you like to enter?"))
    for index in range (days):
        steps = int(input( "enter steps"))
        totalsteps += steps
    print ("the total amount you walked is ", totalsteps)
    print ("average steps", totalsteps / days)
functioninput()

