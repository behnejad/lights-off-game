#ifndef BOARD_H
#define BOARD_H

#include <iostream>
#include <string>

using namespace std;

class Board
{
private:
	bool ** curent_level_; //it shows which light is on and off, if it false means the light is off
	int level_; //it show the number of level
	int count_; //for counting how many move does it take to win
	int *** game_level_ ;

public:
	Board(int ***); // initialize the lightbox
	void show_board(); // this use for show the lightbox
	int end_game(); // return 1 while the game continues, return 0 if all level has finished
	void update_board(int, int); // this function change the board by position(i, j)
	void get_move(string); // this will be get the string like "e3" or "3e" and call update_board for changes
	void update_level(int); // this will get the 3D array and level from level_ and create the curent_level_

};

#endif