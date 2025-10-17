#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

#define MAX_WORDS 20
#define MAX_WORD_LENGTH 20
#define GRID_SIZE 10
#define MAX_ATTEMPTS 100


/**
 * Generate a 10x10 word search puzzle containing the given words.
 * 
 * @param words A vector of strings to include in the puzzle.
 * @return A 2D vector of chars representing the word search puzzle.
 */
void create_crossword(char words[][MAX_WORD_LENGTH], int wordCount, char grid[GRID_SIZE][GRID_SIZE]) {
    // WRITE YOUR CODE HERE
}

void trim(char* str) {
    // Remove leading whitespace
    int start = 0;
    while (str[start] && (str[start] == ' ' || str[start] == '\t' || str[start] == '\r' || str[start] == '\n')) {
        start++;
    }
    
    // Move string to beginning
    int i = 0;
    while (str[start]) {
        str[i++] = str[start++];
    }
    str[i] = '\0';
    
    // Remove trailing whitespace
    int end = strlen(str) - 1;
    while (end >= 0 && (str[end] == ' ' || str[end] == '\t' || str[end] == '\r' || str[end] == '\n')) {
        str[end--] = '\0';
    }
}

int main() {
    srand(time(NULL));
    
    char wordsInput[1000];
    if (!fgets(wordsInput, sizeof(wordsInput), stdin)) {
        fprintf(stderr, "An unexpected error occurred: Failed to read input\n");
        return 1;
    }
    
    char words[MAX_WORDS][MAX_WORD_LENGTH];
    int wordCount = 0;
    
    // Parse comma-separated words
    char* token = strtok(wordsInput, ",");
    while (token != NULL && wordCount < MAX_WORDS) {
        trim(token);
        if (strlen(token) > 0) {
            strcpy(words[wordCount], token);
            wordCount++;
        }
        token = strtok(NULL, ",");
    }
    
    char grid[GRID_SIZE][GRID_SIZE];
    create_crossword(words, wordCount, grid);
    
    // Print the result
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            printf("%c", grid[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}