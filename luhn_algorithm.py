# Luhn's algorithm is used to verify if a card number is valid

card = input('Enter card number: ')


def validation(card):
    digits = len(card)
    if card.isnumeric():

        while digits != 16:
            print('Must have 16 digits')
            break
        num_list = [int(x) for x in str(card)]
        multiplied = []

        for num in range(len(num_list)):
            if num % 2 == 0:
                num_list[num] *= 2
            num_list[num] *= 1
            multiplied.append(num_list[num])

        last = []
        for i in multiplied:
            if i > 9:
                i = sum([int(digit) for digit in str(i)])
            last.append(i)

        if sum(last) % 10 != 0:
            print('Invalid card!')
        else:
            print('Valid card!')


validation(card)
