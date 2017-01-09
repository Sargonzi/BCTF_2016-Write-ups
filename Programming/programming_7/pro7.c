#include<stdio.h>

int max(int num1, int num2);

int main () {

int a = 40000778;
int b = 48406343;
int c = 400007783;
int d = 300007784;
int e = 300007785;
int ret;

ret = max(a, b);

printf( "BCTF{%d}\n", ret );


return 0;
}

int max(int num1, int num2) {

int result;

if (num1 > num2)
result = num1;
else
result = num2;

return result;
}