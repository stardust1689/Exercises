// Checks whether a given array contains the number 7.
function sevenBoom(arr) {
    if (arr.includes(7)) {
        return "Boom!";
    }
    return "there is no 7 in the array";
}

// Takes a variable number of integers, each representing the number of items in a set, and returns the number of combinations that can be made by taking one from each item.
function combinations() {
    return Array.from(arguments).reduce((total, item) => item !== 0 ? total*item : total);
}

// Takes an array of strings and returns only the strings that have numbers in them
function numInStr(arrayOfStrings) {
    let numbers = "1234567890";
    const hasNum = function(str) {
        for (char of str) {
            if (numbers.includes(char)) {return true;}
        }
    }

    return arrayOfStrings.filter(hasNum);
};

// Checks whether a number is "oddish" or "evenish." A number is oddish or evenish depending on whether the sum of the digits is odd or even.
function oddishOrEvenish(num) {
    let numAsArray = String(num).split("");
    digits = numAsArray.filter(digitCheck => digitCheck !== ".");
    oddDigits = digits.filter(digit => digit % 2 !== 0);
    if (oddDigits.length % 2 !== 0) {
        return "Oddish";
    }
    return "Evenish";
};

// Checks whether there is at least one instance in a string where both the last letter of one word and the first of the adjacent word are vowels
function hasVowelLinks(str) {
    let words = str.split(' ');
    let vowels = "aeiouAEIOU";
    for (i = 0; i < words.length - 1; i++) {
        if ( (vowels.includes(words[i][words[i].length - 1]) && (vowels.includes(words[i + 1][0]) ) ) ) {
            return true
        }
    }
    return false
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

// Returns the total number of non-nested items in a nested array (Empty arrays within the initial array do NOT count.)
function getLength(arr) {
    let result = arr.length;
    for (let item of arr) {
        if (Array.isArray(item)) {
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

// Returns the number of days between two date objects, as a rounded integer
const getDays = (date1, date2) => Math.round(Math.abs(date1 - date2) / 86400000)

// Returns the string which falls next in the alphabetically in a string in a fashion similar to a number in base-27
function nextLetters(str) {
    if (str === '') return 'A';
    let letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    let strArrCapRev = str.toUpperCase().split('').reverse();
    let resultRevArr = [];
    
    while (strArrCapRev.length > 0) {
        if (strArrCapRev[0] === 'Z') {
            resultRevArr.push('A');
            if (strArrCapRev[1] !== 'Z') {
                resultRevArr.push(letters[letters.indexOf(strArrCapRev[1]) + 1]);
                resultRevArr.push(strArrCapRev.slice(2).reverse().join(''));
                break
            }
            strArrCapRev.shift();
        } else {
            resultRevArr.push(letters[letters.indexOf(strArrCapRev[0]) + 1]);
            resultRevArr.push(strArrCapRev.slice(1).reverse().join(''));
            break
        }
    }
    
    let result = resultRevArr.reverse().join('');
    return result;
}

// Sorts an array of numbers by the number of "holes" within each number. For reference, the numbers 0, 4, 6, and 9 have 1 hole, 8 has 2 holes, and the rest have 0 holes.
function holeySort(arr) {
    return arr.sort(function(num1, num2) {
        const num1Arr = num1.toString().split('');
        const num2Arr = num2.toString().split('');
        const oneHole = digit => (digit === '0' || digit === '4' || digit === '6' || digit === '9')
        const twoHole = digit => (digit === '8')
        const num1holes = num1Arr.filter(oneHole).length + 2*num1Arr.filter(twoHole).length;
        const num2holes = num2Arr.filter(oneHole).length + 2*num2Arr.filter(twoHole).length;
        return num1holes - num2holes;
    })
}

// An alternative to "holeySort()"
function holeySort2(arr) {
    return arr.sort(function(num1, num2) {
        const hasHoles = digit => '04689'.includes(digit);
        const num1HoleyArr = num1.toString().split('').filter(hasHoles);
        const num2HoleyArr = num2.toString().split('').filter(hasHoles);
        const holeNumbers = { '0': 1, '4': 1, '6': 1,  '8': 2, '9': 1 };
        const holeCount = (total, digit) => total + holeNumbers[digit];
        const num1holes = num1HoleyArr.reduce(holeCount, 0);
        const num2holes = num2HoleyArr.reduce(holeCount, 0);
        return num1holes - num2holes;
    })
}

// Take a string and inserts a whitespace where there is camel casing, or a space between a lowercase and an uppercase letter
function insertWhitespace(str) {
    let regex = /[a-z][A-Z]/g;
    let x = str.split(regex);
    let y = str.match(regex);
    result = '';
    for (let i = 0; i <= x.length - 2; i++) {
        result += x[i] + y[i][0] + ' ' + y[i][1];
    }
    result += x[x.length - 1];
    return result;
}

// Another version of insertWhitespace()
function insertWhitespace2(str) {
    return str.replace(/([A-Z])([a-z])/g, '$1 $2');
}

// Returns the least common multiple of two numbers
function lcm(num1, num2) {
    let addon = num1;
    let result = num1;
    while (result % num2 !== 0) {
        result += addon;
    }
    return result;
}

// Returns a list of all missing letters in a string
function missingLetters(str) {
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    let missing = alphabet.split('').filter(letter => str.indexOf(letter) === -1);
    return missing.length === 0 ? 'No Missing Letter' : missing;
}

// Returns whether arr1 is an "anti-array" of arr2. arr1 should have only two values. If those two values are reversed, arr1 is an anti-array of arr2 if the reversed array equals arr2.
function isAntiArray(arr1, arr2) {
    let [val1, val2] = [...new Set(arr1)];
    let antiArr1 = [];
    for (let i = 0; i < arr1.length; i++) {
        arr1[i] === val1 ? antiArr1.push(val2) : antiArr1.push(val1);
    }
    return antiArr1.every((item, ind) => item === arr2[ind]);
}

// Takes an array of strings with the word "east" in any format and changes them into the word "west" in the same format.
function wrongWay(arr) {
    const eastToWest = str => {
        let stage1 = str.replace('e', 'w');
        let stage2 = stage1.replace('E', 'W');
        let stage3 = stage2.replace('a', 'e');
        return stage3.replace('A', 'E')
    }
    return arr.map(str => eastToWest(str));
}

// Converts an object to an array of arrays, with each array within being a key / value pair
function toArray(obj) {
    let result = [];
    for (key in obj) {
        result.push([key, obj[key]]);
    }
    return result;
}

// Takes an array of numbers and sorts them in ascending order
function sortArray(arrOfNums) {
    let result = [];
    let arrLength = arrOfNums.length;

    for (let i = 0; i < arrLength; i++) {
        let currentMin = Math.min(...arrOfNums);
        result.push(currentMin);
        arrOfNums.splice(arrOfNums.indexOf(currentMin), 1);
    }

    return result;
}

// Takes an array and returns the number of "truthy" values. A truthy value includes the boolean "true", a nonzero number, a nonempty string, array, object, etc. "null", "NaN", and "undefined" are "falsey" values.
const countTrue = arr => arr.filter(val => val).length

// Consider three cups facing down at positions "A", "B", and "C". A ball is hidden under the cup at B. This function take an array whose elements represent a swap of 2 cups between position; ex. "AB" is a swap between the two cups at A and B. The function returns the postion of the ball after all array swaps are completed.
// NOTE: This works with any number of cups so long as one of them starts at "B". 
function cupSwapping(arr) {
    let ballPosition = 'B';
    for (swap of arr) {
        if (swap.includes(ballPosition)) {
            ballPosition = swap.replace(ballPosition, '');
        }
    }
    return ballPosition;
}

// Takes a duration of time (as "duration") and returns its duration adjusted for "speed"
function playbackDuration(duration, speed) {
    let durnArr = duration.split(":").map(num => Number(num))
    let seconds = durnArr[2] + durnArr[1]*60 + durnArr[0]*3600;
    let playbackSeconds = seconds / speed;
    let playbackHours = Math.floor(playbackSeconds / 3600);
    playbackSeconds -= playbackHours * 3600;
    let playbackMinutes = Math.floor(playbackSeconds / 60);
    playbackSeconds -= playbackMinutes * 60;
    let playbackDurArr = [playbackHours, playbackMinutes, playbackSeconds].map(num => num.toString())
    playbackDurArr = playbackDurArr.map(num => {
        if (num[0] == "0") {
            num = num.split("");
            num.unshift("0");
            return num.join("");
        } else {return num;}
    })
    return playbackDurArr[0] + ":" + playbackDurArr[1] + ":" + playbackDurArr[2];
}

// Consider an integer raised to a power (also an integer). If the product's last digits are the starting integer, it is considered "automorphic". This function evaluates the automorphism from the powers 2 to 10.
function powerMorphic(num) {
    let morphicTotal = 0;
    let numString = num.toString();
    for (let i = 2; i <= 10; i++) {
        let powerString = (num**i).toString();
        powerString.slice(-numString.length) === numString ? morphicTotal++ : morphicTotal;
    }
    return morphicTotal === 9 ? "Polymorphic"
         : morphicTotal === 4 ? "Quadrimorphic"
         : morphicTotal === 2 ? "Dimorphic"
         : morphicTotal === 1 ? "Enamorphic"
         : morphicTotal === 0 ? "Amorphic"
         : "Automorphic";
}

// Constructor function which allows for the creation of a circle
class Circle {
    constructor(radius) {
        this.radius = radius;
    }
    getArea = () => Math.PI * this.radius**2;
    getCircumfrence = () => 2 * Math.PI * this.radius;
}

// Returns the escape velocity of a body with mass m and radius r. Escape velocity is the velocity required to escape the gravitational pull from a body.
// Function reqiures either a given mass, radius, and an optional planet that is in a built-in "planets" object. If a planet is given, the planet's mass and radius override the given mass and radius.
function escapeVelocity(mass, radius, planet=-1) {
    if (planet !== -1) {
        earthMass = 5.976 * 10**24;
        earthRadius = 6.378 * 10**6;
        planets = {
            'mercury': {
                mass: 0.0558, 
                radius: 0.383
            },
            'venus': {
                mass: 0.815, 
                radius: 0.95
            },
            'earth': {
                mass: 1, 
                radius: 1
            },
            'mars': {
                mass: 0.107, 
                radius: 0.532
            },
            'jupiter': {
                mass: 318, 
                radius: 11.2
            },
            'saturn': {
                mass: 95.1, 
                radius: 9.41
            },
            'george': {
                mass: 14.5, 
                radius: 4.06
            },
            'neptune': {
                mass: 17.2, 
                radius: 3.88
            }
        }
        if (planet in planets) {
            mass = planets[planet].mass * earthMass;
            radius = planets[planet].radius * earthRadius;
        }
    }

    return Math.sqrt(13.34 * 10**-11 * mass / radius);
}


// Converts an ordinary JS object into an array of arrays, with the first element in each array being one of the keys of the object and the second the key's value
function objectToArray(obj)  {
    arrFromObj = [];
    for (item in obj) {
        arrFromObj.push([item, obj[item]]);
    }
    return arrFromObj;
}

// Takes an initial temperature number (temp) and the scale (type1, in "fahrenheit", "celcius", and "kelvin"), and converts it into the number in the scale of type2.
function converter(type1, temp, type2) {
    if (type1 === "fahrenheit") {
        let celcius = (temp - 32) * 5/9;
        if (type2 === "celcius") { return celcius; }
        else if (type2 === "kelvin") { return celcius + 273.15; }
    }
    else if (type1 === "celcius") {
        if (type1 === "celcius") {
            if (type2 === "fahrenheit") { return type1 * 9/5 + 32; }
            else if (type2 === "kelvin") { return type1 + 273.15; }
        }
    }
    else if (type1 === "kelvin") {
        let celcius = temp - 237.15;
        if (type2 === "celcius") { return celuius; }
        else if (type2 === "fahrenheit") { return celcius * 9/5 + 32; }
    }
}

// Uses a regular expression to extract all addresses from a string. An address always begins with a number and ends with a dot.
function addresses(str) {
    let pattern = /\d[^\.]+\./g;
    return [...str.matchAll(pattern)];
}

// Uses a regex to extract all complete words from a string
function words(str) {
    let pattern = /\w+/g;
    return [...str.matchAll(pattern)];
}

// Returns the number of "<div>" elements in a string, assumed to be taken from an HTML file
function divCount(str) {
    let pattern = /(<div>)/g;
    return [...str.matchAll(pattern)].length;
}

// Takes an array of strings and returns the array whose string have numbers in them. If none of the strings pass the filter, this returns an empty array.
function numInStrFilters(arr) {
    return arr.filter(str => str.split("").some(char => char == Number(char)));
}

// Uses a regex to test whether a string is a valid PIN. A "valid PIN" is defined as having exactly 4 OR 6 numerical characters. No more or less, not 5 numberals, and no letters or whitespaces.
function validPIN(str) {
    pattern = /^\d{4}$|^\d{6}$/g;
    return pattern.test(str);
}

// Checks if a string is a valid email address via a regex
function checkEmail(str) {
    emailPattern = /^[^\.@]+@[^\.@]+\.[A_Za-z]{3}$/g;
    return Boolean(str.match(emailPattern));
}

// Takes a string and uses regexes to return the string with all of its capital letters moved to the front
function capToFront(str) {
    return str.match(/[A-Z]/g).join("") + str.match(/[^A-Z]/g).join("");
}

// Uses a regex to determin if the string is a valid initial, defined as containing only capital letters with exactly one dot then one whitespace between them. Whitespaces at the beginning or end of the string are allowed.
function initalsAreValid(str) {
    let trimmedStr = str.trim() + " ";
    let initialPattern = /[A-Z].\s/g
    let match = trimmedStr.match(initialPattern)
    if (match) {
        if (match.length === trimmedStr.length / 3) {return true}
    }
    return false;
}

str = "One two three four"

// Takes a string and reverses any word within the string that has an odd length. Words include any letters and numbers.
function reverseOdd(str) {
    let result = "";
    let parts = str.match(/[A-Za-z0-9]+|[^A-Za-z0-9]+/g);
    for (part of parts) {
        if (part.match(/[A-Za-z0-9]+/g) && part.match(/[A-Za-z0-9]+/g).length % 2 !== 0) {
            result += part.split("").reverse().join("");
        }
        else { result += part }
    }
    return result;
}

// Takes an integer as the height of a tetrahedral in marble layers and returns the number of marbles
function tetra(int) {
    return (int * (int + 1) * (int + 2)) / 6
} 

// Concatanates a variable number of arrays into a single array
function concat() {
    result = [];
    for (let arr of arguments) {
        for (let item of arr) {
            result.push(item);
        }
    }
    return result;
}

// Takes an array of items that are either numbers or arrays which contain one number. It would be easy for a human to sort it, but trickier for a computer. This function sorts the array regaring all nested arrays as numbers and return the sorted array, with the nested arrays remaining arrays.
function sortIt(arr) {
    let nums = arr.map(item => Array.isArray(item) ? item[0] : item);
    let numsCopy = nums.slice();
    let result = [];
    while (numsCopy.length > 0) {
        let minNum = Math.min(...numsCopy);
        let minIndex = nums.indexOf(minNum);
        let minCopyIndex = numsCopy.indexOf(minNum);
        result.push(arr[minIndex]);
        numsCopy.splice(minCopyIndex, 1);
    }
    return result
}

function calc(expression) {
    pattern = /[^\+\-\*\/]/g;
    return expression.match(pattern);
}

// Consider a string "str". leftRotation(str) and rightRotation(str) returns an array of strings with each string "rotated" to the left or right such that their elements are pushed to the left are right, with the furthest element moved to the othe end to the string.
function leftRotation(str) {
    let result = [];
    for (let i = 0; i < str.length; i++) {
        let addThis = str.slice();
        for (let j = 0; j < i; j++) {
            addThis += addThis[0];
            addThis = addThis.replace(addThis[0], "");
        }
        result.push(addThis);
    }
    return result;
}

function rightRotation(str) {
    let result = [];
    for (let i = 0; i < str.length; i++) {
        let addThis = str.slice();
        for (let j = 0; j < i; j++) {
            lastElement = addThis[addThis.length - 1];
            addThis = lastElement + addThis.replace(lastElement, "");
        }
        result.push(addThis);
    }
    return result;
}

// Takes a number and checks whether all of its digits are the same. Non-numbers return false.
function isRepdigit(num) {
    if (typeof num !== "number") { return false; }
    let digitArray = Math.abs(num).toString().split("").filter(digit => digit !== ".");
    return digitArray.slice(0, digitArray.length - 1).every((digit, ind) => digit === digitArray[ind + 1]);
}

// Take a number and returns the number of digits. Takes any number, including 0, decimals, and negative numbers. Any trailing zeros do not count as digits.
function countDigits(num) {
    let len = Math.abs(num).toString().split("").filter(digit => digit !== ".").length;
    if (num < 1 && num !== 0 && num > -1) {
        len -= 1;
    }
    return len;
}

// Takes a number and returns how many consecutive natural logarithms it can handle; i.e. how many ln's in ln(ln(ln(...ln(num)))) is possible while ramining valid.
function howManyNatLogs(num) {
    let numOfLogs = 0;
    while (num > 0) {
        num = Math.log(num);
        numOfLogs++;
    }
    return numOfLogs;
}