# student_scores = {
#     'Harry': {'score': 88, 'grade': 'A'},
#     'Ron': {'score': 78, 'grade': 'B'},
#     'Hermione': {'score': 95, 'grade': 'A'},
#     'Draco': {'score': 75, 'grade': 'B'},
#     'Neville': {'score': 60, 'grade': 'C'}
# }

# for name, details in student_scores.items():
#     print(f"{name}: {details['grade']}")

# nestd_list = ["A", "B", ["C", "D"]]
# print(nestd_list[2][0])


# student_scores = [100, 90, 95, 80, 85, 70, 75, 60, 65,]

# if student_scores == 100 or student_scores >= 88:
#     student_grades = 'A'
# elif student_scores == 88 or student_scores >= 78:
#     student_grades = 'B'
# elif student_scores == 75 or student_scores >= 60:
#     student_grades = 'C'

# for grades in student_scores:
#     grades = student_grades
#     print(grades)

# user_name1 = input("enter your name! ")
# user_name2 = input("enter your name! ")
# combine_names = user_name2 + user_name1
# lover_case_letter = combine_names.lower()



# for letter in combine_names:
    
#     print(letter)

# t = lover_case_letter.count('t', 'k',)
# print(t)

# import cal

# print(cal)

# def is_prime(num):
#     if num < 2:
#         print("False")
        
#     else:
#         check_prime = True
#         for numbers in range(2, num):
#             if num % numbers == 0:
#                 check_prime = False
#                 break
            
#         if check_prime:
#             print("True")
            
#         else:
#             print("False")
        
# is_prime(3)

i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)

# input = int(input("enter number: "))

# for i in range(2, input):
#     print(i)
