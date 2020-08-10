#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *encrypt(char* msg, char* key);
char *decrypt(char* msg, char* key);
int main(){
	//implementation of vigenere(polyalphabetic) cipher
	int choice, len;
	while(1){
	printf("\nCtrl+C to exit\n");
	printf("Enter 1 to encrypt or 2 to decrypt: ");
	scanf("%d", &choice);
	if(choice==1){
		printf("\nEnter length of message: ");
		scanf("%d", &len);
		char *input=(char*)malloc(len);
		printf("\nEnter message to encrypt: ");
		scanf("%s", input);
		printf("\nEnter length of key: ");
		scanf("%d", &len);
		char *k=(char*)malloc(len);
		printf("\nEnter key: ");
		scanf("%s", k);
		printf("\nEncrypted message is: %s ", encrypt(input, k));
	}
	if(choice==2){
		printf("\nEnter length of message: ");
                scanf("%d", &len);
                char *input=(char*)malloc(len);
                printf("\nEnter message to decrypt: ");
                scanf("%s", input);
                printf("\nEnter length of key: ");
                scanf("%d", &len);
                char *k=(char*)malloc(len);
                printf("\nEnter key: ");
                scanf("%s", k);
                printf("\nDecrypted message is: %s ", decrypt(input, k));
	}
	else{
		printf("Incorrect input!");
		continue;
	}
	}
	return 0;
}
char *encrypt(char* msg, char* key){
	int kl=strlen(key);
	int ml=strlen(msg);
	char* ctxt=(char*)malloc(ml);
	for(int i=0; i<ml; i++){
			ctxt[i]=(msg[i]+key[(i%kl)])%26+'A';
	}
	return ctxt;
}
char *decrypt(char* msg, char* key){
	int kl=strlen(key);
        int ml=strlen(msg);
        char* ctxt=(char*)malloc(ml);
        for(int i=0; i<ml; i++){
                        ctxt[i]=(msg[i]-key[(i%kl)]+26)%26+'A';
        }
        return ctxt;
}
