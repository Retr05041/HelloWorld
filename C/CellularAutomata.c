//
//  Basic Cellular Automata
//
//  Created by Parker Cranfield
//  
//  This program was a very very basic Cellular Automation - I am proud to say I very much enjoyed this one.


/* Includes */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* Initialize Functions */
int printGeneration();
int newGeneration();
int rules();
int confirm_int();

/* Main */
int main(int argc, char const *argv[])
{
    /* Get commands, declare and initialize variables */
    int command1, command2, command3;
    int ruleSet[8];
    int *previousGeneration = NULL;
    int *nextGeneration = NULL;
    int z, i, j, k;
    int numOfGenerations;

    /* Checks if valid input */
    if (argc != 4) {
        return 1;
    } else if (confirm_int(argv[1]) == 0 || confirm_int(argv[2]) == 0 || confirm_int(argv[3]) == 0) {
        return 1;
    } else if (argc != 4 || atoi(argv[1]) <= 0 || atoi(argv[2]) <= 0 || atoi(argv[3]) < 0 || atoi(argv[3]) > 255) {
        return 1;
    } else {
        command1 = atoi(argv[1]); /* # of cells */
        command2 = atoi(argv[2]); /* # of generations */
        command3 = atoi(argv[3]); /* # for rule */
    }


    /* command1 to number of cells - allocates memory */
    previousGeneration = (int *) calloc(command1, sizeof(int));
    memset(previousGeneration, 0, command1 * sizeof(int));
    nextGeneration = (int *) calloc(command1, sizeof(int));
    memset(nextGeneration, 0, command1 * sizeof(int));

    for (z=0; z < command1; z++) {
        if (command1/2 == z) {
            previousGeneration[z] = 1;
            continue;
        }
        previousGeneration[z] = 0;
    } 

    /* command2 to number of generations */
    numOfGenerations = command2;

    /* command3 to binary for ruleSet */
    for (i = 0; i < 8; i++) {
        ruleSet[7-i] = command3%2;
        command3 /= 2;
    }

    /* Prints each generation and generates a new one */
    for (j = 0; j < numOfGenerations; j++) {
        printGeneration(command1, previousGeneration);
        newGeneration(command1, previousGeneration, nextGeneration, ruleSet);

        for (k = 0; k < command1; k++) {
            previousGeneration[k] = nextGeneration[k];
        }
    }

    /* Frees memory and ends main successfuly */
    free(previousGeneration);
    free(nextGeneration);
    return 0;
}

/* Prints each generation */
int printGeneration(int sizeOfList, int list[]) {
    int i;
    char x;
    for (i = 0; i < sizeOfList; i++) {
        x = list[i] ? '*' : ' ';
        printf("%c", x);
    }
    
    printf("\n");
    return 0;
} 

/* Generates a new generation from the last */
int newGeneration(int sizeOfPreviousList, int previousList[], int *newList, int ruleset[8]) {
    int i;
    int left;
    int middle;
    int right;
    int newstate = 420;
    for (i = 0; i < sizeOfPreviousList; i++) {

        if (i == 0) left = previousList[sizeOfPreviousList-1]; else left = previousList[i-1];
        if (i == sizeOfPreviousList-1) right = previousList[0]; else right = previousList[i+1];

        middle = previousList[i];


        newstate = rules(left,middle,right, ruleset);
 
        newList[i] = newstate;
    }
    return 0;
}

/* defines the rules for the generation to be created based off the ruleset */
int rules (int a, int b, int c, int ruleset[8]) {
    int bin = 0;
    if (c)
        bin += 1;
    if (b) 
        bin += 2;
    if (a)
        bin += 4;

    return ruleset[7-bin];
}

/* confirms the input is an integer */
int confirm_int(char* string) {
    int i;
    char hold;
    for (i = 0; string[i] != '\0'; i++) {
        hold = string[i];
        if (hold < '0') {
            return 0;
        } else if (hold > '9') {
            return 0;
        }
    }
    return 1;
}