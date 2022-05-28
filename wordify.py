#!/usr/bin/env python3
import string
import sys


def hundred(lang: string = 'en') -> string:
    """
    Shorthand for 'hundred' word

    :return: a constant -- word for 'hundred'
    """
    lang_hundred = {
        'en': ' hundred',
        'ru': '!сто'
    }
    return lang_hundred[lang]


def powers(pw: int, lang: string = 'en') -> string:
    """
    Provide names for power tripplets.

    :param lang: language to use
    :param pw: sequence order for the tripplet
    :return: power triplet name
    """
    lang_powers = {
        'en':
            {
                0: '',  # 10^0
                1: 'thousand',  # 10^3
                2: 'million',  # 10^6
                3: 'billion',  # 10^9
                4: 'trillion',  # 10^12
                5: 'quadrillion',  # 10^15
                6: 'quintillion',  # 10^18
                7: 'sextillion',  # 10^21
                8: 'septillion',  # 10^24
            },
        'ru':
            {
                0: '',  # 10^0
                1: 'тысяча',  # 10^3
                2: 'миллион',  # 10^6
                3: 'миллиард',  # 10^9
                4: 'триллион',  # 10^12
                5: 'квадриллион',  # 10^15
                6: 'квинтиллион',  # 10^18
                7: 'секстиллион',  # 10^21
                8: 'септиллион',  # 10^24
            }
    }

    if 0 <= pw < 9:
        return lang_powers[lang][pw]
    else:
        print(f"Value {pw} is out of range")
        sys.exit(0)


def ones(amt: int, lang: string = 'en') -> string:
    """
    Given amount `amt` return a word associated with the value.

    :param lang:
    :param amt:
    :return: numeral in words
    """
    lang_ones = {
        'en':
            {0: 'naught',
             1: 'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine', },
        'ru':
            {0: 'ноль',
             1: 'один',
             2: 'два',
             3: 'три',
             4: 'четыре',
             5: 'пять',
             6: 'шесть',
             7: 'семь',
             8: 'восемь',
             9: 'девять', },
    }

    if 0 <= amt <= 9:
        return lang_ones[lang][amt]
    else:
        print(f"Value {amt} is out of range")
        sys.exit(0)


def tens(amt: int, lang: string = 'en') -> string:
    """
    Given amount `amt` return the name for 'tens'.

    :param lang:
    :param amt: index of the 'ten'
    :return: string, representing the 'tens' name
    """
    lang_tens = {
        'en': {
            0: '',
            1: '*teen',
            2: 'twenty-',
            3: 'thirty-',
            4: 'forty-',
            5: 'fifty-',
            6: 'sixty-',
            7: 'seventy-',
            8: 'eighty-',
            9: 'ninety-'
        },
        'ru': {
            0: '',
            1: '*надцать',
            2: 'двадцать ',
            3: 'тридцать ',
            4: 'сорок ',
            5: 'пятьдесят ',
            6: 'шестьдесят ',
            7: 'семьдесят ',
            8: 'восемьдесят ',
            9: 'девяносто '
        },
    }

    if 0 < amt <= 9:
        return lang_tens[lang][amt]
    else:
        print(f"Value {amt} is out of range")
        sys.exit(0)


def teens(amt: int, lang: string = 'en') -> string:
    """
    Given amount `amt` extract the 10-19 (teen) name.

    :param lang:
    :param amt: amount in the range of 10-19
    :return: 'teens' name in words
    """
    lang_teens = {
        'en':
            {10: 'ten',
             11: 'eleven',
             12: 'twelve',
             13: 'thirteen',
             14: 'fourteen',
             15: 'fifteen',
             16: 'sixteen',
             17: 'seventeen',
             18: 'eighteen',
             19: 'nineteen', },
        'ru':
            {10: 'десять',
             11: 'одинадцать',
             12: 'двенадцать',
             13: 'тринадцать',
             14: 'четырнадцать',
             15: 'пятнадцать',
             16: 'шестнадцать',
             17: 'семнадцать',
             18: 'восемнадцать',
             19: 'девятнадцать', },
    }

    if 10 <= amt <= 19:
        return lang_teens[lang][amt]
    else:
        print(f"Value {amt} is out of range")
        sys.exit(0)


def power_shift(val: int, pw: int = 3) -> tuple:
    """
    Shift `val` right by 10^pw to build the numeric sets ("powers").
    In some countries these are not, necessarily, 10^3, hence may need
    to adjust for universality.

    :param val: source amount to shift
    :param pw: power of 10 to be used for shifting
    :return: a tuple of right part and remainder
    """
    return val % (10 ** pw), int(val / (10 ** pw))


def to_words(amt: int, lang: string = 'en') -> string:
    """
    Given the `amt` 0..999 return string in words.

    The function assumes that we only work within a 0..999 range, may
    need to adjust for a few countries where ranges differ, but none (?)
    are going above the 999 bound.

    :param amt: value to transcribe into words
    :param lang: language to use for translation
    :return: a string, representing value in words in `lang` language
    """
    if amt > 99:
        return to_words(int(amt / 100), lang) + hundred(lang) + to_words(int(amt % 100), lang)
    elif amt > 19:
        return ' ' + tens(int(amt / 10), lang) + to_words(int(amt % 10), lang)
    elif amt > 9:
        return ' ' + teens(amt, lang)
    else:
        return ones(amt, lang)


def and_func(i, lang: string = 'en'):
    """
    Silly 'and' beautifier for some languages.

    :param i: index
    :param lang: language
    :return: blank or 'and'
    """
    if lang == 'en' and i == 0:
        return 'and '
    else:
        return ''


def convert_whole(whole_amt: int, lang: string = 'en') -> string:
    """
    FIXME: Should we keep treating whole part different from decimal?

    We want to identify the power triplets in the amount, e.g. 12_345_678
    would have 3 tripplets for millions, thousands and ones.
    We do it by shifting amount in 1000s, calling `power_shift()`

    :param lang:
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
        amount_in_words = and_func(i, lang) + to_words(
            triplets[i], lang) + ' ' + powers(i, lang) + ' ' + amount_in_words

    return amount_in_words


def join_parts(lang: string = 'en') -> string:
    """
    Proper conjunction to use to join whole and fractional parts for the `lang` language

    :param lang:
    :return:
    """
    if lang == 'en':
        return ' and'
    elif lang == 'ru':
        return ' и'
    else:
        return ''


def main() -> int:
    ccy = '¤'  # universal currency symbol
    lang = 'en'

    # quick & dirty parsing of the command line params
    if len(sys.argv) < 2:
        print("Must provide at least an amount")
        sys.exit(0)
    elif len(sys.argv) == 2:
        # only amount given
        amount = float(sys.argv[1])
    elif len(sys.argv) == 3:
        # amount + currency name are expected
        ccy = sys.argv[1]
        amount = float(sys.argv[2])
    elif len(sys.argv) == 4:
        # amount + currency name + language are expected
        ccy = sys.argv[1]
        amount = float(sys.argv[2])
        lang = sys.argv[3]
    else:
        print("Not sure what you want from me :(")
        return 0

    # check that we support the language, fallback to English
    if lang not in ['ru', 'en']:
        print(f'I do not know how to speak {lang}, falling back to English.')
        lang = 'en'

    # first we split fractional and whole part
    whole = int(amount)
    fraction = int((amount * 100) % 100)

    print(convert_whole(whole, lang) + ccy + join_parts(lang) + to_words(fraction, lang))
    return 0


# called as script
if __name__ == '__main__':
    sys.exit(main())
