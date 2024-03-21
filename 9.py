tower_1, tower_2, tower_3 = map(int, input().split())
if tower_1 < tower_2 < tower_3:
    print(tower_3, tower_2, tower_1)
elif tower_3 < tower_2 < tower_1:
    print(tower_1, tower_2, tower_3)
elif tower_1 < tower_3 < tower_2:
    print(tower_2, tower_3, tower_1)
elif tower_3 < tower_1 < tower_2:
    print(tower_2, tower_1, tower_3)
elif tower_2 < tower_3 < tower_1:
    print(tower_1, tower_3, tower_2)
elif tower_2 < tower_1 < tower_3:
    print(tower_3, tower_1, tower_2)