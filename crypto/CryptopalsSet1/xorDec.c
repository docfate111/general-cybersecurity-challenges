#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fixedXor.h"
int score(char *s);
int main(){
	char b[68];
	printf("Enter a hex string: ");
	fgets(b, 68, stdin);
	char output[68]; int max=0;
	for(int i=48; i<127; i++){
		printf("%s \n", other_hexor(i, b));
			if(score(other_hexor(i, b))>max){
				max=score(other_hexor(i, b));
				strcpy(output, other_hexor(i, b));
			}
		}
	puts(output);
	return 0;
}
int score(char *s){
	int count=0;
	int l=(int) strlen(s);
	char freq_chars[]="ULDRHSNIOATE";
	for(int i=0; i<l; i++){
		for(int j=0; j<12 ;j++){
			if(toupper(s[i])==freq_chars[j]){
				count+=j;
			}
		}
	}
	return count;
}

