#Problem Statemet - user will input 3 ages. Find the oldest one.
#Solution
First = int(input("Enter the age of first boy/girl: "))
Second = int(input("Enter the age of second boy/girl: "))
Third = int(input("Enter the age of third boy/girl: "))
if First > Second and First > Third :
    print("First is the elder")

elif Second > First and Second > Third :
    print("Second is the elder")

elif Third > First and Third > Second :
    print("Third is the elder")


