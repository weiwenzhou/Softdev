/*Team Law of C - Wei Wen Zhou, Maryann Foley
SoftDev1 pd8
K28 -- Sequential Progression
2018-12-18
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
