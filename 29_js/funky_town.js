/*Team _ - Wei Wen Zhou, Soojin Choi
SoftDev1 pd8
K29 -- Sequential Progression
2018-12-19
*/
var fibonacci = function(n) {
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
    var list = ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad' ];
    return list[Math.floor(Math.random()*list.length)];
}

var fxn = function() {
    b.nodeValue = "done";
    return 1;
}
var b = document.getElementById("button");
b.addEventListener("click", fxn);
