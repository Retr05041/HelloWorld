//
//  Student File Input Output
//
//  Created by Parker Cranfield
//  
//  This program was written to get input from a couple .csv files, and display them to the user, or do calculations based of student grade

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <unistd.h>

int countLine(FILE *fp) { // Counts the number of lines in the file
    char *buffer = NULL;
    size_t bufsize;
    int numOfLines = 0;
    while (getline(&buffer,&bufsize,fp) != -1) {
            numOfLines++;
    }
    free(buffer);
    return numOfLines;
}

int* getTotalGrades(char *path, int numOfActivities) { // the .csv file contained a list of grades, this took them and returned an array of them
    int *grades = (int *)malloc(sizeof(int) * numOfActivities);
    FILE *fp = fopen(path, "r");
    int i = 0;
    int x = 0;

    char *buffer = NULL;
    size_t bufsize;

    while (getline(&buffer,&bufsize,fp) != -1) {
        if (x == 0) {x++; continue;}
        strtok(buffer, ",");
        grades[i] = atoi(strtok(NULL, ","));
        i++;
    }

    free(buffer);
    fclose(fp);
    return grades;
}

float standardDeviation(float mean, int *grades, int numOfStudents, int absentStudents) { // Calculates standard deviation of the given grades
    int i;
    float add = 0;

    for (i=0; i < numOfStudents-absentStudents; i++) {
        add += pow(grades[i]-mean, 2);
    }

    add += pow(mean, 2)*absentStudents;


    return sqrt(add/numOfStudents);
    
}

int main(int argc, char *argv[])
{
    FILE *fpStudents;
    FILE *fpActivity;
    char *students;
    char *activity;
    int totalStudents;
    int totalActivities;
    int *grades;
    int total = 0;
    int i;
    float deviation;

    if (argc != 3 || strstr(argv[1], "student") == NULL || strstr(argv[2], "activity") == NULL) { // I/O Check
        return 1;
    }

    students = argv[1];
    activity = argv[2];
    


    if (!(fpStudents = fopen(students, "r")) || !(fpActivity = fopen(activity, "r"))) { // Opens the file - returns an error if failure
	    fprintf(stderr, "error opening file(s)\n");
	    exit(EXIT_FAILURE);
    }
    totalStudents = countLine(fpStudents)-1;
    totalActivities = countLine(fpActivity)-1;
    grades = getTotalGrades(activity, totalActivities);

    for (i=0; i<totalActivities; i++){ 
        total += grades[i];
    }

    deviation = standardDeviation((float)total/totalStudents, grades, totalStudents, totalStudents-totalActivities);

    // Displays the findings to the user
    printf("total students = %d\n", totalStudents);
    printf("absent students = %d\n", totalStudents-totalActivities);
    printf("grade mean = %.2f\n", (float)total/totalStudents);
    printf("grade sd = %.2f\n", deviation);
    fclose(fpStudents);
    fclose(fpActivity);
    free(grades);
    return 0;
}
