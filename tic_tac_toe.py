#tictactoe in list representation
v_list=['','','','','','','','','']

#global variables for player 1 and player 2 choice i.e. X or O
pla1=""
pla2=""
#function for players to choose X or O
def choice():
    #gloal variables
    global pla1
    global pla2

    #Player 1 turn to choose
    print("Player 1".center(80,"-"))
    pla1=input("Choose X or O: ")

    #Player 2 default choice if Player 1 chooses
    print("Player 2".center(80,"-"))
    if pla1=="x" or pla1=="X":
        print("Player 1 ---> X\nPlayer 2 ---> O")
        pla2="O"
    elif pla1=="o" or pla1=="O":
        print("Player 1 ---> O\nPlayer 2 ---> X")
        pla2="X"
    else:
        #Player 1 missed chance of choosing, Player 2 turn to choose
        print("Nothing selected by Player 1, Player 2 can choose")
        pla2=input("Choose X or O: ")
        #Player 1 default choice if Player 2 chooses
        if pla2=="x" or pla2=="X":
            print("Player 1".center(80,"-"))
            print("Player 2 ---> X\nPlayer 2 ---> O")
            pla1="O"
        elif pla2=="o" or pla2=="O":
            print("Player 1".center(80,"-"))
            print("Player 2 ---> O\nPlayer 2 ---> X")
            pla1="X"
        else:
            #If both the players don't choose call function again to give more change to players to choose
            print("Nothing selected by Player 2, Player 1 can choose")
            choice()

#printing tictacktoe in matrix form        
def print_tictactoe():
    for i in range(len(v_list)):
        if i%3==0:#go to next line or row if three cells are printed
            print("\n------")
        if v_list[i]=="":
            print(" ",end="|")#If v_list element is empty then print blank space for empty, end="|" for next print to contine on samw line with '|' character seperation
        else:
            print(v_list[i],end="|")#If v_list element is not empty then print the element, end="|" for next print to contine on samw line with '|' character seperation
    print()
    #blank line to print


#Winner function to know if player with X or  O choice has won
#here, val is X or O choice
def Winner(val):
    #global variabless
    global pla1
    global pla2
    print("\n")
    print("".center(80,"*"))
    #if pla1 i.e. player 1 has made val(X or O) choice, he wins otherwise player 2 wins
    if pla1==val:
        
            print("Player 1 wins")
    elif pla2==val:
            print("Player 2 wins")
    print("".center(80,"*"))

def check_win():
    #lists to check the currently filled x and o filled positions in the ticktacktoe
    index_X=[]
    index_O=[]
    #gglobal variable
    global v_list
    #Ieratiing through the main list and searching for positions of  X and O values and apending them in lists
    for i in range(len(v_list)):
        if v_list[i]=="X":
            index_X.append(i)
        elif v_list[i]=="O":
            index_O.append(i)
    #print(v_list)
    #print("index_o",index_O)
    #print("index_x",index_X)

    #Chechking if X made a winning pattern
    for i in index_X:
            #Checking rows
            #E.g. 0,1,2 or 3,4,5 or 6,7,8
            if i==3 or i==0 or i==6:
                if i+1 in index_X:#next value
                    if i+2 in index_X:#next value
                        print_tictactoe()#print tictacktoe in matrix form
                        Winner("X")#Find winner if Player 1 or 2 by calling WInning function with X, as player with X choice has won
                        
                        return(True)#return true
            
            
           
            if i==2 or i==0 or i==1:

                if i+3 in index_X:#vertical
                    if i+6 in index_X:
                        print_tictactoe()#print tictacktoe in matrix form
                        Winner("X")
                        
                        return(True)
           
            if i==2:
                if 4 in index_X and 6 in index_X:#diagonal with 0
                    print_tictactoe()#print tictacktoe in matrix form
                    Winner("X")
                    
                    return(True)
            if i==0:
                if 4 in index_X and 8 in index_X:#diagonal with 2
                    print_tictactoe()#print tictacktoe in matrix form
                    Winner("X")
                    return(True)
            

            
    for i in index_O:
            if i==3 or i==0 or i==6:
                if i+1 in index_O:#horzontal
                    if i+2 in index_O:
                        print_tictactoe()#print tictacktoe in matrix form
                        Winner("O")
                        return(True)
            
            
           
            if i==2 or i==0 or i==1:

                if i+3 in index_O:#vertical
                    if i+6 in index_O:
                        print_tictactoe()#print tictacktoe in matrix form
                        Winner("O")
                        return(True)
           
            if i==2:
                if 4 in index_O and 6 in index_O:#diagonal with 0
                    print_tictactoe()#print tictacktoe in matrix form
                    Winner("O")
                   
                    return(True)
            if i==0:
                if 4 in index_O and 8 in index_O:#diagonal with 2
                    print_tictactoe()#print tictacktoe in matrix form
                    Winner("O")
                    return(True)
            
            


    
print("\nStarting game.........\n")
    
choice()



for i in range(1,10):
    if i%2==0:#even player 2 chance
        print("Player 2 Chance".center(80,"-"))
        while True:
            pla2_index=int(input("Enter any position from [1-9] : "))
            if pla2_index<=0 or pla2_index>9:
                print("Please enter appropriate value for position")
            else:
                if v_list[pla2_index-1]!="":
                    print("Spot already filled by Player 1, choose another spot")
                else:
                    v_list[pla2_index-1]=pla2
                    break
            
        if check_win():
            
            break
    else:#odd player 1 chance
        print("Player 1 Chance".center(80,"-"))
        
        while True:
            pla1_index=int(input("Enter any position from [1-9] : "))
            if pla1_index<=0 or pla1_index>9:
                print("Please enter appropriate value for position")
            else:
                if v_list[pla1_index-1]!="":
                    print("Spot already filled by Player 2, choose another spot")
                else:
                    v_list[pla1_index-1]=pla1
                    break
          
                
                
        if check_win():
            
            break
    print_tictactoe()
else:
    print("\n")
    print("".center(80,"*"))
    print("Match Draw.......................")
    print("".center(80,"*"))










