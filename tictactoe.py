def playerIntro(a):
    print(f'\nPlayer {a}, please enter your name: ')
    p=input('')
    print(f"Hello {p}! Welcome to Tic Tac Toe!")
    return p
def showGrid(grid):
    print("   1     2     3\n")
    for i in range(3):
        print(i+1,end='')
        for j in range(3):
            if (grid[i][j]!='X' and grid[i][j]!='O'):
                print("   ",end='')
            else:
                print(' ',grid[i][j],end='')
            if (j==0 or j==1):
                print('  |',end='')
        if(i!=2):
            print('\n  ----------------')
def checkWinner(grid,row,col):
   if grid[row][0]==grid[row][1] and grid[row][1]==grid[row][2]:
       return 1
   elif grid[0][col]==grid[1][col] and grid[1][col]==grid[2][col]:
       return 1
   elif row==col:
       if grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2]:
           return 1
       elif grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0]:
           return 1
   else:
       return 0
def game():
    print('This is a multiplayer game. There are two players: Player 1 and Player 2. ')
    ch=1
    while(ch!=2): #if the player wants to stay in the application but does not want to leave the game, the player exists the current game but still stays in the application
       ch=int(input("\n\nMenu:\n1.Start a new game\n2.Exit the game\n\nChoose your option: "))
       grid=[[2,3,4],[5,6,7],[8,9,10]]
       leave=0 #leaves the current game
       #win=0
       while(leave!=1):
           p1=playerIntro(1)
           p2=playerIntro(2)
           m1=(input(f'\n{p1}, please enter 1 to choose "X" or enter 2 to choose "O". Any other entry would automatically generate a symbol for you!: '))
           if(m1!='2'):
               m1='X'
               m2='O'
               print(f"{p1} plays with 'X'!\n{p2}, you automatically play with O!")
           else: 
               m1='O'
               m2='X'
               print(f"{p1} plays with 'O'!\n{p2}, you automatically play with X!")
           
           print('The game is starting now!')
           for i in range(9):
               if(i%2==0):
                   print(f'{p1}, it is now your turn!')
                   showGrid(grid)
                   print('\nThis is how the grid looks.')
                   lo=0
                   while(lo!=1):
                       row=int(input(f"Enter the row where you would like to place {m1}: "))
                       col=int(input(f"Enter the column where you would like to place {m1}: "))
                       if(grid[row-1][col-1]!='X' and grid[row-1][col-1]!='O'):
                           grid[row-1][col-1]=m1
                           lo=1
                       else: 
                           print('There already exists an icon there! Try again!')
                   if checkWinner(grid,row-1,col-1):
                       print(f"Congratulations {p1}, you have won the game!!")
                       return 
               else:
                    print(f'\n\n{p2}, it is now your turn!')
                    showGrid(grid)
                    print('\nThis is how the grid looks.')
                    lo=0
                    while(lo!=1):
                        row=int(input(f"Enter the row where you would like to place {m2}: "))
                        col=int(input(f"Enter the column where you would like to place {m2}: "))

                        if(grid[row-1][col-1]!='X' and grid[row-1][col-1]!='O'):
                            grid[row-1][col-1]=m2
                            lo=1
                        else: 
                            print('There already exists an icon there! Try again!')
                    if checkWinner(grid,row-1,col-1):
                        print(f"Congratulations {p2}, you have won the game!!")
                        return 
               print("\nIcon placed!\n")
               showGrid(grid)
               print()
               if i==9:
                   print("The game has come to a draw!")
                   leave=1
       print("You have chosen to exit the game.")
    print("Goodbye!")
        
game()
