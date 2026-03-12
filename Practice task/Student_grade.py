# Student grade system using function
#    Requierments
# 1. Take marks for 3 subjects
# 2. Calculate average
# 3. Assign grade
# 4. Display result

def get_marks():
    Sub1 = int(input("Enter the 1st subject mark: "))
    Sub2 = int(input("Enter the 2nd subject mark: "))
    Sub3 = int(input("Enter the 3rd subject mark: "))

    return Sub1, Sub2, Sub3

def avergae(Sub1, Sub2, Sub3):
    avg = (Sub1+Sub2+Sub3) / 3
    return avg

def find_grade(avg):
    if avg >= 90:
        return "O"
    elif avg >=80:
        return "E"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"
    
def show_result(Sub1, Sub2, Sub3, avg, grade):
    print("||----Result----||")
    print("Markes obtain in 1st subject: ", Sub1)
    print("Markes obtain in 2nd subject: ", Sub2)
    print("Markes obtain in 3rd subject: ", Sub3)
    print("Average mark: ", avg)
    print("Grade: ", grade)

Sub1, Sub2, Sub3 = get_marks()
avg = avergae(Sub1, Sub2, Sub3)
grade = find_grade(avg)
show_result(Sub1, Sub2, Sub3, avg, grade)