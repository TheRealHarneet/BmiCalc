# LB & CM or KG & CM
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

print("Welcome to my BMI Calculator!")
weight = int(input("What is your weight in kg?"))
height = float(input("What is your height in m?"))
bmi = round(weight / (height ** 2))
print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi} you are underweight")
elif bmi < 25:
    print("Your BMI is", bmi, "you have normal weight")
elif bmi < 30:
    print("Your BMI is", bmi, "you are slightly overweight")
elif bmi < 35:
    print("Your BMI is", bmi, "you are obese")
else:
    print("Your BMI is", bmi, "you are clinically obese")

