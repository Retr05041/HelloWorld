//
//  MultiQuoteClient
//
//  Created by Parker Cranfield
//  
//  This program was created to connect to a school server and communicate with it. This program was a mix of my programming and algorithms class and Comptuer fundimentals.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <pthread.h>
#include <sys/socket.h>

#define kMULTIQUOTEPORT 1818

void readNetworkString(int sockfd, char* buff) {// This function gets the response fromt he server
    char getLine[9];
    int lineSize;
    int endOfLine = 0;
    char* setBuffer = buff;
    int i;

    while (endOfLine == 0 && lineSize > 0) {
        lineSize = read(sockfd, getLine, 9);

        for (i = 0; i < lineSize; i++) {
            *setBuffer = getLine[i];
            if (setBuffer != buff && *setBuffer == 10 && *(setBuffer-1) == 13) {
                *(setBuffer-1) = 0;
                endOfLine = 1;
                break;
            }
            setBuffer++;
        }
        *setBuffer = 0;
    }
}


int main(int argc, const char * argv[])
{
    int sockFD;
    int isConnected;
    char line[512];
    char command[128];
    int numOfQuotes;
    int i;

    if (argc != 3) {
        fprintf(stderr, "Not enough commands.\n");
        return 1;
    }

    numOfQuotes = atoi(argv[2]); // sets num of quotes needed 

    sockFD = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP); // Create a socket

    if (sockFD == -1) {
        fprintf(stderr, "Failed to initialise socket.\n");
        return 1;
    }

    struct sockaddr_in serverInfo; // struct holding server info
    struct hostent *phost; // for server ip, as gethostbyname makes a pointer

    memset(&serverInfo, 0, sizeof(serverInfo)); // set mem to 0 for default
    serverInfo.sin_family = AF_INET; // set structs network type
    serverInfo.sin_port = htons(kMULTIQUOTEPORT); // sets structs ip 
    phost = gethostbyname(argv[1]); // Gets the domain from the arguments at runtime
    memcpy(&serverInfo.sin_addr, phost->h_addr, phost->h_length); // copies it to memory

    isConnected = connect(sockFD, (struct sockaddr *)&serverInfo, sizeof(serverInfo)); // connects
    if (isConnected != 0) {
        fprintf(stderr, "Failed to connect.\n");
        return 1;
    }

    while (1) { 
        readNetworkString(sockFD, line); // Read a line

        if (strcmp(line, "BYE") == 0) { // Checks if command is 'BYE' then terminates if true
            break;
        }

        char *closeOrAnother;

        if (--numOfQuotes <= 0) {
            closeOrAnother = "CLOSE";
        } else {
            closeOrAnother = "ANOTHER";
        }

        printf("%s\n\n", line); // prints servers response

        sprintf(command, "%s\r", closeOrAnother); // Gets command from user and sets it to the command var, with size 128
        command[strlen(command)-1] = '\0'; // sets last element to '\0'

        sprintf(line, "%s\r\n", command); // sets line = command with \r \n on the end
        write(sockFD, line, strlen(line)); // sends our command to the server

    }
    close(sockFD);
    return 0;
}
