#Pedro Gallino
#9/12/17
# gradeCalculator.py - tells you your letter grade

grade = int(input('Enter your grade: '))
if grade>=93:
    print('You earned a A')
elif grade>=80:
    print('You earned a B')
elif grade>=70:
    print('You earned a C')
elif grade>=60:
    print('You earned a D')
else:
    print('You earned a NC')
