const fs=require("fs");
let theData=fs.readFileSync("fileNumberOne.txt");
console.log("data being read from the text file ");
console.log(theData.toString());
console.log("read")
 
