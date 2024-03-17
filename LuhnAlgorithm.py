def verify_card_number(card_number):
    sum_off_odd_digits = 0
#indexing last four digits skipping by one
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
#       print(digit)
        sum_of_odd_digits += int(digit)
#   print(sum_of_odd_digits)
#   print(card_number_reversed)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
#       print(digit)
        number = int(digit) * 2
        if number >= 10:
# integer division to get the first digit and the modulus operator to get the second digit           
            number = number // 10 + number % 10
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
#   print(total)
    return total % 10 == 0
#           print(number)

def main():
    card_number = '4111-1111-4555-1142'
#for INVALID! changed the last digit to one 
    card_number = '4111-1111-4555-1141'
#String manipulation using maketrans to create a translation table
    card_translation = str.maketrans({'-':'',' ':''})
#calling translate method on the string
    translated_card_number = card_number.translate(card_translation)
    if verify_card_number(translated_card_number):
        print('VALID!)
    else:
        print('INVALID!')
#   print(translated_card_number)
    

    
main()
