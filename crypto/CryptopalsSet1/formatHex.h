#include <stdio.h>
#include <string.h>
#include <ctype.h>
char * remove_firstTwo(char *input);
char * clean_hex(char *input);
char * remove_firstTwo(char *input){
        const int l=(int) strlen(input);
        static char output[97];
        for(int i=0; i<l-2; i++){
                        output[i]=input[i+2];
        }
        return output;
}
char * clean_hex(char *input){
        int len = (int) strlen(input);
	static char output[97];
        if(input[1]=='x'){
                printf("Removing '0x' \n");
                input=remove_firstTwo(input);
                }
	char hexchars[17]="0123456789ABCDEF";
        //replacing hex characters with capitalized letter otherwise removing character
	for(int i=0; i<len; i++){
		input[i]=toupper(input[i]);
	}
	int counter=1;
        for(int i=0; i<len; i++){
		for(int j=0; j<17; j++){
			if(input[i]==hexchars[j]){
                		output[i]=hexchars[j];
				counter++;
			}else{
				continue;
			}
      	}}
        //if some symbols aren't hex counter won't be equal to the string's length
        if(counter!=len){
            printf("Warning! Non-hex characters in input string ignored. \n");
        }
        return input;
}

