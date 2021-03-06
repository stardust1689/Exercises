import math
import string
import datetime
import functools
import re

def check_odd(number):
    '''
    Returns a list of odd products from a list of numbers, using check_odd() callback to filter out any even numbers
    '''
    if number % 2 != 0:
        return True
    return False

def list_of_multiples(num, length):
    '''
    Returns a list of numbers, each the next multiple of num, with a given length
    '''
    return [num * (i+1) for i in range(length)]

def print_for_loop(start = 10, end = 1, step = -1):
    '''
    Prints all items in a for loop in reverse order as their negative values
    '''
    for item in range(start, end-1, step):
        print(-item)
        
def middle_chars(a_string):
    '''
    Returns the middle three character in a string
    '''
    length = len(a_string)
    start = int(length/2 - 1.5)
    end = start + 3
    result = ""
    for num in range(start, end):
        result += a_string[num]
    return result

def check_bad(char):
    '''
    Checks whether nor not a character is alphanumeric.
    '''
    bad = string.punctuation
    for symbol in bad:
        if char == symbol:
            return False
    return True
    

def remove_symbols(my_string):
    '''
    Remove all non-alphanumeric characters in a string (spaces allowed). Uses callback remove_bad() to filter out symbols.
    '''
    return "".join(list(filter(check_bad, my_string)))

def check_dict_values(dictionary, value):
    '''
    Checks whether a given value is in a given dictionary.
    '''
    if value in list(dictionary.values()):
        return True
    return False

# my_dictionary = {'a': 100, 'b': 200, 'c': 300}
# my_value = 200

def is_curzon(numbah):
    '''
    Checks whether a number is a "Curzon" number. A Curzon number is one where 2 to the power of that number plus 1 is divisible by two times that number plus one.
    '''
    print(numbah)
    powah = 2**numbah + 1
    multiply = 2*numbah + 1
    if powah % multiply == 0:
        return True
    return False

def time_saved(speed_limit, your_speed, distance, time_unit="hours"):
    '''
    Returns how much (or little) time is saved when you drive a given distance at a given speed above that of the given speed limit.
    '''
    time_speeding = distance / your_speed
    time_at_limit = distance / speed_limit
    return f"{time_at_limit - time_speeding} {time_unit}"

def encode_morse(message_string):
    '''
    Takes a string and returns it in Morse code.
    '''
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

    morse_trans = message_string.maketrans(char_to_dots)
    morse = message_string.translate(morse_trans)
    return morse

def has_friday_13(month, year):
    '''
    Checks whether "Friday the 13th" occurs in a given month and year.
    '''
    thirteenth = datetime.date(year, month, 13)
    if thirteenth.weekday() == 4:
        return True
    return False

def karaca(string):
    '''
    Encodes a string by reversing it, replacing all vowels with a certain number, then adding "aca" at the end.
    '''
    encrypting = string.lower()[::-1]
    karaca_dict = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    table = string.maketrans(karaca_dict)
    encrypting = encrypting.translate(table)
    return encrypting + 'aca'

def power_ranger(n, a, b):
    '''
    Returns the number of given integer powers (n) between one number and another (a and b), inclusive.
    '''
    bottom = math.ceil( a**(1/n) )
    top = math.floor( b**(1/n) )
    in_range = list(range(bottom, top+1))
    return len(in_range)

def consecutive_combo(*args):
    '''
    Take any number of lists of integers, combines them, and checks if all integers between the minimum and maximum of the combined list is present (redundencies not allowed).
    '''
    combo = []
    for next_list in args:
        combo += next_list
        
    range_to_meet = range(min(combo), max(combo)+1)
    for num in range_to_meet:
        if num not in combo:
            return False
    
    return True

def majority_vote(lst):
    '''
    Takes a list and returns the majority vote from that list, or the item whose count is greater than half the list's length.
    '''
    for item in lst:
        if lst.count(item) > len(lst) / 2:
            return item


def is_prime(num):
    '''
    Checks whether given number is prime.
    '''
    if num <= 3 and int(num) == num and num != 1:
        return True
    try:
        range(2, num)
    except:
        return False
    for factor in range(2 , num):
        if num % factor == 0:
            return False
    return True

def sum_primes(lst):
    '''
    Returns the sum of all prime numbers in the given list.
    '''
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    return sum(primes)

def next_prime(num):
    '''
    Returns the next prime number after the given number.
    '''
    current = math.ceil(num)
    if current == num:
        current += 1
    while True:
        if is_prime(current):
            return current
        current += 1

def filter_primes(lst):
    '''
    Takes a list of numnbers and returns a list those number which are prime. Non-integers and negative numbers, and 0 are not included.
    '''
    return list(filter(lambda num: is_prime(num), lst))

def number_of_primes(num):
    '''
    Returns the number of prime numbers up to and including the given number.
    '''
    return len(filter_primes(list(range(2,num+1))))

def factorial(number):
    '''
    Returns the factorial of the number (number!, or 1 * 2 * 3 *...* (number-1) * number).
    '''
    if number == 0 or number == 1:
        return 1
    factors = range(2, number+1)
    if number > 1:
        result = 1
        for number in factors:
            result = result*number
        return result
    

def factorial_recursion(number):
    '''
    Returns the factorial of the number (number!, or 1 * 2 * 3 *...* (number-1) * number) using recursion.
    '''
    return 1 if number < 2 else number*factorial_recursion(number-1)

def kempner(number):
    '''
    "Kempner" function; returns the smallest integer greater than 0 whose factorial is divisible by the input. Returns 0 if input is not an integer or is <= 0.
    '''
    if type(number) != int or number <= 0:
        return 0
    kemp = 1
    while factorial(kemp) % number != 0:
        kemp += 1
    return kemp

def first_before_second(string, first, second):
    '''
    Checks a string whether or not all instances of the character "first" come before all instances of the character "second."
    '''
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

def count_datatypes(*args):
    '''
    Builds then returns a dictionary of the count of all datatypes of any number of arguments.
    '''
    datatype_count = {}
    
    for item in args:
        if type(item) in datatype_count.keys():
            datatype_count[type(item)] += 1
        else:
            datatype_count[type(item)] = 1
            
    return datatype_count

# print(count_datatypes(2, 3, 4.5, 6, "asds", [1,2,3], np.array([1,2,3]), {"a": 2}, (123,24)))

def is_disarium(num):
    '''
    Checks is a number is "Disarium". A number is Disarium if the sum of the digits raised to their respective postions equals the number itself.

    For example, 135 is Disarium because 1^1 + 2^2 + 5^3 = 135.
    '''
    total = 0
    power = 1
    for n in str(num):
        total += int(n)**power
        power += 1
    return total == num
        
# print(is_disarium(518))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def binary_search_is_prime(primes, num):
    '''
    Uses a binary search algorithm to check if a number is within a list of sorted prime numbers.
    '''
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

def grade_precentage(score, required):
    '''
    Checks an exam score whether it meets the requirement to pass an exam. Both arguments are strings.
    '''
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

def tallest_skyscraper(skyline):
    '''
    "skyline" is a 2D list with 1's being building space and 0's being empty space. Returns the height of the tallest skyscraper(s).
    '''
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

def meme_sum(num1, num2):
    '''
    "Adds" two numbers incorrectly, instead using the method shown on https://en.meming.world/wiki/Girl_at_Whiteboard_Adding
    '''
    total = []
    lst1 = list(str(num1))
    lst2 = list(str(num2))
    
    while len(lst1) != len(lst2):
        lst2.insert(0,0) if len(lst1) > len(lst2) else lst1.insert(0,0)
            
    for digit in range(len(lst1)):
        total.append( str(int(lst1[digit]) + int(lst2[digit])) )
        
    return int(''.join(total))

def combinations(*args):
    '''
    Takes a variable number of integers, each representing the number of items in a set, and returns the number of combinations that can be made by taking one from each item.
    '''
    nonzero_args = filter(lambda num: num != 0, list(args))
    return functools.reduce(lambda total, acc : total*acc, nonzero_args)

def one_list(lst):
    '''
    Takes a list of lists and combines them into a single list.
    '''
    result = []
    for item in lst:
        result += item
    return result

def make_transpose(matrix):
    '''
    Takes a 2D matrix (written as a list of lists, each inner list being a row) and returns its TRANSPOSE (flipped over by its diagonal).
    '''
    result = []
    for column in range(len(matrix[0])):
        result.append([])
        for row in range(len(matrix)):
            result[column].append(matrix[row][column])
    return result

def chars_at_position(lst_str, pos):
    '''
    Takes a list OR a string and returns the list or string containing only the elements whose position is a multiple of 'pos'.
    '''
    valid_indices = list(range(pos, len(lst_str) + 1, pos))
    result = [lst_str[num-1] for num in valid_indices]
    if type(lst_str) == str:
        return ''.join(result)
    return result

def find_fulcrum(lst):
    '''
    Takes a list and returns the value whose sum of the values on one side equals that of the other, or its "fulcrum." Example: the fulcrum of the list [5,2,1,4] is 2, because 5 (the sum of values on its left) = 1 + 4 (the sum on its right). 
    '''
    for i in range(1, len(lst) - 1):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return lst[i]
    return -1

def make_box(side):
    '''
    Returns a list containing a "square" box with each side having 'side' (an integer) * the string '#'.
    '''
    result = []
    result.append('#'*side)
    for num in range(1, side - 1):
        result.append('#' + ' ' * (side-2) + '#')
    result.append('#'*side)
    return result

def sentence_searcher(txt, word):
    '''
    Searches for a word in a string and returns the entire sentence containing the word (not case-sensitive).
    '''
    result = ''
    for char in txt:
        result += char
        if char == '.':
            if word.lower() in result.lower():
                return result.strip()
            result = ''
    return result

def face_interval(lst):
    '''
    In a list, the interval is the difference between the maximum and the minimum. Returns ":)" if the interval is in the list, ":(" if not, and "/" if the argument is not a list.
    '''
    if type(lst) != list:
        return ':/'
    interval = max(lst) - min(lst)
    return ':)' if interval in lst else ':('

def no_duplicate_letters(txt):
    '''
    Takes a string and returns whether all words have no duplicate letters.
    '''
    txt_lst = txt.lower().split()
    
    def has_duplicate(next_string):
        for letter in next_string:
            if next_string.count(letter) > 1:
                return True
        return False
    
    return len(list(filter(has_duplicate, txt_lst))) == 0

def no_duplicate_letters2(txt):
    '''
    More efficient version of no_duplicate_letters().
    '''
    txt_lst = txt.lower().split()
    
    for next_string in txt_lst:
        for letter in next_string:
            if next_string.count(letter) > 1:
                return False
            
    return True

def triangle_perimeter(p1, p2 ,p3):
    '''
    Takes the three poins of a triangle in Cartesian coordinates and returns the perimeter.
    '''
    side1 = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    side2 = math.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)
    side3 = math.sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2)
    return round(side1 + side2 + side3, 2)


def closing_in_sum(num):
    '''
    Takes digit "num" returns the sum of the combined digits of the first and last digit of num, the second and second-last digit of num, until the digits reach the center of num.

    Example: closing_in_sum(5645) => 119, becuase 55 + 64 = 119.

    If the length of num is odd, the center digit is added alone. Ex: closing_in_sum(343) => 33 + 4 = 37.
    '''
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
    
class Menu():
    '''
    Simulates a "menu" represented as a given list with to first element "selected" by square brackets. Using move_forward() and move_backward() methods changes the selection respectively and the display() method shows the list with its selection bracketed.
    '''
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

def square_areas_difference(radius):
    '''
    Consider a circle and two squares. One square's sides touch the circle, and the other squares corners touch the circle. This evaluates the area difference of the squares.
    '''
    return 2 * radius**2

class Calculator():
    '''
    Simple calculator simulation which can add, subtract, multiply, and divide.
    '''
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

def max_collatz(num):
    '''
    Creates a "Collatz" sequence and returns its maximum number. The sequence is a list starting from the given number. If the number is even, the next number is halved. If odd, it is multiplied by 3 and 1 is added. This contionues until the current number is 1.
    '''
    # Conditional used to avoid an infinite loop
    if num != int(num) or num < 0:
        return num
    collatz = [num]
    while collatz[-1] != 1:
        collatz.append(
            collatz[-1] / 2) if collatz[-1] % 2 == 0 else collatz.append((collatz[-1] * 3) + 1)
    return int(max(collatz))

def show_the_love(lst):
    '''
    Takes a list of numbers, removes 25% from each number that is NOT the smallest number on the list, then adds the sum total of these removals to the smallest number.
    '''
    give = 0
    for num in lst:
        if num != min(lst):
            give += 0.25 * num
    return [0.75 * num if num != min(lst) else num + give for num in lst]

def chunkify(lst, n):
    '''
    Takes a list and returns it split into several lists with a length of n. If the list cannot be split evenly, the last chunk's length is the remainder.
    '''
    result = []
    while len(lst) > 0:
        result.append(lst[0:n])
        for num in range(n):
            try: lst.pop(0) 
            except IndexError: break

    return result

def item_pairs(string):
    '''
    Takes a string and returns the number of pairs for each unique item.
    '''
    pairs = 0
    lst = string.split()
    uniques = set(lst)
    for item in uniques:
        pairs += math.floor(lst.count(item) / 2) 
    return pairs

def loves_me(num):
    '''
    "Loves me, loves me not" is a traditional method of determining whether a person who loves another loves him back. The person plucks off the petals of a flower one at a time, saying "Loves me" then "loves me not" repatedly until all of the petals have been plucked.
    
    This function simulates that method with a flower of a given number of petals.
    '''
    result = ""
    petal = 1
    while petal < num:
        result += "Loves me, " if petal % 2 != 0 else "Loves me not, "
        petal += 1
    result += "LOVES ME" if petal % 2 != 0 else "LOVES ME NOT"
    return result

def pop(lst):
    '''
    When a water balloon pops, it soaks the area around it. This function simulates that by takeing a list of numbers with only one nonzero element and returns a "soaked" list.
    '''
    nonzero = max(lst)
    ind = lst.index(nonzero)
    while ind > 0 and nonzero > 0:
        lst[ind - 1] = nonzero - 1
        nonzero -= 1
        ind -= 1
    nonzero = max(lst)
    ind = lst.index(nonzero)
    while ind < len(lst) and nonzero > 0:
        lst[ind + 1] = nonzero - 1
        nonzero -= 1
        ind += 1
    return lst

def mark_math(lst):
    '''
    Takes a list of equations presented as strings and evaluates the percentage of equations that ore correct.

    Only one operation (addition or subtraction) is allowed, and it must be on the left side of the equation.

    Only integers allowed.

    Negative numbers are allowed, but only on the right side of the equation.
    '''
    correct = 0
    num_pattern = re.compile(r'\d+')
    op_pattern = re.compile(r'\+|-')

    for attempt in lst:
        eqn_lst = attempt.split("=")
        numbers = list(map(lambda num: int(
            num), num_pattern.findall(eqn_lst[0]) + eqn_lst[1:]))
        operation = op_pattern.findall(attempt)

        if operation[0] == "+":
            if numbers[0] + numbers[1] == numbers[2]:
                correct += 1
        elif operation[0] == "-":
            if numbers[0] - numbers[1] == numbers[2]:
                correct += 1
    
    return str(round(correct/len(lst) * 100)) + "%"

def solutions(a, b, c):
    '''
    Given the equation a*x**2 + b*x + c = 0, this function returns the number of real solutions.
    '''
    if a == 0 and b == 0 and c != 0:
        return "invalid equation"
    elif a == 0 and b == 0 and c == 0:
        return 0
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0

def sastry(n):
    '''
    If the concatenation of a positive integer plus (itself + 1) is a perfect square, the number is a Sastry number. This function evaluates this condition with a positive integer.
    '''
    concat = int(str(n) + str(n + 1))
    root = concat ** (1/2)
    return root == int(root)

def non_digits(string):
    '''
    Seperates a string by any digits then rejoins each segment with a whtiespace.
    '''
    pattern = re.compile(r'\D+')
    return " ".join(pattern.findall(string))

def shell_volume(outer, inner):
    '''
    Takes the radii of two concentric spheres and calculates the volume of the outer shell, or the difference in the two spheres' volumes, rounded to three decimals.
    '''
    return round((4/3) * math.pi * (outer**3 - inner**3), 3)

def invert(dictionary):
    '''
    "Inverts" a dictionary, or takes the values of a dictionary and makes them the keys, and vice-versa.
    ''' 
    inverted = {}
    for key in dictionary:
        inverted[dictionary[key]] = key
    return inverted

def cube_diagonal(volume):
    '''
    Takes the volume of a cube and return its diagonal, or the length through the cube from one vertex to the opposite vertex, rounded to two decimal places.
    '''
    edge = volume**(1/3)
    side_diagonal = 2**(1/2) * edge
    return round((edge**2 + side_diagonal**2)**(1/2), 2)

def non_alphanumeric(string):
    '''
    Takes a string and returns all non-alphanumeric and whitespace characters.
    '''
    pattern = re.compile(r'[^A-Za-z0-9\s]')
    return re.findall(pattern, string)


def add(num_str1, num_str2):
    '''
    Takes two numbers as strings and reeturns their sum as a a string. Returns "invalid operation" if either cannot be converted into a number.
    '''
    try: 
        return str(float(num_str1) + float(num_str2))
    except ValueError:
        return "Invalid operation"

def lines_are_parallel(line1, line2):
    '''
    Determines whether two lines are parallel. Lines are represented by two lists with three elements, with the list [a,b,c] reflecting the line ax + by = c in xy-coordinates.
    '''
    return (line1[0] / line1[1]) == (line2[0] / line2[1])

class NumDiv():
    '''
    Class with a number as a parameter with properties ".ones", ".threes", and ".nines", which show how many 1's 3's, and 9's fit into the number respectively. 
    '''
    def __init__(self, num):
        self.ones = round(num)
        self.threes = round(num / 3)
        self.nines = round(num / 9)

def check_score(lsts):
    '''
    Takes a list of lists and checks the "score" of each element (indicated in the function). If the TOTAL score is > 0, the score is returned; else 0 is returned.
    '''
    score_values = {
        "#": 5,
        "O": 3,
        "X": 1,
        "!": -1,
        "!!": -3,
        "!!!": -5
    }
    score = 0
    for lst in lsts:
        for item in lst:
            try:
                score += score_values[string]
            except KeyError:
                continue
    return score if score > 0 else 0

def normalize(string):
    '''
    Takes a string and returns the string with all letters lowercase except the first character.
    '''
    first_letter_cap = string[0].upper()
    lower_conversion = map(lambda char: char.lower(), list(string[1:]))
    return first_letter_cap + "".join(lower_conversion)

def sum_fractions(frac1, frac2):
    '''
    Takes two lists, each with two elements representing the numerator and denomenator of a single fraction, and returns the sum of the two fractions in the same format, plus the nearest integer to the sum.
    '''
    frac1_common_den = [frac1[0] * frac2[1], frac1[1] * frac2[1]]
    frac2_common_den = [frac2[0] * frac1[1], frac2[1] * frac1[1]]
    frac_sum = [frac1_common_den[0] + frac2_common_den[0], frac1_common_den[1]]
    lowest_possible_fact = min(frac1_common_den[0], frac2_common_den[0])
    for num in range(lowest_possible_fact, 0, -1):
        if frac1_common_den[0] % num == 0 and frac2_common_den[0] % num == 0:
            frac_sum = [frac_sum[0] / num, frac_sum[1] / num]
            break
    return [int(frac_sum[0]), int(frac_sum[1])], int(frac_sum[0] / frac_sum[1])


def happiness_number(string):
    '''
    Takes a string and returns a score of how "happy" it is. Each instance of ":)" and "(:" add 1, and each instance of ":(" and "):" take away 1.
    '''
    return string.count(":)") + string.count("(:") - string.count(":(") - string.count("):")

def same_length(sequence):
    '''
    Takes a number or string and checks whether every consecutive sequence of ones is followed by a consecutive sequence of zeroes of the same length.
    '''
    if type(sequence) == int:
        sequence = str(sequence)
    if sequence.count("0") + sequence.count("1") != len(sequence):
        return False
    consecutive_nums = []
    new_cons_string = ""
    for i in range(len(sequence)):
        if new_cons_string == "" or sequence[i] in new_cons_string:
            new_cons_string += sequence[i]
        else:
            consecutive_nums.append(new_cons_string)
            new_cons_string = sequence[i]
        if i == len(sequence) - 1:
            consecutive_nums.append(new_cons_string)
    for i in range(0, len(consecutive_nums), 2):
        if len(consecutive_nums[i]) != len(consecutive_nums[i+1]):
            return False
    return True

def pentagonal(number):
    '''
    Consider a group of marbles arranged as a series of pentagons with a single marble at the center surrounded by a pentagon of 2 marbles per side, surrounded by another pentagon with 3 per side, etc.
    
    This function returns the total number of marbles depending on how many sides the outermost pentagon is, or how "deep" the series is.
    '''
    total = 1
    if int(number) != number or number < 1:
        return 0
    if number > 1:
        for num in range(2, number+1):
            total += 5 * (num - 1)
    return total

def weekday_dutch(date_str):
    dutch_days = {
        0: "maandag",
        1: "dinsdag",
        2: "woensdag",
        3: "donerdag",
        4: "vrijdag",
        5: "zaterdag",
        6: "zondag"
    }
    pattern = re.compile(r'\d+')
    [day, month, year] = map(lambda num: int(num), pattern.findall(date_str))
    date = datetime.date(year, month, day)
    return dutch_days[date.weekday()]
