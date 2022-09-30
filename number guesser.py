from random import randint
import time

print('Добро пожаловать в числовую угадайку', '\n')
down_dig = input('Ведите нижнюю границу загадываемого числа: ')
while True:
    if down_dig.isdigit():
        down_dig = int(down_dig)
        break
    else:
        print('Это должно быть целое число!')
        down_dig = input('Ведите нижнюю границу загадываемого числа: ')
up_dig = input('Ведите верхнюю границу загадываемого числа: ')
while True:
    if up_dig.isdigit():
        up_dig = int(up_dig)
        if down_dig < up_dig:
            break
        else:
            print('Это должно быть целое число, больше первого!')
            up_dig = input('Ведите верхнюю границу загадываемого числа: ')
    else:
        print('Это должно быть целое число, больше первого!')
        up_dig = input('Ведите верхнюю границу загадываемого числа: ')
rand_dig = randint(down_dig, up_dig + 1)
print(f'Компьютер загадал число от {down_dig} до {up_dig}, попробуй угадать его!)', '\n')

def is_valid(inp):
    if inp.isdigit():
        return down_dig <= int(inp) <= up_dig
    else:
        return False
    
n = input(f'введите число от {down_dig} до {up_dig}: ')
count = 1

while True:
    if is_valid(n):
        if int(n) > rand_dig:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
            n = input()
        elif int(n) < rand_dig:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
            n = input()
        else:
            if 10 < count < 15 or 10 < count % 100 < 15:
                p = 'попыток'
            elif count == 1 or count % 10 == 1:
                p = 'попытку'
            elif 1 < count % 10 < 5 or 1 < count < 5:
                p = 'попытки'
            else:
                p = 'попыток'
                
            print(f'Вы угадали за {count} {p}, поздравляем!', '\n')
            answer = input('Желаете попробовать еще раз? (Y/N) ')
            while answer not in ('Y', 'N', 'n', 'y', ''):
                answer = input()
            if answer in ('Yy'):
                print('\n' * 3)
                down_dig = input('Ведите нижнюю границу загадываемого числа: ')
                while True:
                    if down_dig.isdigit():
                        down_dig = int(down_dig)
                        break
                    else:
                        print('Это должно быть целое число!')
                        down_dig = input('Ведите нижнюю границу загадываемого числа: ')
                up_dig = input('Ведите верхнюю границу загадываемого числа: ')
                while True:
                    if up_dig.isdigit():
                        up_dig = int(up_dig)
                        if down_dig < up_dig:
                            break
                        else:
                            print('Это должно быть целое число, больше первого!')
                            up_dig = input('Ведите верхнюю границу загадываемого числа: ')
                    else:
                        print('Это должно быть целое число, больше первого!')
                        up_dig = input('Ведите верхнюю границу загадываемого числа: ')
                rand_dig = randint(down_dig, up_dig)
                print(f'Компьютер загадал число от {down_dig} до {up_dig}, попробуй угадать его!', '\n')
                n = input(f'введите число от {down_dig} до {up_dig}: ')
                count = 1
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                time.sleep(3)
                break
    else:
        print(f'А может быть все-таки введем целое число от {down_dig} до {up_dig}?')
        n = input()
