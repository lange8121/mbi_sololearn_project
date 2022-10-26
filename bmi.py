height = float(input('Enter height in meters: '))
weight = float(input('Enter weight in kg: '))

def BMI(height, weight):
    bmi = weight/(height**2)
    if (bmi < 18.5):
       return 'Underweight', bmi

    elif (bmi >= 18.5 and bmi < 25):
        return 'Normal', bmi

    elif (bmi >= 25 and bmi < 30):
        return 'Overweight', bmi

    elif (bmi >= 30):
        return 'Obesity', bmi

quote, bmi = BMI(height, weight) 
print('Your bmi is: {} and you are: {}'.format(bmi, quote))