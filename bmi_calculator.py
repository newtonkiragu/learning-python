#! /usr/bin/python
weight = int(input('Please key in your weight: '))
height = float(input('Please key in your height in meters: '))
bmi = weight/(height*height)
if bmi <= 18.5:
    print('Your BMI is', bmi,'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
    print('Your BMI is', bmi,'which means you are normal.')

elif bmi > 25 and bmi < 30:
    print('your BMI is', bmi,'overweight.')

elif bmi > 30:
    print('Your BMI is', bmi,'which means you are obese.')
