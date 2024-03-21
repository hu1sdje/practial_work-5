number = int(input())
num = []
for i in range(1, 5):
    if i != 1:
        num.append(number % 10 ** i // (10 ** (i - 1)))
    else:
        num.append(number % 10 ** i)
if num == num[::-1]:
    print('настоящее')
else:
    print('кривое')