/*Team ArmorBuns - Wei Wen Zhou, Soojin Choi
SoftDev1 pd8
K29 -- Sequential Progression
2018-12-19
*/
var fibonacci = function(n) {
    // Returns the nth Fibonacci number
    if (n == 0) {
        return 0;
    }
    if (n < 3) {
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

var gcd = function(a, b) {
    // Returns gcd of a, b
    var x;
    if (a < b) {
        x = a;
    } else {
        x = b;
    }
    while (x > 0) {
        if (a % x == 0 && b % x == 0) {
            return x;
        }
        x--;
    }
}

var randomStudent = function() {
    // Returns a random value from a list
    var list = ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad' ];
    return list[Math.floor(Math.random()*list.length)];
}

var eventOne = function(){
    // Generates a random integer, n, between [0,10) and changes the text to the nth Fibonacci number
    randVal = Math.floor(Math.random() * 10);
    retVal = fibonacci(randVal)+"<br>";
    console.log(retVal);
    var textbox = document.getElementById('log');
    textbox.innerHTML = textbox.innerHTML + retVal;
    return retVal;
};

// Please Click button
var b = document.getElementById('button');
console.log(b);
b.addEventListener('click', eventOne);

// Clear Output button
b.addEventListener('click', eventOne);