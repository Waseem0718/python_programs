def int_to_roman(num):
    # Define the mappings of Roman numerals to their integer values
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
   
    roman_numeral = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_numeral += symbols[i]
            num -= val[i]
   
    return roman_numeral
# Example usage
print(int_to_roman(1987))  # Output: MCMLXXXVII 
