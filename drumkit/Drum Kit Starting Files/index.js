document.addEventListener("keydown",function(){ 
    let actualKey=event.key.toLowerCase();
    playSound(actualKey)
    buttonAnimation(actualKey)
})
// document.addEventListener("keyup",function(){ 
//     let aVariable='.'+event.key;
//     document.querySelector(aVariable).style.color="#DA0463";
//     document.querySelector(aVariable).
// });
// let audio=[
//     "sounds/crash.mp3",
//     "sounds/kick-bass.mp3",
//     "sounds/snare.mp3",
//     "sounds/tom-1.mp3",
//     "sounds/tom-2.mp3",
//     "sounds/tom-3.mp3",
//     "sounds/tom-4.mp3"  
// ];
// for(let i=0;i<8;i++){ 
//     document.querySelectorAll(".drum")[i].addEventListener("click",function(){ 
//         let sound=new Audio(audio[i]);
//         sound.play();
//     });
//     }


for(let i=0;i<8;i++){ 
    document.querySelectorAll(".drum")[i].addEventListener("click",function(){ 
        let buttonInnerHtml=this.innerHTML;
        playSound(buttonInnerHtml)
        buttonAnimation(buttonInnerHtml)
    });
} 
function playSound(alpha){ 
    switch(alpha){ 
        case "w": 
        let crash =new Audio("sounds/crash.mp3");
        crash.play();       
        break;
        case "a": 
        let kick =new Audio("sounds/kick-bass.mp3");
        kick.play();
        break;
        case "s": 
        let snare =new Audio("sounds/snare.mp3");
        snare.play();
        break;
        case "d": 
        let tom1 =new Audio("sounds/tom-1.mp3");
        tom1.play();
        break;
        case "j": 
        let tom2 =new Audio("sounds/tom-2.mp3");
        tom2.play();
        break;
        case "k": 
        let tom3 =new Audio("sounds/tom-3.mp3");
        tom3.play();
        break;
        case "l": 
        let tom4 =new Audio("sounds/tom-4.mp3");
        tom4.play();
        break;
    default: 
    console.log("wrong key");
    }
}
function buttonAnimation(key){ 
console.log(key)
document.querySelector('.'+key).classList.add("pressed")
setTimeout(function(){ 
    document.querySelector('.'+key).classList.remove("pressed")
},200)
}