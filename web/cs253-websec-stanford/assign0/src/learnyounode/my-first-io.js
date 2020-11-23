// Write a program that uses a single synchronous filesystem operation to  
//   read a file and print the number of newlines (\n) it contains to the  
//   console (stdout), similar to running cat file | wc -l.  
   
//   The full path to the file to read will be provided as the first  
//   command-line argument (i.e., process.argv[2]). You do not need to make  
//   your own test file.  
   
// ## HINTS  
   
//   To perform a filesystem operation you are going to need the fs module from  
//   the Node core library. To load this kind of module, or any other "global"  
//   module, use the following incantation:  
   
const fs = require('fs')  

//   Now you have the full fs module available in a variable named fs.  
   
//   All synchronous (or blocking) filesystem methods in the fs module end with  
//   'Sync'. To read a file, you'll need to use  
//   fs.readFileSync('/path/to/file'). This method will return a Buffer object  
//   containing the complete contents of the file.  
   
//   Documentation on the fs module can be found by pointing your browser here:  
//   file:///usr/local/lib/node_modules/learnyounode/docs-nodejs/fs.html  
buf = fs.readFileSync(process.argv[2]);
console.log(buf.toString().split('\n').length-1);
   
