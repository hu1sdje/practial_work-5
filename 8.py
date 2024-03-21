knats = int(input())
ghalleons = knats // (29 * 17)
sikles = knats // 29
if knats // (29 * 17) != 0 and knats - (29 * 17) > 28 and knats - knats // (29 * 17) * (29 * 17) - knats // 29 * 29 > 0:
    print(f'{knats // (29 * 17)} галлеонов, {knats // 29} сиклей, '
          f'{knats - knats // (29 * 17) * (29 * 17) - knats // 29 * 29} кнатов')
elif knats // (29 * 17) == 0 and knats - (29 * 17) > 28 and knats - knats // (29 * 17) * (29 * 17) - knats // 29 * 29 > 0:
    print(f'{knats // 29} сиклей, {knats - knats // (29 * 17) * (29 * 17) - knats // 29 * 29} кнатов')
elif knats // (29 * 17) != 0 and knats - (29 * 17) < 29 and knats - knats // (29 * 17) * (29 * 17) > 0:
    print(f'{knats // (29 * 17)} галлеонов, {knats - knats // (29 * 17) * (29 * 17)} кнатов')
elif knats // (29 * 17) != 0 and knats - (29 * 17) > 28 and knats - knats // (29 * 17) * (29 * 17) - knats // 29 * 29 == 0:
    print(f'{knats // (29 * 17)} галлеонов, {knats // 29} сиклей')