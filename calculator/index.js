function clearr(keyclear){ 
    console.log(keyclear+"this one is clearing")
    $("h1").slideUp().slideDown();
    $("h1").text(0);
}
var operationFunction='';
var firstNumber=0;
function calc(value){ 
    let oldValue=$("h1").text();
    value=Number(value)+oldValue*10;
    $("h1").text(value+" ");
    console.log(typeof(value))
    console.log(value)
    let len=$("h1").text().length-1
    if(len>15){ 
        alert("Limit reached")
        $("h1").text(0);
    }
}
function operation(keyValue){ 
    firstNumber=Number($("h1").text());
    operationFunction=keyValue;
    $("h1").text(0);
    switch(keyValue){
 case "add":
        $("h2").text(firstNumber+"+");
        break;
        case "sub":
            $("h2").text(firstNumber+"-");
            break;
            case "mul":
                $("h2").text(firstNumber+"*");
                break;
                case "div":
                    $("h2").text(firstNumber+"/");
                    break;
    }
}
function equal(){ 
    $("h2").text('Calculator');
    let secondNumber=Number($("h1").text());    
    if(operationFunction == 'add'){ 
        $("h1").text(firstNumber+secondNumber);
    }
    if(operationFunction == 'sub'){ 
        $("h1").text(firstNumber-secondNumber);
    }
    if(operationFunction == 'mul'){ 
        $("h1").text(firstNumber*secondNumber);
    }
    if(operationFunction == 'div'){ 
        $("h1").text(firstNumber/secondNumber);
    }
}
