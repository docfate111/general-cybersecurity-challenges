#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char *decrypt(char* nums);
//polybius square remembers indexes start at 0 (global var)
char polybius_square[6][6]={"fghijk", "exyz1l", "dw892m", "cv7!3n", "bu654o", "atsrqp"};
//can be written with different letters (i.e. with z without i/j)
int main(){
	char nums[]="52515053513003403040503505521010523002102550510330520045535015505325503520315041155102035151452545535345215051241450255000511053501550532551105251315041155130452010035242423222251010515051401550300545415110352";
	printf("%s", decrypt(nums));
	return 0;
}
char* decrypt(char* nums){
	int l=(int) strlen(nums);
	int i=0; int j= 0;
	char *output=(char *)malloc(l);
	while(i<l){
		int r=nums[i++]-'0';
		int c=nums[i++]-'0';
		output[j++]=polybius_square[r][c];
	}
	return output;
}
