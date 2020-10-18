function sevenBoom(array) {
    if (array.includes(7)) {
        return "Boom!"
    }
    return "there is no 7 in the array"
}

function foo() {
    for (var i = 0; i < arguments.length; i++) {
        console.log(arguments[i]);
    }
}

function combonations() {
    let args = Array.from(arguments);
    let total = 1;
    for (let ind = 0; ind < args.length; ind++) {
        total *= args[ind];
    }
    return total;
}

function addressExtractor(str, patt) {
    return str.match(patt);
}

let my_str = "123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St.";

function addressExtractor(my_str) {
    let pattern = /\d[\s\w]{1,}\./g;
    return my_str.match(pattern)
}

let movies = [
    {
        title: "The Hunchback of Notre Dame",
        rating: 8,
        hasWatched: true
    },
    {
        title: "The Road to El Dorado",
        rating: null,
        hasWatched: false
    },
    {
        title: "Toy Story",
        rating: 9,
        hasWatched: true
    },
    {
        title: "The Tigger Movie",
        rating: null,
        hasWatched: false
    }
]

// for (let i = 0; i <= movies.length - 1; i++) {
//     if (movies[i].hasWatched === true) {
//         console.log("You have watched " + movies[i].title + " - " + movies[i].rating/2 + " stars.")
//     }
//     else {
//         console.log("You have not watched " + movies[i].title + ".")
//     }
// };

// movies.forEach( function(movie) {
//     let result = "You have ";
//     if (movie.hasWatched) {
//         result += "watched ";
//     }
//     else {
//         result += "not seen ";
//     }
//     result += "\"" + movie.title + "\" - ";
//     result += movie.rating/2 + " stars."
//     console.log(result)
// });

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

function minSwaps(binary1, binary2) {
    let total_swaps = 0;
    for (let i = 0; i < binary1.length; i++) {
        if (binary1[i] !== binary2[i]) {
            total_swaps += 0.5;
        }
    }
    return Math.floor(total_swaps);
}

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

    console.log(digitArray)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    for (let i = 0; i < numbers.length; i++) {
        if (!digitArray.includes(numbers)) {
            return false
        }
    }

    return true;
}