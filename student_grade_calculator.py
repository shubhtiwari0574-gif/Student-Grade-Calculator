Name=(input("Enter a Name :"))
marks = []
for i in range(5):
    while True:
        try:
            mark = int(input(f"Enter marks of subject {i+1}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Invalid marks. Try again.")
        except ValueError:
            print("Please enter a number")
TOTAL=sum(marks)
PERCENTAGE= round(TOTAL/500*100, 2)
if min(marks)<33:
    print("FAIL")
else :
    print("PASS")
    print(f"TOTAL Marks of {Name}:",TOTAL)
    print(f"PERCENTAGE of {Name}:",PERCENTAGE)
    if PERCENTAGE >= 80:
        print("Grade A")
    elif PERCENTAGE >= 60:
        print("Grade B")
    else:
        print("Grade C")
