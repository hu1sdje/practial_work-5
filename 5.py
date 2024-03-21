mass, height = map(int, input().split())
imt = mass / ((height / 100) ** 2)
print(imt)
if imt < 16:
    print('выраженный дефицит массы тела')
elif imt < 18.5:
    print('недостаточная масса тела')
elif imt < 25:
    print('норма')
elif imt < 30:
    print('избыточная масса тела')
elif imt < 35:
    print('ожирение первой степени')
elif imt < 40:
    print('ожирение второй степени')
elif imt > 40:
    print('ожирение третьей степени')