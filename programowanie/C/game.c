/*
Example execution:


. . #     . . # 
. . .     . # . 
. . #     . . . 
. . .     . . . 

PLAYER
row: 2
column: 2

COMPUTER
row: 2
column: 0
. . #     . . # 
. . .     . # . 
* . #     . . * 
. . .     . . . 

PLAYER
row: 1
column: 1

COMPUTER
row: 0
column: 2
. . @     . . # 
. . .     . @ . 
* . #     . . * 
. . .     . . . 

PLAYER
row: 0
column: 2

COMPUTER
row: 3
column: 0

End of the game
. . @     . . @ 
. . .     . @ . 
* . #     . . * 
* . .     . . . 
Player: 1, computer 0
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define ROWS 4
#define COLS 3
#define TABLES_GAP 4

#define EMPTY 0
#define TARGET 1
#define HIT 2
#define SHOT 3

#define TARGETS 2

int main()
{
  int r, c;
  int t, g;
  int boardP[ROWS][COLS], boardC[ROWS][COLS];
  int targetsP = TARGETS, targetsC = TARGETS;
  char symbols[] = {'.', '#', '@', '*'};
  bool done;
  
  srand(time(NULL));

  // BEGIN: Initialize data
  for (r = 0; r < ROWS; r++) {
    for (c = 0; c < COLS; c++) {
      boardP[r][c] = boardC[r][c] = EMPTY;
    }
  }
  
  for (t = 0; t < TARGETS; t++) {
    while (true) {
      r = rand() % ROWS;
      c = rand() % COLS;
      
      if (boardP[r][c] == EMPTY) {
        boardP[r][c] = TARGET;
        break;
      }
    }
    
    while (true) {
      r = rand() % ROWS;
      c = rand() % COLS;
      
      if (boardC[r][c] == EMPTY) {
        boardC[r][c] = TARGET;
        break;
      }
    }
  }
  // END: Initialize data
    
  // BEGIN: Main game loop
  while (targetsP > 0 && targetsC > 0) {
    // BEGIN: Print boards
    for (r = 0; r < ROWS; r++) {
      for (c = 0; c < COLS; c++) {
        printf("%c ", symbols[boardP[r][c]]);
      }
      for (g = 0; g < TABLES_GAP; g++) {
        printf(" ");
      }
      for (c = 0; c < COLS; c++) {
        printf("%c ", symbols[boardC[r][c]]);
      }
      printf("\n");
    }
    // END: Print boards
        
    // BEGIN: Player's move
    while(true) {
      printf("\nPLAYER\n");
      printf("row: ");
      scanf("%d", &r);
  
      printf("column: ");
      scanf("%d", &c);
      
      if (r >= ROWS || c >= COLS || r < 0 || c < 0)
          continue;
            
      switch (boardC[r][c]) {
        case EMPTY:
          boardC[r][c] = SHOT;
          done = true;
          break;
        case TARGET:
          targetsC -= 1;
          boardC[r][c] = HIT;
          done = true;
          break;
        default:
          done = false;
          break;
      }
      
      if (done) {
       break;
      }
    }
    // BEGIN: Player's move

    // BEGIN: Computer's move
    while(true) {
      r = rand() % ROWS;
      c = rand() % COLS;
      
      switch (boardP[r][c]) {
        case EMPTY:
          boardP[r][c] = SHOT;
          done = true;
          break;
        case TARGET:
          targetsP -= 1;
          boardP[r][c] = HIT;
          done = true;
          break;
        default:
          done = false;
          break;
      }
      
      if (done) {
        printf("\nCOMPUTER\n");
        printf("row: %d\ncolumn: %d\n", r, c);
        break;
      }
    }
    // END: Computer's move
  }
  // END: Main game loop
  
  // BEGIN: Print final result
  printf("\nEnd of the game\n");
  for (r = 0; r < ROWS; r++) {
    for (c = 0; c < COLS; c++) {
      printf("%c ", symbols[boardP[r][c]]);
    }
    for (g = 0; g < TABLES_GAP; g++) {
      printf(" ");
    }
    for (c = 0; c < COLS; c++) {
      printf("%c ", symbols[boardC[r][c]]);
    }
    printf("\n");
  }
  printf("Player: %d, computer %d\n", targetsP, targetsC);
  // END: Print final result
  
  return 0;
}