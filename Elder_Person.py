#Problem Statemet - user will input 3 ages. Find the oldest one.
#Solution
age_1 = int(input("Enter the age of first boy/girl: "))
age_2 = int(input("Enter the age of second boy/girl: "))
age_3 = int(input("Enter the age of third boy/girl: "))
if age_1 > age_2 and age_1 > age_3 :
    print("First person is the elder")

elif age_2 > age_1 and age_2 > age_3 :
    print("Second person is the elder")

elif age_3 > age_1 and age_3 > age_2 :
    print("Third person is the elder")


