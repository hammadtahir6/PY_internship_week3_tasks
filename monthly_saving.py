try:
    salary = float(input("enter ypur salary: "))
    expenses = float(input("enter your expenses"))

    savings = salary - expenses

    if savings > 10000:
        print("Your saving is ,well")
    elif 5000 <= savings <= 9999:
        print("your saving is average")
    else:
        print("try to save more  money")
    
except ValueError:
    print("error: try using numeric values")

