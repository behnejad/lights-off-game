#include "board.h"

Board::Board(int *** map)
{
	//introducing:
	cout << "\t\t\t Hello Dear" << endl
		<< "\t for win the game you must do your best to kill" << endl
		<< "\t for reseting the level type 'reset'" << endl
		<< "\t for reseting the game type 'resetall'" << endl
		<< "\t if you are ready " << endl << "\t " ;
	
	system("pause");
	
	level_ = 0;
	count_ = 0;

	//initializing the curent_level_
	
	curent_level_ = new bool *[5];
	for (int i = 0; i < 5; i++)
	{
		curent_level_[i] = new bool [5];
		for (int j = 0; j < 5; j++)
			curent_level_[i][j] = false;
			
	}

	// initializing the game_level_
	
	game_level_ = new int **[19];
	
	for (int i = 0; i < 19; i++)
		game_level_[i] = new int *[5];

	for (int i = 0; i < 19; i++)
		for (int j = 0; j < 5; j++)
			game_level_[i][j] = new int [5];

	for (int i = 0; i < 19; i++)
		for (int j = 0; j < 5; j++)
			for (int k = 0; k < 5; k++)
				game_level_[i][j][k] = map[i][j][k];
				
	update_level(0);

	/*
	curent_level_ = new bool *[5];
	for (int i = 0; i < 5 ; i++)
	{
		curent_level_[i] = new bool [5];
		for (int j = 0; j < 5; j++) // for initializing curent_level_ default all boxs are on or light
			curent_level_[i][j] = true;
	}
	*/
}//end of function

void Board::show_board()
{
	//system("cls"); // for clearing the consol
	cout << "level : " << level_ + 1 << endl;
	cout << "   _________________________ " << endl
		 << "  |  _    _    _    _    _  |" << endl;
	for (int i = 0; i < 5; i++)
	{
		cout << i+1 << " | ";
		for (int j = 0; j < 5; j++)
		{
			cout << (curent_level_[i][j] ? "|O|" : "| |" );
			cout << (j != 4 ? "  " : " |" );
		}//end of inner for
		if (i != 4)
			cout << endl << "  |  _    _    _    _    _  |" << endl;
		else
			cout << endl;
	}//end of main for
	cout << "   ------------------------- " << endl
		 << "     A    B    C    D    E   " << endl << endl;
}//end of function

int Board::end_game()
{
	bool end = true;
	//if all the boxs are "X" or 0 means the level has been complete
	for (int i = 0; i < 5 ; i++)
		for (int j = 0; j < 5; j++) 
			if(curent_level_[i][j])
				end = false;
	
	if (end && level_ != 18)
	{
		cout << "--------------- you pass level " << level_ + 1 << "---------------" << endl;
		level_ += 1;
		cout << "\a";
		update_level(level_);

		return 1;
	}//end of if
	else if (end && level_ == 18)
	{
		cout << "WOW you win with " << count_ << "moves" << endl;
		return 0;
	}
	else
		return 1;
}//end of function

void Board::update_board(int i, int j)
{
	curent_level_[i][j] = !curent_level_[i][j]; // for changing the light attribute
	if (i - 1 >= 0 ){ curent_level_[i - 1][j] = !curent_level_[i - 1][j];} // if it has upper light
	if (i + 1 <= 4 ){ curent_level_[i + 1][j] = !curent_level_[i + 1][j];} // if it has blow light
	if (j - 1 >= 0 ){ curent_level_[i][j - 1] = !curent_level_[i][j - 1];} // if it has left light
	if (j + 1 <= 4 ){ curent_level_[i][j + 1] = !curent_level_[i][j + 1];} // if it has right light
}// end of function

void Board::get_move(string a)
{
	if (a == "reset")
		update_level(level_);
	else if ( a == "resetall")
	{
		count_ = 0;
		update_level(0);
	}//end of if
	else if (a.length() == 2)
	{
		if ((a[0] >= 'a' && a[0] <= 'e') && (a[1] >= '1' && a[1] <= '5'))
		{
			// a[0] must be one of {a,b,c,d,e} and a[1] must be one of {1,2,3,4,5}
			update_board((int)(a[1] - '1'), (int)(a[0] - 'a'));
			count_ += 1;
		}//end of if
		else if ((a[1] >= 'a' && a[1] <= 'e') && (a[0] >= '1' && a[0] <= '5'))
		{
			// a[1] must be one of {a,b,c,d,e} and a[0] must be one of {1,2,3,4,5}
			update_board((int)(a[0] - '1'), (int)(a[1] - 'a'));
			count_ += 1;
		}// end of if
		else
		{
			cout << "unillegal move" << endl;
			count_ += 1;
		}//end of else
	}//end of outer if
	else
	{
		cout << "insert the correct position" << endl;
	}//end of else
}//end of function

void Board::update_level(int a)
{
	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 5; j++)
			if (game_level_[a][i][j])
				curent_level_[i][j] = true;

}//end of function

/*
const int Board::level_ [19][5][5] = {
		{
			{0,0,0,0,0},
			{0,0,1,0,0},
			{0,1,1,1,0},
			{0,0,1,0,0},
			{0,0,0,0,0}
		},
		{
			{1,1,0,1,1},
			{1,0,0,0,1},
			{0,0,0,0,0},
			{1,0,0,0,1},
			{1,1,0,1,1}
		},
		{
			{0,0,1,0,0},
			{0,1,1,1,0},
			{0,0,0,0,0},
			{0,1,1,1,0},
			{0,0,1,0,0}
		},
		{
			{0,1,1,1,0},
			{0,1,0,1,0},
			{1,0,1,0,1},
			{0,1,0,1,0},
			{0,1,1,1,0}
		},
		{
			{0,1,1,1,0},
			{1,0,0,0,1},
			{1,0,1,0,1},
			{1,0,0,0,1},
			{0,1,1,1,0}
		},
		{
			{0,1,0,1,0},
			{1,1,1,1,1},
			{0,1,1,1,0},
			{1,1,1,1,1},
			{0,1,0,1,0}
		},
		{
			{0,0,1,0,0},
			{0,1,1,1,0},
			{0,1,1,1,0},
			{1,1,1,1,1},
			{0,0,1,0,0}
		},
		{
			{1,1,1,1,1},
			{0,0,1,0,0},
			{0,0,0,0,0},
			{0,0,1,0,0},
			{1,1,1,1,1}
		},
		{
			{1,1,1,1,1},
			{1,1,0,0,1},
			{1,1,0,0,1},
			{0,0,1,1,1},
			{1,0,1,1,1}
		},
		{
			{1,1,1,0,0},
			{0,0,0,0,1},
			{1,1,1,1,1},
			{0,0,0,0,1},
			{1,1,1,0,0}
		},
		{
			{0,0,0,1,0},
			{0,0,0,1,0},
			{0,1,1,0,0},
			{0,0,1,0,0},
			{0,1,1,1,0}
		},
		{
			{0,1,0,1,0},
			{1,0,0,0,1},
			{0,0,0,0,0},
			{1,0,0,0,1},
			{0,1,0,1,0}
		},
		{
			{1,1,0,0,1},
			{1,0,1,1,0},
			{0,1,0,0,0},
			{0,1,0,1,1},
			{1,0,0,1,0}
		},
		{
			{0,0,0,0,1},
			{0,1,1,1,1},
			{1,0,1,0,1},
			{1,0,1,0,1},
			{0,1,0,0,0}
		},
		{
			{0,0,0,0,0},
			{0,0,0,1,0},
			{0,0,0,1,1},
			{0,1,0,1,0},
			{0,1,1,0,1}
		},
		{
			{0,1,1,1,0},
			{1,0,0,0,1},
			{0,0,1,0,0},
			{0,0,1,0,0},
			{1,0,0,0,1}
		},
		{
			{1,1,0,1,0},
			{0,0,1,1,0},
			{1,0,0,1,1},
			{0,1,0,1,0},
			{0,1,0,1,0}
		},
		{
			{0,0,0,1,0},
			{1,0,0,1,0},
			{0,0,1,0,0},
			{0,1,0,0,1},
			{0,1,0,0,0}
		},
		{
			{0,0,0,0,0},
			{0,0,0,1,1},
			{0,1,0,0,0},
			{1,0,0,0,1},
			{0,1,1,0,0
			}
		}
		};
		*/