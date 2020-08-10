#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "hex264.h"
char *hexor(char *a, char *b);
char *other_hexor(int a, char *b);
int main(){
	char a[68];
	printf("Enter a hex string: ");
	fgets(a, 68, stdin);
	printf("%s", other_hexor(80, a));
	return 0;
}
char *hexor(char *a, char *b){
	int l=(int) strlen(a);
	char hex[]="0123456789abcdef";
	char* output=(char *)malloc(l);
	for(int j=0; j<l; j++){
		output[j]=hex[hex2dec(a[j])^hex2dec(b[j])];
	}
	return output;
}
char *other_hexor(int a, char *b){
	int l=(int) strlen(b);
        char ascii_table[]="!'#$%&'()*+,-.|0123456789:;>=<?@ABCDEFGHIJKLMNOPQRSTUVWXYZ{|}^_'abcdefghijklmnopqrstuvwxyz";
        char* output=(char *)malloc(l);
        for(int j=0; j<l; j++){
		int c=a^hex2dec(b[j]);
		if(c<33|c>122){
			output[j]=' ';
		}else{
			output[j]=ascii_table[c];
		}
        }
	return output;
}

