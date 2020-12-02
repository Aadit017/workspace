let buttonColors=["red","blue","green","yellow"]
var randomNumber;
let gamePattern=[]
let userPattern=[]
let start=false
let level=0
$(document).keydown(function (e) { 
     if(!start){
     nextSequence();  
     console.log(e.key)
     start=true
}});
$(".btn").on('click',function(){ 
     let userChosenColor=$(this).attr("id")
     userPattern.push(userChosenColor)
     let sound=new Audio('sounds/'+userChosenColor+'.mp3')
     sound.play()   
     animateButton(userChosenColor) 
     checkAnswer(userPattern.length-1)
});
function nextSequence(){ 
     userPattern=[]
     level+=1;
     $("#level-title").text("level "+level)
     randomNumber=Math.floor((Math.random()*4))
     let randomChosenColor=buttonColors[randomNumber];
     gamePattern.push(randomChosenColor)
     console.log(gamePattern)
     $('#'+randomChosenColor).fadeOut(100).fadeIn(100);
     playSound(randomChosenColor)   
}
function playSound(color){ 
     let audio=new Audio('sounds/'+color+'.mp3')
     audio.play()
}
// animate button function 
function animateButton(userChosenColor){ 
     $('#'+userChosenColor).addClass("pressed")
     setTimeout(function(){ 
          $('#'+userChosenColor).removeClass("pressed")
     },100);
}
// this function is to check the answer 
function checkAnswer(colorLength){ 
if(gamePattern[colorLength]===userPattern[colorLength]){
   console.log("success")
   if(userPattern.length===gamePattern.length){
     setTimeout(function()
     {
     nextSequence();
     },1000)
}}
else{ 
     let wrongSound=new Audio('sounds/wrong.mp3')
     wrongSound.play()
     console.log("wrong")
     $("body").addClass("game-over")
     setTimeout(function(){
          $("body").removeClass("game-over")
     },200)
     $("h1").text("Game Over press any key to continue")
     level=0
     gamePattern=[]
     userPattern=[]
     start=false
}}

