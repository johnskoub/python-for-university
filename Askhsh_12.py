import datetime
x = int(input("Enter year: "))
y = int(input("Enter month: "))
z = int(input("Enter day: "))

my_date = datetime.datetime(x, y, z)
now_date = datetime.datetime.now()
diff = abs(my_date - now_date)
seconds = diff.seconds
hours = seconds // 3600                         # Παίρνω ακέραιο πηλίκο της διαίρεσης για να βρώ τις ώρες αφού 3600 δευτερόλεπτα είναι μια ώρα! 
seconds = seconds % 3600                        # Παίρνω ακέραιο υπόλοιπο της διαίρεσης για να βρώ τα δευτερόλεπτα!
print(" The given date is: ", my_date.strftime("%d/%m/%Y"))
print(" The current date is: ",  now_date)
print(" The difference between the two dates is: ")
print(diff.days, "days,", hours, "hours and", seconds, "seconds!")

if y <= 7:                                      # Ελέγχω πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας που δώσαμε!
    if y != 2:
        if y % 2 == 1:
            print("The month has: 31 days")
        else:
            print("The month has: 30 days")
    else:                                       # Κάνω έλεγχω αμα είναι δίσεκτο το έτος!
        if x % 4 == 0:
            if x % 100 != 0:
                print ("The month has: 29 days")
        elif x % 400 == 0:
            print ("The month has: 29 days")
        else:
            print ("The month has: 28 days")
else:
    if y% 2 == 0:
        print("The month has: 31 days")
    else:
        print("The month has: 30 days")