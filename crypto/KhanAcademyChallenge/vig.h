#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *encrypt(char* msg, char* key);
char *decrypt(char* msg, char* key);
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
