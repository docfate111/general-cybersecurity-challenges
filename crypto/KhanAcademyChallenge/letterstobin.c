#include "xor.h"
int* letterstobin(char *m);
int main(){
	int *n=malloc(14);
	n=letterstobin("thisissometext");
	for(int w=0; w<sizeof(n)/sizeof(int); w++){
		printf("%d", n[w]);
	}
 	//xorarr(letterstobin("hi"), letterstobin("by"), 2);
	return 0;
}
int* letterstobin(char *m){
	int l=(int) strlen(m);
	int* out=malloc(l);
	//if it is a vowel it is a 1
	int bin=0;
	int k=0;
	char vowels[]="aeiouy";
	for(int i=0; i<l; i++){
		for(int j=0; j<6; j++){
			if(m[i]==vowels[j]){
				bin=1;
				break;
			}
		}
		char c=bin+'0';
		out[k++]=c;
		bin=0;
	}
		return out;
	}
