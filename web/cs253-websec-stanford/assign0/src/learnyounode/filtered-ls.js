// Create a program that prints a list of files in a given directory,  
// filtered by the extension of the files. You will be provided a directory  
// name as the first argument to your program (e.g. '/path/to/dir/') and a  
// file extension to filter by as the second argument.  
const testFolder = process.argv[2];
const fs = require('fs');
var path = require('path');
var ext = '.' + process.argv[3];
fs.readdir(testFolder, (err, files) => {
  files.forEach(file => {
    if(ext==path.extname(file)){
        console.log(file);
    }
  });
});
// For example, if you get 'txt' as the second argument then you will need to  
// filter the list to only files that end with .txt. Note that the second  
// argument will not come prefixed with a '.'.
   
