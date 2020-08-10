#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char *decrypt(char* nums);
//polybius square remembers indexes start at 0 (global var)
char polybius_square[5][5]={"abcde", "fghij", "klmno", "pqrst", "uvwxy"};
//can be written with different letters (i.e. with z without i/j)
int main(){
	char input[275];
	printf("Enter a string: ");
	scanf("%s", input);
	printf("%s", decrypt(input));
	return 0;
}
char* decrypt(char* nums){
	int l=(int) strlen(nums);
	int i=0; int j= 0;
	char *output=(char *)malloc(l);
	while(i<l){
		int r=nums[i++]-'1';
		int c=nums[i++]-'1';
		output[j++]=polybius_square[r][c];
	}
	return output;
}
