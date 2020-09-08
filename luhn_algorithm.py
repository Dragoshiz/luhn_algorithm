card_num = input('Credit card number: ')


def check_card_validation(card):
    num_digits = len(card)

    if card.isdecimal():
        while num_digits != 16:
            raise ValueError
        last_num = int(card[-1])
        rest = card[:-1]
        reverse_rest = rest[::-1]
        reverse_rest = list(map(int, reverse_rest))
        for i in range(len(reverse_rest)):
            if i % 2 == 0:
                reverse_rest[i] *= 2
        for i in range(len(reverse_rest)):
            if reverse_rest[i] > 9:
                reverse_rest[i] -= 9
        result = sum(reverse_rest) % 10
        if result == last_num:
            print("Valid Credit Card!")
        else:
            print("Invalid Credit Card")
    else:
        print("Check if your Credit Card number is correct")


check_card_validation(card_num)
