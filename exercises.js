// Checks whether a given array contains the number 7.
function sevenBoom(arr) {
    if (arr.includes(7)) {
        return "Boom!";
    }
    return "there is no 7 in the array";
}

// Takes a variable number of integers, each representing the number of items in a set, and returns the number of combinations that can be made by taking one from each item. This is actually just the product of the numbers of items per each set; i.e. the product of the arguments.
function combinations() {
    let args = Array.from(arguments);
    let total = 1;
    for (let ind = 0; ind < args.length; ind++) {
        total *= args[ind];
    }
    return total;
}

// Takes an array of strings and returns only the strings that have numbers in them
function numInStr(arrayOfStrings) {
    let numbers = "1234567890";
    function isNumber(char) {
        for (let i = 0; i < numbers.length; i++) {
            if (char === numbers[i]) {
                return true;
            };
        };
    };

    let result = [];
    for (let i = 0; i < arrayOfStrings.length; i++) {
        let iArray = arrayOfStrings[i].split("");
        if (iArray.filter(isNumber).length > 0) {
            result.push(arrayOfStrings[i]);
        };
    };
    return result;
};

// Checks whether a number is "oddish" or "evenish." A number is oddish or evenish depending on whether the sum of the digits is odd or even.
function oddishOrEvenish(num) {
    if (numb % 2 === 0) {
        return "Evenish";
    }

    let numAsArray = String(numr).split("");
    digits = numAsArray.filter(digitCheck => digitCheck !== ".");
    oddDigits = digits.filter(digit => digit % 2 !== 0);
    if (oddDigits.length % 2 !== 0) {
        return "Oddish";
    }
    return "Evenish";
};

// Checks whether there is at least one instance in a string where both the last letter of one word and the first of the adjacent word are vowels
function hasVowelLinks(str) {
    let wordLinks = [];
    for (let i = 0; i < str.length - 2; i++) {
        if (str[i+1] === " ") {
            wordLinks.push(str.slice(i,i+3));
        }
    }
    let vowels = "aeiouAEIOU";
    let vowelLinks = wordLinks.filter(wordLink => (vowels.includes(wordLink[0]) && (vowels.includes(wordLink[2]))));
    return vowelLinks.length > 0;
}

// Shows the "leaders" in an array of numbers, or the numbers that are larger than all of the following numbers in the array.
function leader(arr) {
    let leaders = [];
    for (let i = 0; i < arr.length; i++) {
        let subArr = arr.slice(i);
        if (arr[i] === Math.max(...subArr)) {
            leaders.push(arr[i]);
        }
    }
    return leaders;
}

// Takes two binary objects (numbers or strings) with equal numbers of ones and zeros and returns the number of swaps betwwen two numbers in one object to make it eqaul the other.
// Example: the number 1001 takes two swaps of numbers before it equals 0110.
function minSwaps(binary1, binary2) {
    let total_swaps = 0;
    for (let i = 0; i < binary1.length; i++) {
        if (binary1[i] !== binary2[i]) {
            total_swaps += 0.5;
        }
    }
    return Math.floor(total_swaps);
}

// Checks whether an integer has all number 0-9 included in its digits. MIGHT work with large integers.
function isPandigital(int) {
    let exponent = Math.floor(Math.log10(int));
    let digitArray = [];
    while (int > 0) {
        if (int < 10) {
            digitArray.push(int);
            break;
        }
        let digitToAdd = Math.floor(int / (10**exponent));
        digitArray.push(digitToAdd);
        int -= digitToAdd * 10**exponent;
        console.log(int);
        exponent -= 1;
    }

    console.log(digitArray);

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    for (let i = 0; i < numbers.length; i++) {
        if (!digitArray.includes(numbers)) {
            return false;
        }
    }

    return true;
}

// Checks whether a 3D rectangular brick with dimensions a, b, and c can fit through a rectangular hole with width w and height h. The brick may be turned, but only in right angles
function doesBrickFit(a, b, c, w, h) {
    if ((w < a && (h < b || w < c)) || 
        (w < b && (h < a || h < c)) || 
        (w < c && (h < a || h < b))) {
        return false;
    }
    return true;
}

// Checks whether a string is ALMOST a palindrome, such that the string is spelled the same forwards and backwards if one and only one character is changed to another
function almostPalindrome(string) {
    let stringArray = string.split('');
    let reverseArray = stringArray.slice().reverse();

    let checkForOne = stringArray.filter(function(character, index) {
        if (character !== reverseArray[index]) {
            return true;
        }
    });

    if (checkForOne.length === 2) {
        return true;
    }
    return false;
}

// Returns the Fibonacci number of the given index using recursion
function fibo(num) {
    if (num === 0 || num === 1) {
        return num;
    }
    return fibo(num - 2) + fibo(num - 1);
}

// Returns the total number of non-nested items in a nested array (empty arrays within the initial array count as 1)
function getLength(arr) {
    let result = arr.length;
    for (let item of arr) {
        if (Array.isArray(item)) {
            if (item.length === 0) {
                result++;
            }
            result += (getLength(item) - 1);
        }
    }
    return result;
}

// "Maps" a string into numbers (one for each unique character) and returns an array of the string as these mapped numbers
function characterMapping(str) {
    let characters = [...(new Set(str.split('')))];
	
	let map = str.split('').map(function(char) {
        let number = characters.indexOf(char);
		return number
    });
	
	return map;
}

// Returns a boolen telling whether of not an array as more unique positive values than unique negative values
function isPositiveDominant(arr) {
    let uniqueValues = [...(new Set(arr))];
    let positive = 0;
    let negative = 0;

    for (value of uniqueValues) {
        if (value > 0) {
            positive++;
        }
        else if (value < 0) {
            negative++;
        }
    }

    return positive > negative;
}

// Returns whether a number is Zygodrome, or a number that can be partitioned into clusters of repeating digits (so cannot be a single digit number). So, 33 is Zygodrome, but 332, 1, and 1001 are not.
function isZygodrome(num) {
    let numAsArray = num.toString().split('');

    let result = numAsArray.every((num, index) => {
        if (index === 0) {
            return num === numAsArray[index + 1];
        }
        else {
            return !(num !== numAsArray[index-1] && num !== numAsArray[index+1]);
        }
    })

    return result;
}

// Checks a string whether there are three question marks between two single-digit numbers that add to 10
function QuestionsMarks(str) {   
  let parts = str.split('???');

  for (let i = 0; i < parts.length - 1; i++) {
    if (Number(parts[i][parts[i].length - 1]) + Number(parts[i + 1][0]) === 10) {
      return true;
    }
  }

  return false; 
}

//  Calculates whether a line intersects a point on a point, where the line is given as a string representing a slope-intercept equation "y = mx + b", where m is the slope and b is the y intercept
function willHit(equation, position) {
    equation = equation.replaceAll(" ", "");
    let equationToSplit = [];
    for (item of equation) {
        if (item === '+' || item === '-') {
            equationToSplit += ('!' + item);
        }
        else {
            equationToSplit += item;
        }
    }

    let equationArray = equationToSplit.split(/\!|y\=/g);
    equationArray = equationArray.filter(item => item !== "");

    let slope = 0;
    let yIntercept = 0;
    if (equationArray.length === 2) {
        slope = Number(equationArray[0].slice(0 ,equationArray[0].length - 1));
        yIntercept = Number(equationArray[1]);
    }
    else if (equationArray.length === 1 && equationArray[0] !== '0') {
        if (equationArray[0].indexOf("x") === -1) {
            yIntercept = Number(equationArray[0]);
        }
        else {
            slope = Number(equationArray[0].slice(0 ,equationArray[0].length - 1));
        }
    }

    let [xChange, yChange] = [position[0], position[1] - yIntercept];

    if ((yChange / xChange) === slope) {
        return true;
    }
    return false;
}

// Returns the number of "boomerangs" found in the array. A boomerang is defined as an array or sub-array of 3 elements which reads the same forwards and backwards, and whose elements are not identical.
function countBoomerangs(arr) {
    let result = 0;
    for (let i = 0; i < arr.length - 2; i++) {
        if ((arr[i] === arr[i+2]) && (arr[i] !== arr[i+1])) {
            result++;
        }
    }
    return result;
}

// Takes 2 arrays and returns an array showing the common elements betwwen them
function commonElements(arr1, arr2) {
    let arr1set = [...new Set(arr1)];
    let arr2set = [...new Set(arr2)];
    return arr1set.filter(item => arr2set.includes(item));
}