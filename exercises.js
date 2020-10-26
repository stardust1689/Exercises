// Checks whether a given array contains the number 7.
function sevenBoom(array) {
    if (array.includes(7)) {
        return "Boom!"
    }
    return "there is no 7 in the array"
}

// function foo() {
//     for (var i = 0; i < arguments.length; i++) {
//         console.log(arguments[i]);
//     }
// }

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
function oddishOrEvenish(number) {
    if (number % 2 === 0) {
        return "Evenish";
    }

    let numAsArray = String(number).split("");
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
function isPandigital(integer) {
    let exponent = Math.floor(Math.log10(integer));
    let digitArray = [];
    while (integer > 0) {
        if (integer < 10) {
            digitArray.push(integer);
            break;
        }
        let digitToAdd = Math.floor(integer / (10**exponent));
        digitArray.push(digitToAdd);
        integer -= digitToAdd * 10**exponent;
        console.log(integer);
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
    let stringArray = string.split("");
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
