



"""    ---------Project 2048-----------
                Amir Mustefa-----ATR/6830/09
                                               """
## 1. Generate two numbers of value 2 in random cells
## 2. Print_table function
## 3. Accept input of Next Move from the player
## 4. Merge_table function
##      a. Single Merge function --- works only for left direction.
##      b. Single Merge for all direction fuction that works in all directions.
##      c. Double Merge function
##         A. Transpose function which makes the single-merge function work for column-wise.
## 5. Generate one number of value either 2 or 4 in random cell of merged table.
## 6. Check if Game is over function
## 7. Check if You've won the game


## Check your play function -- it generates random numbers in repeated identical moves.
## Check Game over function
## How do I terminate or restart in the middle of the game.
## Already started the exit method

import random
def print_table(matrice):
    """ Prints matrice in table format."""
    for i in range(4):
        for j in range(4):
            print(format(matrice[i][j],"6d"),end="")
        print()
        
def single_merge(L):
    """Merges the given length-4 list after a next move is taken by player"""
    final_row=[]
    i=0
    for j in range(1,4):
        if L[i]==L[j] and L[i]!=0:
            L[i]=(L[i]+L[j])  ###added
            i+=1
            L[j]=0
        elif L[i]==L[j] and L[i]==0:
            continue
        elif L[i]!=L[j] and L[i]==0:
            L[i]=L[j]
            L[j]=0
        elif L[i]!=L[j] and L[j]==0:
            continue
        elif L[i]!=L[j] and L[i]!=0 and L[j]!=0:
            temp=L[j]
            L[j]=0   ###added
            L[i+1]=temp  ##added
            i+=1
    while len(final_row)<4:###simply change length of L if you want an extension of function to longer lists.
        final_row.append(0)
    return L

def single_merge_all_direction(L,direction):
    if direction=="a" or direction=="w":
        return single_merge(L)
    elif direction=="d" or direction=="s":
        L.reverse()
        temp_list=L
        final_list=single_merge(temp_list)
        final_list.reverse()
        return final_list

def Transpose(matrice): ### Matrice means the whole 4*4 multidimensional list
    """Returns the Transpose of a given multi-dimensional array"""
    returned_matrice=[]
    for j in range(4):
        L=[]
        for i in range(4):
            L.append(matrice[i][j])
        returned_matrice.append(L)
    return returned_matrice
          
 
 
    
def double_merge(matrice,direction):
    """Merges the whole multi-dimensional list in the given direction"""
    if direction=="w" or direction=="s":
        temp_matrice=Transpose(matrice)
    elif direction=="a" or direction=="d":
        temp_matrice=matrice
    empty_matrice=[]
    for rows in temp_matrice:
        empty_matrice.append(single_merge_all_direction(rows,direction))
    if direction=="w" or direction=="s":
        return Transpose(empty_matrice)
    else: return empty_matrice

def generate_random_numbers_in(L):
    """It appends onto the given list a randomly generated number of value
of either two or four in a random zero cell(empty cell)."""
    i=random.randint(0,3)
    j=random.randint(0,3)
    while L[i][j]!=0:
        i=random.randint(0,3)
        j=random.randint(0,3)
    L[i][j]=random.choice([2,4])
    return L

def generate_first_random_number():
    """Generates the table(multi-dimensional list) along with the randomly
positioned two values of 2."""
    matrice=[]
    for i in range(4):
        row=[]
        for j in range(4):
            row.append(0)
        matrice.append(row)
    a=random.randint(0,3)
    b=random.randint(0,3)
    ###### Choose first random cell
    c=random.randint(0,3)
    d=random.randint(0,3)
    ##### Choose second random cell
    matrice[a][b]=2
    while (a,b)==(c,d):
        c=random.randint(0,3)
        d=random.randint(0,3)
    #### Make sure the random cells chosen are not the same
    matrice[c][d]=2
    return matrice

def isGameOver(matrice):
    """Takes a multi-dimensional array and checks if it's in a game-over state
:It checks if all the cells have been occupied by a non-zero number"""
    occupied_cell=0
    for rows in range(4):
        for columns in range(4):
            if matrice[rows][columns]==0:
                break
            else:occupied_cell+=1
    if occupied_cell==16:
        return True
    else:return False

def isWin(matrice):
    """Takes a multi-dimensional array and checks if it's in a win state
:It checks if all the cells have been occupied by a non-zero number"""
    iswin="no"
    for rows in range(4):
        for columns in range(4):
            if matrice[rows][columns]==2048:
                iswin="yes"
                break
            else:continue
    if iswin=="yes":
        return True
    else: return False

def accept_direction_input():
    """It request for an input from the user and saves it as directon.
     Accepts 'n' as instruction to exit."""
    direction=str(input("Please enter your next move ('w','a','s','d'): "))
    if direction not in ['w','a','s','d','n']:
        print("Invalid move:")
        return accept_direction_input()
    return direction

def is_equal_to(M,L):
    num_of_equal=0
    for i in range(4):
        for j in range(4):
            if M[i][j]==L[i][j]:
                num_of_equal+=1
                continue
            else:return False
    if num_of_equal==16:
        return True
    else: return False
            
def play():
    """Starts the game. Equivalent of main function."""
    matrice2=generate_first_random_number()
    print_table(matrice2)
    while not isWin(matrice2) or isGameOver(matrice2):
        direction=accept_direction_input()
        if direction=="n":
            break
        else:
            matrice=matrice2
            matrice2=double_merge(matrice2,direction)
            if is_equal_to(matrice2,matrice)==False:
                matrice2=generate_random_numbers_in(matrice2)
            else:matrice2=matrice2
            print_table(matrice2)
    if isWin(matrice2):
        print("You Win")
    elif isGameOver(matrice2):
        print("Game Over, You Lose!!!")
    choice=str(input("Wanna play Again 'y'/'n'"))
    if choice=="y":
        return play()
    else:print("Bye Bye!")



    



    
                            
    

