var result = document.getElementsByClassName("result")[0];
var operatorIndex = -1;
var operator = undefined;
var firstNumber = 0;
var dot = false;


function init() {
    window.resizeTo("240", "360");

    initButtons();
}

function initButtons() {
    var buttons = document.getElementsByClassName("button");

    for (var i = 0; i < buttons.length; i++) {
        buttons[i].onclick = function() { append(this.value) };
    }
}

function append(value) {
    if (/\d/.test(value)) {
        result.value += value;
        return;
    }
    if (value == '.') {
        if (lastIsDigit() && !dot) {
            result.value += value;
            dot = true;
        }
        return;
    }

    if (!lastIsDigit()) return;
    firstNumber = calc();
    dot = false;

    if (['+','-','×','÷','*','/'].indexOf(value) != -1) {
        if (operator != undefined) result.value = firstNumber;
        operator = value;
        operatorIndex = result.value.length;
        result.value += value;
        return;
    }
    if (value == '=') {
        operator = undefined;
        result.value = firstNumber;
        return;
    }
}

function lastIsDigit() {
    var str = result.value;
    return /\d/.test(str[str.length - 1]);
}

function calc() {
    if (operator === undefined) 
        return parseFloat(result.value);
        
    var secondNumber = parseFloat(
        result.value.substring(operatorIndex + 1));
    
    if (operator == '+')
        return firstNumber + secondNumber;
    if (operator == '-')
        return firstNumber - secondNumber;
    if (['×','*'].indexOf(operator) != -1)
        return firstNumber * secondNumber;
    if (['÷','/'].indexOf(operator) != -1)
        return firstNumber / secondNumber;
}