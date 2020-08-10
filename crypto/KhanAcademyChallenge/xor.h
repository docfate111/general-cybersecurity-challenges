#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int *xorarr(int *m, int *n, int l);
int *xorarr(int *m, int *n, int l){
	int* nums=malloc(l);
	for(int i=0; i<l; i++){
		nums[i]=m[i]^n[i];
		printf("%d", nums[i]);
	}
	return nums;
}
