/*
Team Law of C - Wei Wen Zhou, Maryann Foley
SoftDev1 pd8
K30 -- Sequential Progression III: Season of the Witch
2018-12-20
*/


list = document.getElementById("thelist"); // <ol> : the list
fibList = document.getElementById("fiblist"); // <ol> : fib list
head = document.getElementById("h"); // <h1>
button0 = document.getElementById("b"); // <button> : The Button
fibButton = document.getElementById("fb"); // <button> : fib button

var fibonacci = function(n) {
    // Returns the nth Fibonacci number

    // Why think when you can hard-code it haha!
    var list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765];

    if (n < list.length) {
        return list[n];
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

var first = 0;
var second = 1;

var fib2 = function() {
    var temp = first + second;
    first = second;
    second = temp;
    return first;
}

// Changes the header to the text of the <li> item hover over
list.addEventListener("mouseover",function(e){
    console.log(e.target);
    if (e.target.nodeName == "LI") {
    console.log("Change Header");
    head.innerHTML=e["target"].innerHTML;
    }
    //what is "h"
})

// Changes the header to Hello World when you are no longer leave the <ol> area
list.addEventListener("mouseout",function(e){
    console.log(e);
    console.log("Change Header");
    head.innerHTML="Hello world!";
})

// Removes the <li> item that has been clicked
list.addEventListener("click", function(e) {
    console.log(e);
    if (e.target.nodeName == "LI") {
        e.target.remove();
        head.innerHTML= "Hello world!";
    }
})

// Adds a <li> iten to the <ol> when clicked
button0.addEventListener("click", function(e) {
    console.log(e);
    var node = document.createElement("LI");
    node.innerHTML = "WORD";
    list.appendChild(node);
})

// Adds the next fib # to the second <ol> when clicked
var nth = 1;
fibButton.addEventListener("click", function(e) {
    console.log(e);
    var node = document.createElement("LI");
    node.innerHTML = fib2();
    fibList.appendChild(node);
    nth += 1;
})
