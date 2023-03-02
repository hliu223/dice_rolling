# python
Game set up. 
Before the game starts, the user is asked to choose the number of players 
that are going to play the game and respectively asks the names of each 
player. So, if the user selects 4 players, the game will ask for 4 players’ names 
and saves them, respectively.
After successfully setting up the players, the user is prompted to enter the 
number of rounds the players wish to play. Once this is completed, the game 
starts with an empty scoreboard. An example of a scoreboard is shown below 
but you can produce your own design.
*************************************************************
Name Round 1 Round 2 Round 3 Total
Ali - - - -
Malcolm - - - -
Janet - - - -
Sichuan - - - -
**************************************************************
Playing the game. 
After the game has saved the names of the players and knows how many 
rounds it will be played for, the game starts.
During each round, each player (virtually) rolls two dices and the sum of the 
two dices is saved for each player per round. Players will roll the dices on the 
same order that their names were entered during the set up. Rolling the dices 
is as easy as the following:
The program prints the name of the player that must play and asks them to 
hit enter to roll their dices and the program generates two random numbers
between 1 and 6 for each dice.
After each round 
At the end of each round, the game shows the scoreboard containing each 
player’s scores per round and their respective total scores. An example is 
shown below but again, you do not have to follow the same format. You can 
come up with your own scoreboard format. Get creative!
*********************** End of Round of 2************************
~ Round 1 Round 2 Round 3 Total
Malcolm 2 12 - 14
Janet 3 7 - 10
Sichuan 5 5 - 10
**************************************************************
After the last round
Once the last player has played the last round, the game shows the final 
scoreboard, congratulates the winner, and asks whether the players want to 
player another game. If the players choose to play again, an empty 
scoreboard is displayed and the game starts over.
Specific instructions
Please note that you cannot use third-party libraries in your code. The 
standard python 3 libraries are sufficiently enough to accomplish this 
assignment.
An example of a game with 2 players and three rounds is shown below.
***** Welcome to another Dice Rolling Game *****
Please enter the number of players: 2
Please enter player #1 name: John
Please enter player #2 name: Sarah
Please enter how many rounds the players wish to play: 2
*********************** Round 1************************
~ Round 1 Round 2 Total
John - - -
Sarah - - -
************************************************************
John! Hit enter once you are ready to roll your dices!
1 and 6
Sarah! Hit enter once you are ready to roll your dices!
6 and 6
*********************** End of round 1************************
~ Round 1 Round 2 Total
John 7 - 7
Sarah 12 - 12
************************************************************
John! Hit enter once you are ready to roll your dices!
3 and 6
Sarah! Hit enter once you are ready to roll your dices!
1 and 2
*********************** End of round 2************************
~ Round 1 Round 2 Total
John 7 9 16
Sarah 12 3 15
************************************************************
Congratulations John! You are our WINNER!
Would you like to play another game?
[1] Yes
[2] No
Your choice: 2
Thank you and see you later!
