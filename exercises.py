import math
import string
import datetime
import functools

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
	morse_trans = message_string.maketrans(char_to_dots) 
	morse = message_string.translate(morse_trans)
	return morse

# Checks whether "Friday the 13th" occurs in a given month and year
def has_friday_13(month, year):
    thirteenth = datetime.date(year, month, 13)
    if thirteenth.weekday() == 4:
        return True
    return False

# Encodes a string by reversing it, replacing all vowels with a certain number, then adding "aca" at the end.
def karaca(string):
    encrypting = string.lower()[::-1]
    karaca_dict = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    table = string.maketrans(karaca_dict)
    encrypting = encrypting.translate(table)
    return encrypting + 'aca'

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
    
    return True

# takes an list and returns the majority voite from that list, or the item whose count is greater than half the list's length
def majority_vote(lst):
    for item in lst:
        if lst.count(item) > len(lst) / 2:
            return item

# Checks whether given number is prime
def is_prime(number):
    if number <= 3:
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

# Returns the next prime number after the given number
def next_prime(num):
    current = math.ceil(num)
    if current == num:
        current += 1
    while True:
        if is_prime(current):
            return current
        current += 1

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
    
def factorial_recursion(number):
    return 1 if number < 2 else number*factorial_recursion(number-1)

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
    
# print(rearranged_difference(2301))

# Checks an exam score whether it meets the requirement to pass an exam. Both arguments are strings.
def grade_precentage(score, required):
    digits = [digit for digit in string.digits]
    
    def is_digit(char):
        return char in digits
    
    score = int(''.join(list(filter(is_digit, score))))
    required = int(''.join(list(filter(is_digit, required))))
    
    if score >= required:
        pass_fail = 'PASSED'
    else:
        pass_fail = 'FAILED'
        
    return f'You {pass_fail} the exam'
    
# print(grade_precentage("80%", "75%"))

# "skyline" is a 2D list with 1's being building space and 0's being empty space. Returns the height of the tallest skyscraper(s).
def tallest_skyscraper(skyline):
    heights = []
    for building in range(len(skyline[0])):
        height = 0
        for space in range(len(skyline)):
            if skyline[space][building] == 1:
                height += 1
        heights.append(height)
    return max(heights)

# print(tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]))
# Returns "3" as the building / column second-furthest left has 3 1's, making it the tallest.

# "Adds" two numbers incorrectly, instead using the method shown on https://en.meming.world/wiki/Girl_at_Whiteboard_Adding
def meme_sum(num1, num2):
    total = []
    lst1 = list(str(num1))
    lst2 = list(str(num2))
    
    while len(lst1) != len(lst2):
        lst2.insert(0,0) if len(lst1) > len(lst2) else lst1.insert(0,0)
            
    for digit in range(len(lst1)):
        total.append( str(int(lst1[digit]) + int(lst2[digit])) )
        
    return int(''.join(total))

# Takes a variable number of integers, each representing the number of items in a set, and returns the number of combinations that can be made by taking one from each item.

def combinations(*args):
    nonzero_args = filter(lambda num: num != 0, list(args))
    return functools.reduce(lambda total, acc : total*acc, nonzero_args)

# Takes a list of lists and combines them into a single list
def one_list(lst):
	result = []
	for item in lst:
		result += item
	return result

# Takes a 2D matrix (written as a list of lists, each inner list being a row) and returns its TRANSPOSE (flipped over by its diagonal)
def make_transpose(matrix):
    result = []
    for column in range(len(matrix[0])):
        result.append([])
        for row in range(len(matrix)):
            result[column].append(matrix[row][column])
    return result

# Takes a list OR a string and returns the list or string containing only the elements whose position is a multiple of 'pos'
def chars_at_position(lst_str, pos):
    valid_indices = list(range(pos, len(lst_str) + 1, pos))
    result = [lst_str[num-1] for num in valid_indices]
    if type(lst_str) == str:
        return ''.join(result)
    return result

# Takes a list and returns the value whose sum of the values on one side equals that of the other, or its "fulcrum." Example: the fulcrum of the list [5,2,1,4] is 2, because 5 (the sum of values on its left) = 1 + 4 (the sum on its right). 
def find_fulcrum(lst):
    for i in range(1, len(lst) - 1):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return lst[i]
    return -1

# Returns a list containing a "square" box with each side having 'side' (an integer) * the string '#'.
def make_box(side):
    result = []
    result.append('#'*side)
    for num in range(1, side - 1):
        result.append('#' + ' ' * (side-2) + '#')
    result.append('#'*side)
    return result

# Searches for a word in a string and returns the entire sentence containing the word (not case-sensitive)
def sentence_searcher(txt, word):
    result = ''
    for char in txt:
        result += char
        if char == '.':
            if word.lower() in result.lower():
                return result.strip()
            result = ''
    return result

# In a list, the interval is the difference between the maximum and the minimum. Returns ":)" if the interval is in the list, ":(" if not, and "/" if the argument is not a list.
def face_interval(lst):
    if type(lst) != list:
        return ':/'
    interval = max(lst) - min(lst)
    return ':)' if interval in lst else ':('

# Takes a string and returns whether all words have no duplicate letters
def no_duplicate_letters(txt):
    txt_lst = txt.lower().split()
    
    def has_duplicate(next_string):
        for letter in next_string:
            if next_string.count(letter) > 1:
                return True
        return False
    
    return len(list(filter(has_duplicate, txt_lst))) == 0

# More efficient version of no_duplicate_letters()
def no_duplicate_letters2(txt):
    txt_lst = txt.lower().split()
    
    for next_string in txt_lst:
        for letter in next_string:
            if next_string.count(letter) > 1:
                return False
            
    return True

# Takes the three poins of a triangle in Cartesian coordinates and returns the perimeter
def triangle_perimeter(p1, p2 ,p3):
    side1 = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    side2 = math.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)
    side3 = math.sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2)
    return round(side1 + side2 + side3, 2)

# Takes digit "num" returns the sum of the combined digits of the first and last digit of num, the second and second-last digit of num, until the digits reach the center of num.
# Example: closing_in_sum(5645) => 119, becuase 55 + 64 = 119.
# If the length of num is odd, the center digit is added alone. Ex: closing_in_sum(343) => 33 + 4 = 37.
def closing_in_sum(num):
    digits_num = [digit for digit in str(num)]
    total = 0
    if len(digits_num) % 2 != 0:
        middle = int((len(digits_num) / 2) - 0.5)
        total += int(digits_num[middle])
        digits_num.pop(middle)

    while len(digits_num) > 0:
        total += int(digits_num[0] + digits_num[-1])
        digits_num.pop(0)
        digits_num.pop(-1)

    return total
    
# Simulates a "menu" represented as a given list with to first element "selected" by square brackets. Using move_forward() and move_backward() methods changes the selection respectively and the display() method shows the list with its selection bracketed.
class Menu():
    def __init__(self, lst, cursor=0):
        self.list = lst
        self.cursor = cursor

    def move_forward(self):
        self.cursor += 1
        if self.cursor == len(self.list):
            self.cursor = 0

    def move_backward(self):
        self.cursor -= 1
        if self.cursor == -1:
            self.cursor = len(self.list) - 1

    def display(self):
        self.list_display = self.list[:]
        self.list_display[self.cursor] = [self.list_display[self.cursor]]
        return self.list_display

# Consider a circle and two squares. One square's sides touch the circle, and the other squares corners touch the circle. This evaluates the area difference of the squares.
def square_areas_difference(radius):
    return 2 * radius**2

# Simple calculator simulation which can add, subtract, multiply, and divide
class Calculator():
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "approaches infinity"
        return num1 / num2

# Creates a "Collatz" sequence and returns its maximum number. The sequence is a list starting from the given number. If the number is even, the next number is halved. If odd, it is multiplied by 3 and 1 is added. This contionues until the current number is 1.
def max_collatz(num):
    # Conditional used to avoid an infinite loop
    if num != int(num) or num < 0:
        return num
    collatz = [num]
    while collatz[-1] != 1:
        collatz.append(
            collatz[-1] / 2) if collatz[-1] % 2 == 0 else collatz.append((collatz[-1] * 3) + 1)
    return int(max(collatz))
