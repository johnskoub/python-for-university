num = int(input("Enter number: "))
new_num = num * 3 + 1
while len(str(new_num)) > 1:
    Str = str(new_num)
    List = list(Str)
    Sum = 0
    for i in List:
        Sum = Sum + int(i)
    new_num = Sum
    if new_num >= 10:
        new_num = new_num * 3 + 1
print("The final summary is: ")
print(new_num) 