number = int(input())
if number < 100:
    if 2 <= number % 10 <= 4 and not 12 <= number % 100 <= 14:
        print(f'{number} попугая')
    elif number % 10 == 1 and not number % 100 == 11:
        print(f'{number} попугай')
    else:
        print(f'{number} попугаев')