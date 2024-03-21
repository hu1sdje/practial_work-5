pin = input()
if len(pin) == 4:
    if pin[0] != pin[1] and pin[0] != pin[2] and pin[0] != pin[3] and pin[1] != pin[2] and pin[1] != pin[3] and pin[2] \
            != pin[3]:
        if not 1900 < int(pin) < 2050:
            print('OK')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')
