X=eval(input("Enter height in meters: "))
Y=int(input("Enter weight in kilograms: "))
BMI=Y/(X)**2
if BMI >=30:
    print("Obesity")
elif BMI >=25 and BMI <30:
    print("Overweight")
elif BMI >= 18.5 and BMI<25:
    print("Normal")
else:
    print("Underweight")
