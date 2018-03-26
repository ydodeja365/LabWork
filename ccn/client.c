#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <unistd.h>
int main(int argc, char *argv[])
{
	int s,len=sizeof(struct sockaddr_in),sent_conf,cli;
	char data[80];
	struct sockaddr_in server;
	//printf("Socket Creating:");
	if((s=socket(AF_INET,SOCK_STREAM,0))==-1)
	{
		perror("Error in creating socket!");
		exit(-1);
	}
	
	server.sin_family=AF_INET;
	int port=htons(10000);
	server.sin_port=port;
	inet_pton(AF_INET,argv[1],&server.sin_addr.s_addr);
	printf("Starting Connection..\n");
	if((connect(s,(struct sockaddr *)&server,len))==-1)
	{
		perror("Error in connecting!");
		exit(-1);
	}
	printf("Client Connected!\n");
	printf("Data from server:");
	
		read(s,data,80);
			fputs(data,stdout);
	close(s);
}