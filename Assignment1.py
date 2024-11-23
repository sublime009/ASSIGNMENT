user_name = input('Enter your name:')
weight = float(input('Enter your weight (in kg): '))
height = float(input('Enter your height (in m): '))

if weight <= 0:
    print(f'{user_name} error')

if height <= 0:
    print(f'{user_name} error')

bmi = weight/height**2

if bmi < 18.5:
    print(f'{bmi:.2f} Underweight ')

elif bmi >= 18.5 and bmi < 25:
    print(f'{bmi:.2f} Normal')    

elif bmi < 25 <= bmi < 30:
    print(f'{bmi:.2f} Overweight')    

elif bmi >= 30:
    print(f'{bmi:.2f} Obesity')

print(f'Your total body mass index {bmi + weight:.2f}')
