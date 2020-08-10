#include <stdio.h>
#include <stdlib.h>
int *xorarr(int *m, int *n, int l);
int main(){
	int a[4]={1, 1, 0, 1};
	int b[4]={1, 1, 1, 0};
	int l=sizeof(a)/sizeof(int);
	xorarr(a, b, l);
	return 0;
}
int *xorarr(int *m, int *n, int l){
	int* nums=malloc(l);
	for(int i=0; i<l; i++){
		nums[i]=m[i]^n[i];
		printf("%d", nums[i]);
	}
	return nums;
}
