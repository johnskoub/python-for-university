number = int(input("Enter number: "))
if len(str(number)) == 16:
    sum = 0
    _str = str(number)
    for i in range(len(_str)):
        y = number % 10                     # Παίρνω κάθε φορά το τελευταίο ψηφίο του number
        number = number // 10               # Και το number κάθε φορά γίνεται το ακέραιο υπόλοιπο του 10
        if i % 2 == 1:                      # το y ειναι το καθε τελευταίο ψηφίο και επειδή στην αρχή το τελευταιο ψηφιο είναι στην θέση 15 μας ενδιαφέρουν οι περιττοί αριθμοί. 
            y = y * 2
            if y > 9:
                y = y % 10 + y // 10
        sum = sum + y
    apotel = sum % 10
    if apotel == 0:
        print ("The number is valid!")
    else:
        print ("The number is not valid!")
else:
    print("The number must be 16 digits")

    
        
        