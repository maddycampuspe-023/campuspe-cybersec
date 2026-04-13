#include<stdio.h>

int main(){
    int port = 80;
    int *ptr = &port;
    
    printf("port value (variable):%d\n",port);
    printf("port value (pointer): %d \n",*ptr);

    *ptr = 443;
     
    printf("New port value: %d\n",port);

    return 0;
}
