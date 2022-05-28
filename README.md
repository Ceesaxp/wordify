# Wordify

This is a quick hack to convert number into a worded string. **Very** quick hack for now, assumes that input amount is a currency amount with only 2 decimals.

## Usage

`wordify.py [currency name] [amount] [language]`

- [currency name] - optionally specify the nme of currency
- [amount] - must be provided, expected to have only 2 fractional digits
- [language] - optional language specification (currenlty only 'en' and 'ru' are supported)

## Example

```
$ wordify.py 'pounds' 748574.65

seven hundred forty-eight thousand and five hundred seventy-four  pound and sixty-five
```
or

```
$ wordify.py 'руб.' 12088.99 ru

двенадцать тысяча  восемьдесят восемь  руб. and девяносто девять
```
