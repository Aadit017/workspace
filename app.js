const express=require('express')

const https =require('https')
const http=require("http")
const app=express();
const bodyParser=require("body-parser")
app.use(bodyParser.urlencoded({extended:true}))
app.listen(3000,function(){ 
    console.log('starting the server')
})
app.get('/',function(req,res){ 
    res.sendFile(__dirname+"/index.html")
})
app.post('/',function(req,res){ 
    console.log(req.body.cityName)
    const location=req.body.cityName
     const apiKey="9d9bc10b3beb944c39396d17325abe29"
     const unitType="metric"
     let url="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apiKey+"&units="+unitType 
    //  https://api.openweathermap.org/data/2.5/weather?q=London&appid=9d9bc10b3beb944c39396d17325abe29&units=metric
     // this http's' is very important in the get request method 
     https.get(url,function(responce){ 
         console.log("the below is the status code ")
         console.log(responce.statusCode);
         responce.on("data",function(data){
             const weatherData=JSON.parse(data)//json.stringify would have converted it into 
             // console.log(weatherData)          //a one line string form 
             const description=weatherData.weather[0].description
             const temp=weatherData.main.temp
             const name=weatherData.name
             const icon=weatherData.weather[0].icon
             const imageUrl="http://openweathermap.org/img/wn/"+icon+"@2x.png"
             // res.send("the temperature is "+temp+" degree celsius and it feels like "+description);
             res.write("<p><h1> The temperature of "+name+" is "+temp+" C </h1> </p>")
        
              res.write("seems a bit "+description)
             res.write("<img src="+imageUrl+">")
             res.end()
        
            })
            })
})
// res.send is basically-> 
// res.write()
// and then res.end()
// so if you want ot write multiple lines use res.write()
// as many times as you want and then use res.end()
