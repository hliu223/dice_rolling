def game():
    import random
    # first module: get players' number and make two empty lists. listOfName is going to be the first element list in listOfPlayers which is going to be 2d list 
    print("***********************Welcome to another Dice Rolling Game****************************")
    numberOfPlayers = int(input("Please enter the number of players:")) # ask user how many players
    listOfName = ["Name"] # put Name at first, because "name" is unchangeable 
    listOfPlayers = []
    for i in range (1,numberOfPlayers + 1):                                 # ask players to enter the name of each player and add them to the list named listOfPlayers
        contentOfAskPlayer = "Please player #" + str(i) + " name:"
        player = input(contentOfAskPlayer)
        listOfName.append(player) # add each player's name to the listOfName list
    numberOfRounds = int(input("Please enter how many rounds players wish to play: "))# ask how many rounds
    Columns = numberOfPlayers + 1       # Once got the number of rounds, a 2d list could be created 
    rows = numberOfRounds + 2
    '''
    The list should be like this: assume there are two players and two rounds
    [[name,playerName1,playerName2],
    [round1,"-","-"],
    [round2,"-","-"],
    [Total,"-","-"]]
    so, the 2d list has numberofplayers + 1 colums and numberOfRound + 2 rows.(name and total) 
    '''
    for i in range(0,rows):
        row = ["-"] * Columns
        listOfPlayers.append(row)  # The list store every data has been created.
    listOfPlayers[0] = listOfName  # put listofname to the first element list in listofplayers
    for i in range (1,numberOfRounds + 1):
            i = str(i)             # make number str
            listOfPlayers[int(i)][0] = ("round" + i)    # conbine round and the number of round to the listOfplayers list
    listOfPlayers[-1][0] = "Total"   # the first element in the last list element in listOfPlayers should always be Total
    #print(listOfPlayers)
    # Next module(line 32 - line 42) is in charge of printing the first scoreboard that only has name and round total without scores
    print("********************************************round 1***********************************************" )  
    # Before print listOfPlayers(contain everything), must change the sequence of index. index of rows change to index of columns
    listOfPrint = []
    for i in range(len(listOfPlayers[0])):
        Temp = []
        for j in range(len(listOfPlayers)):
            Temp.append(listOfPlayers[j][i])
        listOfPrint.append(Temp)
    #print the listOfPrint
    for r in listOfPrint:
        for c in r:
            print("\t",c,end="      ") 
        print("\n")
    print("*************************************************************************************************" )
    # This module(46-55) is in charge of adding every score of round to the listOfPlayers
    a = 0                                #set a initial value for the while loop
    while a < numberOfRounds:
        for i in range (1,len(listOfPlayers[0])):
            if input(str(listOfPlayers[0][i]) + "! Hit enter once you are ready to roll your dices!") == '':
                number1 = random.randint(1,6)               # generate random numbers
                number2 = random.randint(1,6)
                print(number1," and ",number2)
                numberTotal = number1 + number2            #calculate total number of each round
                listOfPlayers[a + 1][i] = numberTotal      # insert each numberTotal into listOfPlayers for each round 
    #This module(56-67) is in charge of adding the total number of each player
        j = 1
        total = 0
        while j <= numberOfPlayers:
            for x in range(1,numberOfRounds + 1):
                #listTemp = []
                if type(listOfPlayers[x][j]) == int:            #some are "-"
                    #listTemp.append(listOfPlayers[x][j])
                    total = listOfPlayers[x][j] + total
                listOfPlayers[-1][j] = total                 # put the result into the Total element in listOfplayers
            total = 0      # refresh total and make it ready for the next total
            j = j + 1
        print("*************************************end of round",a+1,"*************************************************" )
        # play the same role like line 34-44
        listOfPrint = []
        for i in range(len(listOfPlayers[0])):
            Temp = []
            for j in range(len(listOfPlayers)):
                Temp.append(listOfPlayers[j][i])
            listOfPrint.append(Temp)
        for r in listOfPrint:
            for c in r:
                print("\t",c,end="      ") 
            print("\n")
        print("*******************************************************************************************************" )
        a = a + 1
    # this module (line 83-88) is in charge of getting the winner of this game and print it
    listOfContainer = []
    for z in range(1,len(listOfPlayers[-1])):
        listOfContainer.append(listOfPlayers[-1][z])               # put the total number of all players into the container list
    for h in range(0,len(listOfContainer)):
        if listOfContainer[h] == max(listOfContainer):             # loop total number and get the max one to use the index of column to print who is the winner
            print("Congratulations ",listOfPlayers[0][h + 1],"! You are the winner of this game!!!")
    #This module is in charge of asking player if restart this game
playAgain = "1"                                #set a var for the while loop
while playAgain == "1":
    game()
    playAgain = input("Would you like to play this game again?\n[1] yes \n[2] no \nEnter your choice:")
    if playAgain == "1":                                # once users enter 1, this game will be restarted
        continue
    elif playAgain == "2":                             #enter 2,  print thank you and jump out of this loop
        print("Thank you and see you later!")
        break