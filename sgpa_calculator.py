subjects_ = int(input(" Enter the Number of subjects "))
labs_ = int(input(" Enter the Number of lab Externals "))
points_subject = []
credits_sum = 0
for i in range (subjects_):
	print(i+1,end= '.subject  Credits =  ')
	credits_ = int(input())
	points_subject.append(credits_)
	credits_sum = credits_+credits_sum
lab_credits = []
lab_credits_sum = 0
for i in range(labs_):
	 print(i+1,end= '.lab  Credits =  ')
	 labs_credits = float(input())
	 lab_credits.append(labs_credits)
	 lab_credits_sum = labs_credits +lab_credits_sum
total_credits = lab_credits_sum+credits_sum
print(total_credits)
list_grades_Fixed = ["A+","A","B","C","D","E","F"]
subject_grades = []
points_of_grades = [10,9,8,7,6,5,0]
for i in range(subjects_):
	 grades = input((" subject grades "))
	 grades_ = grades.upper( )
	 subject_grades.append(grades_)
lab_grades = []
for i in range (labs_):
	 grades = input((" lab grades "))
	 lab_grade = grades.upper( )
	 lab_grades.append(lab_grade )
credits_obtain = []
for i in subject_grades:
	if i in list_grades_Fixed:
		b = list_grades_Fixed.index(i) 
		credits_obtain.append(b)
points_subject_obtained = []
for i in credits_obtain:
	points_obtain = points_of_grades[i]
	points_subject_obtained.append(points_obtain)
pc = 0
for a,b in zip(points_subject_obtained,points_subject):
	pc = a*b + pc
print(" Subject point * subject credits =  ", pc)
credits_obtain_lab= []
for i in lab_grades:
	if i in list_grades_Fixed:
		b = list_grades_Fixed.index(i) 
		credits_obtain_lab.append(b)
points_lab_obtained = []
for i in credits_obtain_lab:
	points_obtain = points_of_grades[i]
	points_lab_obtained.append(points_obtain)
lpc = 0
for a,b in zip(points_lab_obtained,lab_credits):
	lpc = a*b + lpc
print(" lab point * lab credits =  ", lpc)
summation_ = pc+lpc
f_count =  'f'
count_  = subject_grades.count(f_count)
count   =  lab_grades.count(f_count)
tc = total_credits-(count_*3+count*1.5)
sgpa = (summation_/tc)
print("your sgpa = " ,sgpa)
