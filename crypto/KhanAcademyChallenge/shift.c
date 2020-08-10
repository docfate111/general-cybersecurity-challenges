#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char * encrypt(char *a, int key){
char *ciphertext = (char *) malloc(sizeof(char) * strlen(a));
for(int i=0; i<strlen(a); i++){
ciphertext[i]=((a[i]+key)%26)+'A';
}
return ciphertext;}
char * decrypt(char *a, int key){
char *ciphertext=(char *) malloc(sizeof(char) * strlen(a));
for(int i=0; i<strlen(a); i++){
ciphertext[i]=((a[i]+26-key)%26)+'A';}
return ciphertext;}
int main(){
char m[40];
int k, choice;
while(1){
printf("1 for encryption, 2 for decryption, Ctrl+C to exit ");
scanf("%d", &choice);
if(choice==1){
printf("Enter message to encrypt(must be all caps): ");
scanf("%s", m);
printf("Key: ");
scanf("%d", &k);
printf("%s \n", encrypt(m, k));}
else if(choice==2){
printf("Enter message to decrypt: ");
scanf("%s", m);
printf("Key: ");
scanf("%d", &k);
printf("%s \n", decrypt(m, k));}
else{
printf("Invalid input");
break;}
} 
return 0;}
