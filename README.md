# River-Crossing-Game

This is a 2 player game. The person with the most points by the end wins the game. Further, if the players decide to continue the game, the points keep adding to the previous scores and if they choose to play again, the score resets to zero and you are taken to instructions screen where you can start the game.

***Controls:***<br/>
The controls for player 1 movement are up, down, left and right arrow keys.<br/>
The controls for player 2 movement are w, s, a and d keys for up, down, left and right movement respectively.

***Obstacles:***<br/>
Initially there are 5 ships and 5 boats as moving obstacles and 10 rocks as fixed obstacles. As a round completes, 2 fixed obstacles are spawned. The speed of moving obstacles increases for a player if they complete a round.

***Scoring:***<br/>
Players are awarded 5 points for crossing fixed obstacles<br/>
Players are awarded 10 points for crossing moving obstacles<br/>
Further, if the player reaches the finish point, player is awarded more points based on time taken to finish the round.

***Game is ended if:***<br/>
Both the players finish 5 rounds (and/or)<br/>
Both the players crash with an obstacle in the same round


***About the code:***<br/>
The initialization of variables has been done in "configuration.py" file and the main code for the game can be found in "game.py" file. Additional files used i.e. fonts, images and music can be found in the assets folder. Make sure to place the assets folder and configuration file in the same directory as the 'game.py' file before running it.

### Game By:- Shayaan Hussain
