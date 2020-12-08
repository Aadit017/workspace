// console.log(new Error("something bad happened"))
// console.warn("this is a warning ")
// if we have to use the console class 
// const out=getStreamSomehow()
// const err=getStreamSomehow()
// const myconsole = new console.Console(out,err)
// myconsole.log('this is working ')
// console.assert(true,"does nth")
// console.assert(false,"does nth")
// console.assert()
// let cond=!0
// console.assert(cond,"if this is true it wil do nth")
// console.assert()
// 0! this means true 
// and !1 this means false 
// console.clear() this is basically for clearing the console
// -------------------------------------------------------------
// console.table([{a:1,b:2},{a:'A',b:'B'}])
// ┌─────────┬─────┬─────┐
// │ (index) │  a  │  b  │
// ├─────────┼─────┼─────┤
// │    0    │  1  │  2  │
// │    1    │ 'A' │ 'B' │
// └─────────┴─────┴─────┘
//-------------------------------
console.time("time->")
for(let i=0;i<100000000;i++){ 
    i=i+1-1;
};
console.timeEnd("time->")
// both the labels have to be same 