try:
    attendence = float(input("enter your attendence percentage: "))
    marks = float(input("enter your marks: "))

    if attendence >=75 and marks >=50:
        print("you are PROMOTED")
    else:
        print("you are NOT promoted")
except ValueError:
    print("enter numerical values ")