#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "formatHex.h"
int hex2dec(char c);
char * hex2b64(char *input);
char *divnconq(char *input);
int hex2dec(char c){
	//for numbers the same character in hex is in decimal:
	if(c>='0'&c<='9'){
		return c-48;
	}
	//for characters A through F:
	else{
		return toupper(c)-55;
	}
	}
//takes 3 hex characters and returns 2 base64 characters:
char * hex2b64(char *input){
	int nums[3];
	char *output=(char *)malloc(4*sizeof(char));
	char base64[64]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	//replace each hex with respective decimal through method above:
	for(int i=0; i<3; i++){
		nums[i]=hex2dec(input[i]);
	}
	//hex digits x,y,z->64(4x+(y/4)),16(y%4)+z
	int a=(nums[1]>>2)+(nums[0]<<2);
	output[0]=base64[a];
	int b=(((nums[1])&3)<<4)+nums[2];
	output[1]=base64[b];
	return output;
	}
char *divnconq(char *input){
	int l=(int) strlen(input)+14;
	static char a[4];
	a[3]='\0';
	static char temp[3]; //* arr? char*output
	//divide string into 3 and append converted base64:
	static char output[46];
	int k=0;
	for(int i=0; i<l-(l%3); i++){
		if(i%3==0&i>=3){
			strcpy(temp, hex2b64(a));
			//strcpy changes value of input and so does strcat how to append?
			output[k++]=temp[0];
			output[k++]=temp[1];
		}
		a[i%3]=input[i];
	}
	//const char* pad="=";
	//for the remaining characters padding with = sign
	//for(int j=l-(l%3); j<l; j++){
	//	strcat(output, pad);
	//}
	return output;
}
