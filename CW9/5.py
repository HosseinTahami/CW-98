def number_recognizer(num:str):
    try :
        num = int(num)
    except ValueError:
        return("Invalid Input !")
    
    result = "Positive number" if num > 0 else "Zero" if num == 0 else "Negative number" 
    return result


num = input("Enter a number: ")
print(number_recognizer(num))