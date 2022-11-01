

def take_rational_part(user_number):
    # Функция возвращает рациональную часть из комплексного
    rational_part = []
    for k in range(0, len(user_number)):
        if user_number[k] != ' ':
            rational_part.append(user_number[k])
        else:
            break
    rational_part = float(''.join(rational_part))
    return rational_part

def take_imaginary_part(user_number):
    # Функция возвращает мнимую часть
    imaginary_part = []
    for i in range(0, len(user_number)):
        if user_number[i] == 'i':
            while user_number[i] != ' ':
                imaginary_part.insert(0,user_number[i - 1])
                i-= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part

def take_symbol(user_number):
    # Функция возвращает - или + между рациональной и мнимой частями
    symbol = []
    for l in range(0, len(user_number)):
        if user_number[l] == '-' and l !=0 or user_number[l] == '+' and l != 0:
            symbol.append(user_number[l])
    symbol = ''.join(symbol)
    return symbol

def addition(r1, s1, i1, r2, s2, i2):
    # Функция сложения двух комплексных чисел
    result = []
    result.append(r1+r2)
    # print('1', result)
    if s1 == '+' and s2 == '+':
        result.append(i1+i2)
        # print('2', result)
    elif s1 == '+' and s2 == '-':
        result.append(i1-i2)
        # print('3', result)
    elif s1 == '-' and s2 == '+':
        result.append(i2-i1)
        # print('4', result)
    else:
        result.append(-(i1+i2))
        # print('5', result)
    return result
    # print (result)

def deduction(r1, s1, i1, r2, s2, i2):
    # Функция вычитания второго комплексного числа из первого
    result = []
    result.append(r1-r2)
    if s1 == '+' and s2 == '+':
        result.append(i1-i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1+i2)
    elif s1 == '-' and s2 == '+':
        result.append(-i2-i1)
    else:
        result.append(i2-i1)
    return result

def multiply(r1, s1, i1, r2, s2, i2):
    # Функция умножения двух комплексных чисел
    result = []
    result.append(r1*r2)
    # print('1', result)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        result.append(-i1*i2)
        # print('2', result)
    else:
        result.append(i1*i2)
        # print('3',result)
    if s1 == "+":
        result.append(r2*i1)
        # print('4',result)
    else:
        result.append(-r2*i1)
        # print('5',result)
    if s2 == "+":
        result.append(r1*i2)
        # print('6',result)
    else:
        result.append(-r1*i2)
        # print('7',result)
    result[0] = result[0] + result[1]
    # print('8',result)
    result[1] = result[2] + result[3]
    # print('9',result)
    result.pop(3)
    # print('10',result)
    result.pop(2)
    # print('11',result)
    return result    
    
def division(r1, s1, i1, r2, s2, i2):
    # Функция деления двух комплексных чисел
    numerator = []
    denominator = []
    result = []
    numerator.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        numerator.append(i1*i2)
    else:
        numerator.append(-i1*i2)
    if s1 == "-":
        numerator.append(-r2*i1)
    else:
        numerator.append(r2*i1)
    if s2 == "+":
        numerator.append(-r1*i2)
    else:
        numerator.append(r1*i2)
    numerator[0] = numerator[0] + numerator[1]
    numerator[1] = numerator[2] + numerator[3]
    numerator.pop(3)
    numerator.pop(2)
    denominator.append(r2**2+i2**2)
    result.append(numerator[0]/denominator[0])
    result.append(numerator[1]/denominator[0])
    # print(result[1])
    return result

def record_in_file(result):
    # Добавлены результаты в файл
    ot=[]
    with open('results.json', 'a') as data:
        print('1', result[1])
        if int(result[1]) != 0:
            for i in range(0, 2):

                if result[i] > 0 and i == 1:
                    print('2', '+ ', end='')
                    data.write('+ ')
                elif result[i] < 0 and i == 1:
                    result[i] = -result[i]
                    result[i] = str(result[i])
                    print('3','- ', end='')
                    data.write('- ')
                    print('4',result[i], end='')
                    data.write(result[i])
                elif i != 1:
                    print('5', ' ', end='')
                    data.write(' ')
                elif result[i] ==0:
                    print('6','', end='')
                    data.write('')
                else:
                    result[i] = str(result[i])
                    print(f'7 {result[i]}', end='')
                    data.write(result[i])

            print(f'8 {result[1]}i')
            data.write(f'{result[1]}i\n')
        else:
            result[0] = str(result[0])
            print(f'9 {result[0]}\n')
            data.write(f'{result[0]}\n')
    print('10',ot)
    data.close()

