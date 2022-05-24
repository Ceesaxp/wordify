# Wordify

This is a quick hack to convert number into a worded string. **Very** quick hack for now, assumes that input amount is a currency amount with only 2 decimals.

## Usage

`wordify.py [currency name] [amount]`

- [currency name] - optionally specify the nme of currency
- [amount] - must be provided, expected to have only 2 fractional digits

## Example

```
$ wordify.py 'UK pound' 748574.65

seven hundred forty-eight thousand and five hundred seventy-four  UK pound and sixty-five
```