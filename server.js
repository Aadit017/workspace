const express=require("express")
const app=express();
app.get("/",function(req,res){
res.send("this is the home/landing page")
})//'/' this is the root of our homepage 
app.listen(3000,function(){// 3000 is the port we will be working on  
    console.log("starting the server ")
});
app.get('/contacts',function(req,res){ 
res.send("contact me ")
})
app.get('/aboutme',function(req,res){ 
    res.send('this is the about me page and here ill be sharing the ')
})
app.get('/hobbies',function(req,res){ 
    res.send('<ul><li>javascript</li><li>java</li></ul>')
})
// this is the call back function example 
// const message=function(){ 
//     console.log("yo this is a callback function")
// }
// setTimeout(function(){ message },100);