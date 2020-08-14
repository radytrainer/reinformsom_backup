

// let text = "Students";
// let reverseText = "";
// for(let i = 1; i <= text.length; i++) {
//     reverseText += text[text.length-i];
// }
// document.write(text + " => "+ reverseText);




// let star = "*";
// let numberRowOfStart = 6; // row
// let numberColOfStart = 20; // column 
// for(let i = 0; i <= numberRowOfStart; i++) { // row
//    for(let j = 0; j <= numberColOfStart; j++) { // column
//        document.write(star);
//     }
//     document.write(" <br> ");
// }

// let star = "*";
// let numberRowOfStart = 10;
// for(let i = 0; i <= numberRowOfStart; i++) { // row
//    for(let j = 0; j < i+1; j++) { // column
//        document.write(star);
//     }
//     document.write(" <br> ");
// }




let star = "*";
let numberRowOfStart = 10;
for(let i = 0; i <= numberRowOfStart; i++) { // row
   for(let j = 0; j <  numberRowOfStart-i; j++) { // column
       document.write(star);
    }
    document.write(" <br> ");
}

