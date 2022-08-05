#Guessing game
user_no = 10
question = input("Enter number: ")


#validation
try:
    # runs if input is valid
    user_no = float(user_no)
    print("horray,you entered a number")

    if (user_no >= 0):
        print("True")

    elif (user_no<=0): 
        print("false")
    
    else:
        print("error")

except:
    print("This is not a number")