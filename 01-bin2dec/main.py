def is_valid_binary(binary):
    if len(binary) == 0:
        return False

    if len(binary) > 8:
        return False

    for digit in binary:
        if digit != '0' and digit != '1':
            return False

    return True


def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return decimal


while True:
    binary_number = input('Enter a binary number, up to 8 digits, or q to quit: ')

    if binary_number.lower() == 'q':
        print("Quitting...")
        break

    if is_valid_binary(binary_number):
        decimal_number = binary_to_decimal(binary_number)
        print(f"Decimal value: {decimal_number}")
    else:
        print("Invalid binary number. Use only 0 and 1, maximum 8 digits.")