#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
int main()
{
	int s,len=sizeof(struct sockaddr_in),sent_conf,cli;
	struct sockaddr_in server,clientDetail;
	char msg[]="Welcome to Yash's Server!";
	if((s=socket(PF_INET,SOCK_STREAM,0))==-1)
	{
		perror("Error in creating socket!");
		exit(-1);
	}
	server.sin_family=AF_INET;
	int port=htons(10000);
	server.sin_port=port;
	server.sin_addr.s_addr=INADDR_ANY;
	bzero(&server.sin_zero,8);
	
		if((bind(s,(struct sockaddr *)&server,len)==-1))
		{
			perror("Error in binding!");
			exit(-1);
		}
		while(1)
		{
		if((listen(s,5))==-1)
		{
			perror("Error in listening!");
			exit(-1);
		}
		if((cli=accept(s,(struct sockaddr *)&clientDetail,&len))==-1)
		{
			perror("Error in accepting!");
			exit(-1);
		}
		printf("Sending data to %s!\n",inet_ntoa(clientDetail.sin_addr));
		write(cli,msg,strlen(msg));
		printf("\n");
	}
		close(cli);
}