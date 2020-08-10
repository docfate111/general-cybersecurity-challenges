#include "shift.h"
int scoreEnglish(char *input){
	int score=0;
	for(int i=0; i<(int)strlen(input); i++){
		switch(input[i]){
			case 'E': score+=12; break;
			case 'T': score+=9; break;
			case 'A': score+=8; break;
			case 'O': score+=7; break;
			case 'I': score+=6; break;
			case 'N': score+=5; break;
			case 'S': score+=5; break;
			case 'R': score+=5; break;
			case 'H': score+=4; break;
			default: break;
		}
	}
	return score;
}
int main(){
        char m[150];
        printf("Enter message to decrypt: ");
        scanf("%s", m);
	int toPrint=0;
	int max=1;
	for(int i=0; i<26; i++){
		if(scoreEnglish(decrypt(m, i))>max){
        		max=scoreEnglish(decrypt(m, i));
			toPrint=i;
		}else{continue;}
        }
	printf("%s", decrypt(m, toPrint));
        return 0;
        }
