#include<stdio.h>
#include<string.h>

int main(){
    char buffer[16];

    printf("enter the input:");
    fgets(buffer, sizeof(buffer),stdin);

    printf("you entered: %s\n",buffer);

    return 0;
}

