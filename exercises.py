# Returns a list of odd products from a list of numbers, using check_odd() callback to filter out any even numbers
def check_odd(number):
  if number % 2 != 0:
    return True
  return False

def find_odd_products(integers):
  odd_integers = list(set(filter(check_odd, integers)))
  odd_products = []
  while len(odd_integers) > 1:
    for ind in range(1, len(odd_integers)):
      odd_products.append([odd_integers[0], odd_integers[ind]])
    odd_integers.pop(0)
  return odd_products

# seq1 = [1,2,3,4,5,6,7,7,8,6]
# seq2 = (9,10,11,12,12,13,14,15,16,17)
# seq3 = {18,19,20,21,22,23,25,26,29}

# Prints all items in a for loop in reverse order as their negative values
def print_for_loop(start = 10, end = 1, step = -1):
    for item in range(start, end-1, step):
        print(-item)
        
# Returns the middle three character in a string
def middle_chars(a_string):
    length = len(a_string)
    start = int(length/2 - 1.5)
    end = start + 3
    result = ""
    for num in range(start, end):
        result += a_string[num]
    return result

import string

# Remove all non-alphanumeric characters in a string (spaces allowed). Uses callback remove_bad() to filter out symbols.
def remove_bad(char):
    bad = string.punctuation
    for symbol in bad:
        if char == symbol:
            return False
    return True
    
def remove_symbols(my_string):
    return "".join(list(filter(remove_bad, my_string)))

# Checks whether a given value is in a given dictionary
def check_dict_values(dictionary, value):
    if value in list(dictionary.values()):
        return True
    return False

# my_dictionary = {'a': 100, 'b': 200, 'c': 300}
# my_value = 200

# Checks whether a number is a "Curzon" number. A Curzon number is one where 2 to the power of that number plus 1 is divisible by two times that number plus one.
def is_curzon(numbah):
    print(numbah)
    powah = 2**numbah + 1
    multiply = 2*numbah + 1
    if powah % multiply == 0:
        return True
    return False

# Returns how much (or little) time is saved when you drive a given distance at a given speed above that of the given speed limit
def time_saved(speed_limit, your_speed, distance, time_unit="hours"):
    time_speeding = distance / your_speed
    time_at_limit = distance / speed_limit
    return f"{time_at_limit - time_speeding} {time_unit}"

# Takes a string and returns it in Morse code 
char_to_dots = {
  'A': '.-', 
  'B': '-...', 
  'C': '-.-.', 
  'D': '-..', 
  'E': '.', 
  'F': '..-.',
  'G': '--.', 
  'H': '....', 
  'I': '..', 
  'J': '.---', 
  'K': '-.-', 
  'L': '.-..',
  'M': '--', 
  'N': '-.', 
  'O': '---',
  'P': '.--.', 
  'Q': '--.-', 
  'R': '.-.',
  'S': '...', 
  'T': '-', 
  'U': '..-', 
  'V': '...-', 
  'W': '.--', 
  'X': '-..-',
  'Y': '-.--', 
  'Z': '--..', 
  ' ': ' ', 
  '0': '-----',
  '1': '.----', 
  '2': '..---', 
  '3': '...--', 
  '4': '....-', 
  '5': '.....',
  '6': '-....', 
  '7': '--...', 
  '8': '---..', 
  '9': '----.',
  '&': '.-...', 
  "'": '.----.', 
  '@': '.--.-.', 
  ')': '-.--.-', 
  '(': '-.--.',
  ':': '---...', 
  ',': '--..--', 
  '=': '-...-', 
  '!': '-.-.--', 
  '.': '.-.-.-',
  '-': '-....-', 
  '+': '.-.-.', 
  '"': '.-..-.', 
  '?': '..--..', 
  '/': '-..-.'
}

def encode_morse(message_string):
    morse = ""
    for char in message_string:
        morse += (char_to_dots[char.capitalize()] + " ")
    return morse

import datetime

# Checks whether "Friday the 13th" occurs in a given month and year
def has_friday_13(month, year):
    thirteenth = datetime.date(year, month, 13)
    if thirteenth.weekday() == 4:
        return True
    return False

# Encodes a string by reversing it, replacing all vowels with a certain number, then adding "aca" at the end.
def karaca(stringer):
    if stringer.lower() != stringer:
        return "All letters MUST be lowercase, silly."
    encrypting = stringer[::-1]
    karaca_dict = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    for key in karaca_dict:
        encrypting = encrypting.replace(key, karaca_dict[key])
    encrypting += "aca"
    return encrypting
        
# print(karaca("courage the cowardly dog"))

import math

# Returns the number of given integer powers (n) between one number and another (a and b), inclusive
def power_ranger(n,a,b):
    bottom = math.ceil( a**(1/n) )
    top = math.floor( b**(1/n) )
    in_range = list(range(bottom, top+1))
    return len(in_range)

# Take any number of lists of integers, combines them, and checks if all integers between the minimum and maximum of the combined list is present (redundencies not allowed)
def consecutive_combo(*args):
    combo = []
    for next_list in args:
        combo += next_list
        
    range_to_meet = range(min(combo), max(combo)+1)
    for num in range_to_meet:
        if num not in combo:
            return False
        combo.pop(combo.index(num))
        
    if len(combo) == 0:
        return True
    return False

# takes an list and returns the majority voite from that list, or the item whose count is greater than half the list's length
def majority_vote(lst):
    for item in lst:
        if lst.count(item) > len(lst) / 2:
            return item

# Checks whether given number is prime
def is_prime(number):
    if number <= 1:
        return False
    try:
        range(2, number)
    except:
        return False
    for num in range(2 , number):
        if number % num == 0:
            return False
    return True

# Returns the sum of all prime numbers in the given list
def sum_primes(lst):
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    return sum(primes)

# Returns the factorial of the number (number!, or 1 * 2 * 3 *...* (number-1) * number)
def factorial(number):
    if number == 0 or number == 1:
        return 1
    factors = range(2, number+1)
    if number > 1:
        result = 1
        for number in factors:
            result = result*number
        return result

# "Kempner" function; returns the smallest integer greater than 0 whose factorial is divisible by the input. Returns 0 if input is not an integer or is <= 0.
def kempner(number):
    if type(number) != int or number <= 0:
        return 0
    kemp = 1
    while factorial(kemp) % number != 0:
        kemp += 1
    return kemp

# Checks a string whether or not all instances of the character "first" come before all instances of the character "second"
def first_before_second(string, first, second):
    second_index = string.find(second)
    if second_index == -1:
        return False
    string_part_1 = string[ : second_index]
    string_part_2 = string[second_index :]
    if string_part_1.find(first) == -1:
        return False
    
    for char in string_part_2:
        if char == first:
            return False
    
    return True

import numpy as np
    
# Builds then returns a dictionary of the count of all datatypes of any number of arguments
def count_datatypes(*args):
    datatype_count = {}
    
    for item in args:
        if type(item) in datatype_count.keys():
            datatype_count[type(item)] += 1
        else:
            datatype_count[type(item)] = 1
            
    return datatype_count

# print(count_datatypes(2, 3, 4.5, 6, "asds", [1,2,3], np.array([1,2,3]), {"a": 2}, (123,24)))

# Checks is a number is "Disarium". A number is Disarium if the sum of the digits raised to their respective postions equals the number itself.
# For example, 135 is Disarium because 1^1 + 2^2 + 5^3 = 135.
def is_disarium(num):
    total = 0
    power = 1
    for n in str(num):
        total += int(n)**power
        power += 1
    return total == num
        
# print(is_disarium(518))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Uses a binary search algorithm to check if a number is within a list of sorted prime numbers
def binary_search_is_prime(primes, num):

    while len(primes) > 1:
        if num < primes[int(len(primes) / 2)]:
            primes = primes[0: int(len(primes) / 2)]
        else:
            primes = primes[int(len(primes) / 2):]
        
    if len(primes) == 1 and num in primes:
        return "yes"

    return "no"

# print(binary_search_is_prime(primes, 11))

def rearranged_difference(num):
    numArray = [digit for digit in str(num)]
    minimum, maximum = numArray, numArray[:]
    minimum.sort(), maximum.sort()
    maximum.reverse()
    minimum = int(''.join(minimum))
    maximum = int(''.join(maximum))
    return maximum - minimum
    
print(rearranged_difference(2301))
    