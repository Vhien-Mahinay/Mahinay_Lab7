#Input student informations
student_fullname = (input("Enter Student Full Name:"))
student_section = (input("Enter Student Section:"))
prelim_grade = float(input("Enter Prelim Grade:"))
midterm_grade = float(input("Enter Midterm Grade:"))
finals_grade = float(input("Enter Finals Grade:"))

#Calculation of final grades

if prelim_grade > 100 or midterm_grade > 100 or finals_grade > 100:
    print("Invalid Input. Please Input and grade from 40 to 100")
elif prelim_grade < 40 or midterm_grade < 40 or finals_grade < 40:
    print("Invalid Input. Please Input and grade from 40 to 100")
else:

    finalgrade = prelim_grade * 0.3333 + midterm_grade * 0.3333 + finals_grade * 0.3333
    finalgrade_percentage = round(finalgrade)


if finalgrade_percentage >= 99 and finalgrade_percentage <=100:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 1.00, he or she has an Exellent Remark!")
elif finalgrade_percentage >=96 and finalgrade_percentage <=98:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 1.25, he or she has an Outstanding Remark!")
elif finalgrade_percentage >=93 and finalgrade_percentage <=95:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 1.50, he or she has a Superior Remark!")
elif finalgrade_percentage >=90 and finalgrade_percentage <=92:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 1.75, he or she has a Very Good Remark!")
elif finalgrade_percentage >=87 and finalgrade_percentage <=89:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 2.00, he or she has a Good Remark!")
elif finalgrade_percentage >=84 and finalgrade_percentage <=86:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 2.25, he or she has a Satisfactory Remark!")
elif finalgrade_percentage >=81 and finalgrade_percentage <=83:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 2.50, he or she has a Fairly Satisfactory Remark!")
elif finalgrade_percentage >=78 and finalgrade_percentage <=80:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 2.75, he or she has a Fair Remark!")
elif finalgrade_percentage >=75 and finalgrade_percentage <=77:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 3.00, he or she has a Passing Remark!")
elif finalgrade_percentage <=75:
    print(f"{student_fullname} from {student_section} has a Final Grade Average of {finalgrade_percentage} and grade point of 5.00, he or she has a Failing Remark.")