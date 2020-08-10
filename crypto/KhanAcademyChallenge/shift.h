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

