let superheroes=require("superheroes")
let supervillains=require("supervillains")
let arr=[],ar=[]
for(let i=0;i<5;i++){ 
    arr.push(superheroes.random())
    ar.push(supervillains.random())
}
console.log(arr);
console.log(ar);

  