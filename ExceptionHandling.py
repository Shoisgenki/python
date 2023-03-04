# exception = events detected during execution that interrupt the normal flow of the program
try:
    numerator = int(input("Enter a number to divide :"))
    denominator = int(input("Enter a number to divide by :"))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("0? Seriously?")

except ValueError as e:
    print(e)
    print("Enter only numbers pls")

except Exception:
    print("Something went wrong :(")

else:
    print(result)

finally:
    print('This will always execute')
