#include<stdio.h>
#include<string.h>
#include<arpa/inet.h>
#include<unistd.h>

int scan_port(int port){
    int sock;
    struct sockaddr_in server;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0 ) return 0;

    server.sin_family = AF_INET;
    server.sin_port = htons(port);
    server.sin_addr.s_addr = inet_addr("127.0.0.1");

    int result = connect(sock, (struct sockaddr *)&server, sizeof(server));

    close(sock);

    if (result ==0 )
        return 1;
    else
        return 0;

}

int main(){
    int ports[] = {22, 80, 443, 3306};
    int size = 4;
     
    for (int i =0;i < size; i++){
        if (scan_port(ports[i]))
            printf("port %d: OPEN\n", ports[i]);
        else
            printf("port %d: CLOSED\n",ports[i]);
    }
    return 0 ;
}