import string
import sys


# dictionaries
ones = {
    0: 'naught',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens = {
    0: '',
    1: 'teen',
    2: 'twenty-',
    3: 'thirty-',
    4: 'forty-',
    5: 'fifty-',
    6: 'sixty-',
    7: 'seventy-',
    8: 'eighty-',
    9: 'ninety-'
}

powers = {
    0: '',             # 10^0
    1: 'thousand',     # 10^3
    2: 'million',      # 10^6
    3: 'billion',      # 10^9
    4: 'trillion',     # 10^12
    5: 'quadrillion',  # 10^15
    6: 'quintillion',  # 10^18
    7: 'sextillion',   # 10^21
    8: 'septillion',   # 10^24
}


def power_shift(val: int) -> tuple:
    """
    Shift amount right by 1000 to build the triplets

    :param val: source amount to shift
    :return: a tuple of right part and remainder
    """
    return (val % 1000, int(val / 1000))


def to_words(amt: int) -> string:
    """
    given the amount 0..999 return string in words

    :param amt: value to transcribe into words
    :return: a string, representing value in words
    """
    if amt > 99:
        return to_words(int(amt/100)) + ' hundred' + to_words(int(amt % 100))
    elif amt > 19:
        return ' ' + tens[int(amt/10)] + to_words(int(amt % 10))
    elif amt > 9:
        return ' ' + teens[amt]
    else:
        return ones[amt]


def convert_whole(whole_amt: int) -> string:
    """
    FIXME: Treating whole part different from decimal
    We want to identify the power triplets in the amount, e.g. 12_345_678
    would have 3 tripplets for millions, thousands and ones.
    We do it by shifting amount in 1000s, calling `power_shift()`

    :param whole_amt: amount to convert
    :return: string, representing value in words
    """
    triplets = []
    num_part, whole_amt = power_shift(whole_amt)
    while num_part > 0:
        triplets.append(num_part)
        num_part, whole_amt = power_shift(whole_amt)

    amount_in_words = ''
    for i in range(0, len(triplets)):
        if i == 0:
            and_and = 'and '
        else:
            and_and = ''

        amount_in_words = and_and + to_words(
            triplets[i]) + ' ' + powers[i] + ' ' + amount_in_words

    return amount_in_words


def main() -> int:
    ccy = '¤'  # universal currency symbol

    # quickly parse the command line
    if len(sys.argv) < 2:
        print("Must provide at least amount")
        sys.exit(0)
    elif len(sys.argv) == 2:
        # only amount given
        amount = float(sys.argv[1])
    else:
        # amount + currency name is expected
        ccy = sys.argv[1]
        amount = float(sys.argv[2])

    # first we split fractional and whole part
    whole = int(amount)
    fraction = int((amount * 100) % 100)

    print(convert_whole(whole) + ccy + ' and' + to_words(fraction))
    return 0


# called as script
if __name__ == '__main__':
    sys.exit(main())
