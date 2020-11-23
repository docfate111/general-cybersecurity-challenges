// Write a program that uses a single asynchronous filesystem operation to  
// read a file and print the number of newlines it contains to the console  
// (stdout), similar to running cat file | wc -l.  
const fs = require('fs');
var myNumber = 0;
fs.readFile(process.argv[2], 'utf-8', function(err, fileContents){
    if(err){
        console.log(err.message);
    }else{
        console.log(fileContents.split('\n').length-1);
    }
});