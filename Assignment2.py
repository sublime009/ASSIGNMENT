a = float(input ('Enter the value of the first side of the traingle: '))
b = float(input ('Enter the value of the second side of the traingle: '))
c = float(input ('Enter the value of the third side of the traingle: '))

result = a, b, c

if a + b <= c or a + c <= b or b + c <= a:
    print(f'Result: {result}')
    print('Error! invalid Triangle')

else:
    if a == b == c:
        print(f'Result: {result}')
        print('Equilateral Triangle: (Sum of all sides are the same).')

    elif a == b or a == c or b == c:
        print(f'Result: {result}')
        print('Isosceles Triangle: (Sum of two sides are equal).')

    else:
        print(f'Result: {result}')
        print('Scalene Triangle: (Sum of two sides greater than one).')