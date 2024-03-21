day_1, day_2, day_3 = map(int, input().split())
if (day_1 == day_2) + (day_1 == day_3) + (day_3 == day_2) == 1:
    print(2)
elif (day_1 == day_2) + (day_1 == day_3) + (day_3 == day_2) == 0:
    print(1)
elif (day_1 == day_2) + (day_1 == day_3) == 2:
    print(3)