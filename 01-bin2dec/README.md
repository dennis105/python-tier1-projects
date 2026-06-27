# Bin2Dec

A simple Python console app that converts a binary number into a decimal number.

## Features

- Accepts binary numbers with up to 8 digits
- Validates that the input contains only `0` and `1`
- Converts valid binary numbers to decimal
- Shows an error message for invalid input

## Example

```txt
Enter a binary number, up to 8 digits, or q to quit: 1011
Decimal value: 11
Enter a binary number, up to 8 digits, or q to quit: 01101110
Decimal value: 110
Enter a binary number, up to 8 digits, or q to quit: 2
Invalid binary number. Use only 0 and 1, maximum 8 digits.
Enter a binary number, up to 8 digits, or q to quit: q
Quitting...
```

## How to run

```bash
python main.py
```

## What I learned

- How to validate user input
- How to use functions
- How binary to decimal conversion works
- How to use loops and conditionals in Python

## Next improvements

- Add automated tests
- Add a graphical or web interface