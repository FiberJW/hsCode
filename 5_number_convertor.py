# Converts number to other base representations

def decision():
    response = input("\nDo you want to convert another number? " \
                        "Type [y]es or [n]o:\n\t=>").lower()

    if response == 'y' or response == 'yes':
        master()
    elif response == 'n' or response == 'no':
        raise SystemExit
    else:
        print('\nInvalid input.\n')
        decision()


def bin_convert():
    val_bin = 0, 1
    num_dig_left = 0
    num_invalid = 0
    num = input('\nInput binary number:\n\t=>')
    try:
        int(num)
    except ValueError:
        print('\n\tInvalid number.\n')
        bin_convert()
    for i in num:
        if int(i) not in val_bin:
            print('\nInvalid digit: {}\n'.format(i))
            num_dig_left += 1
            num_invalid += 1
            if num_dig_left == len(num):
                if num_invalid > 0:
                    bin_convert()
        else:
            num_dig_left += 1
            if num_dig_left == len(num):
                if num_invalid > 0:
                    bin_convert()
                else:
                    break
    new_bin = '0b' + num
    new_int = int(new_bin, 2)
    print('\nBase 8: {0:o}'.format(new_int))
    print('\nBase 10: {0:d}'.format(new_int))
    print('\nBase 16: {0:x}'.format(new_int))
    decision()


def oct_convert():
    val_oct = 0, 1, 2, 3, 4, 5, 6, 7
    num_dig_left = 0
    num_invalid = 0
    num = input('\nInput octal number:\n\t=>')
    try:
        int_num = int(num)
    except ValueError:
        print('\n\tInvalid number.\n')
        oct_convert()
    for i in num:
        if int(i) not in val_oct:
            print('\nInvalid digit: {}\n'.format(i))
            num_dig_left += 1
            num_invalid += 1
            if num_dig_left == len(num):
                if num_invalid > 0:
                    oct_convert()
        else:
            num_dig_left += 1
            if num_dig_left == len(num):
                if num_invalid > 0:
                    oct_convert()
                else:
                    break
    new_int = int(num, 8)
    print('\nBase 2: {0:b}'.format(new_int))
    print('\nBase 10: {0:d}'.format(new_int))
    print('\nBase 16: {0:x}'.format(new_int))
    decision()


def dec_convert():
    val_dec = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    num_dig_left = 0
    num_invalid = 0
    num = input('\nInput decimal number:\n\t=>')
    try:
        int_num = int(num)
    except ValueError:
        print('\n\tInvalid number.\n')
        dec_convert()
    for i in num:
        if int(i) not in val_dec:
            print('\nInvalid digit: {}\n'.format(i))
            num_dig_left += 1
            num_invalid += 1
            if num_dig_left == len(num):
                if num_invalid > 0:
                    dec_convert()
        else:
            num_dig_left += 1
            if num_dig_left == len(num):
                if num_invalid > 0:
                    dec_convert()
                else:
                    break
    print('\nBase 2: {0:b}'.format(int_num))
    print('\nBase 8: {0:o}'.format(int_num))
    print('\nBase 16: {0:x}'.format(int_num))
    decision()


def master():
    base = input('\nWhat base do you want to convert from \
(2, 8, or 10):\n\t=>')
    if base == '2':
        bin_convert()
    elif base == '8':
        oct_convert()
    elif base == '10':
        dec_convert()
    else:
        print('\nInvalid base.\n')
        master()

master()
