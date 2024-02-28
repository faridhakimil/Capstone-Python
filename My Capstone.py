# ============================================================ DICTIONARY
arsenalTeam     = {
     1001   : [ 'Aaron Ramsdale'     , 'GK' , 25,  28000000],
     1022   : [ 'David Raya'         , 'GK' , 28,  35000000],
     1002   : [ 'William Saliba'     , 'CB' , 22,  75000000],
     1006   : [ 'Gabriel Magalhaes'  , 'CB' , 26,  60000000],
     1035   : [ 'Oleksandr Zinchenko', 'LB' , 27,  42000000],  
     1004   : [ 'Ben White'          , 'RB' , 26,  55000000],
     1041   : [ 'Declan Rice'        , 'DMF', 25, 110000000],
     1020   : [ 'Jorginho'           , 'DMF', 32,  15000000],
     1029   : [ 'Kai Havertz'        , 'AMF', 24,  55000000],        
     1008   : [ 'Martin Odegaard'    , 'AMF', 25,  90000000],
     1007   : [ 'Bukayo Saka'        , 'RW' , 22, 120000000],
     1011   : [ 'Gabriel Martinelli' , 'LW' , 22,  85000000],
     1019   : [ 'Leandro Trossard'   , 'LW' , 29,  38000000],
     1009   : [ 'Gabriel Jesus'      , 'CF' , 26,  70000000],
     1014   : [ 'Eddie Nketiah'      , 'CF' , 24,  35000000]}

arsenalReserve  = {
     1015   : [ 'Jacub Kiwior'       , 'CB' , 24,  25000000],
     1018   : [ 'Takehiro Tomiyasu'  , 'RB' , 25,  30000000],
     1005   : [ 'Thomas Partey'      , 'DMF', 30,  25000000],
     1021   : [ 'Fabio Vieira'       , 'AMF', 23,  28000000], 
     1010   : [ 'Emile Smith Rowie'  , 'AMF', 23,  25000000],  
     1024   : [ 'Reiss Nelson'       , 'RB' , 24,  15000000]}

arsenalAll     = {
    1001   : [ 'Aaron Ramsdale'     , 'GK' , 25,  28000000],
     1022   : [ 'David Raya'         , 'GK' , 28,  35000000],
     1002   : [ 'William Saliba'     , 'CB' , 22,  75000000],
     1006   : [ 'Gabriel Magalhaes'  , 'CB' , 26,  60000000],
     1035   : [ 'Oleksandr Zinchenko', 'LB' , 27,  42000000],  
     1004   : [ 'Ben White'          , 'RB' , 26,  55000000],
     1041   : [ 'Declan Rice'        , 'DMF', 25, 110000000],
     1020   : [ 'Jorginho'           , 'DMF', 32,  15000000],
     1029   : [ 'Kai Havertz'        , 'AMF', 24,  55000000],        
     1008   : [ 'Martin Odegaard'    , 'AMF', 25,  90000000],
     1007   : [ 'Bukayo Saka'        , 'RW' , 22, 120000000],
     1011   : [ 'Gabriel Martinelli' , 'LW' , 22,  85000000],
     1019   : [ 'Leandro Trossard'   , 'LW' , 29,  38000000],
     1009   : [ 'Gabriel Jesus'      , 'CF' , 26,  70000000],
     1014   : [ 'Eddie Nketiah'      , 'CF' , 24,  35000000],
     1015   : [ 'Jacub Kiwior'       , 'CB' , 24,  25000000],
     1018   : [ 'Takehiro Tomiyasu'  , 'RB' , 25,  30000000],
     1005   : [ 'Thomas Partey'      , 'DMF', 30,  25000000],
     1021   : [ 'Fabio Vieira'       , 'AMF', 23,  28000000], 
     1010   : [ 'Emile Smith Rowie'  , 'AMF', 23,  25000000],  
     1024   : [ 'Reiss Nelson'       , 'RB' , 24,  15000000]
     }

playerListed    = {
     1003   : [ 'Harry Kane'         , 'CF' , 30, 110000000],
     1016   : [ 'Jude Bellingham'    , 'AMF', 20, 180000000],
     1020   : [ 'Jorginho'           , 'DMF', 32,  15000000],
     1013   : [ 'Moises Caicedo'     , 'DMF', 21, 116000000],
     1012   : [ 'Rasmus Hojlund'     , 'CF' , 20,  34000000],
     1029   : [ 'Kai Havertz'        , 'AMF', 24,  55000000],
     1017   : [ 'Alexis Mac Allister', 'CMF', 24,  65000000],
     1014   : [ 'Eddie Nketiah      ', 'CF' , 24,  35000000]}

playersInNew    = {}

playerscreate   = {}

playersOut      = {}

playersRetire   = {}

listFinance = [
        ['Balance'                  , 5000000000],
        ['transferBudgetSeason'     , 1000000000],
        ['transferBudgetRemaining'  , 1000000000],
        ['loansOutstanding'         , 2100000000],
        ['totalwagebudget'          ,     700000],
        ['currentwagetotal'         ,     500000]]

macamYes        = ["yes", "ya", "y"]
macamNo         = ["no", "n"]

# ============================================================ SUB MENU 1
def arsenal_Team():
    print('\t\t\t   ARSENAL ')
    print('\t\t Player List - General Info :\n')
    print('Index\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
    for a,b in enumerate(arsenalTeam):
        print (f'  {a}\t|  {b} | {arsenalTeam[b][0].ljust(15)}\t|  {arsenalTeam[b][1]}\t| {arsenalTeam[b][2]}  | {arsenalTeam[b][3]:,}')

def sureUnsureMoveR():
    while True:
        sure = input("\n    Are you sure you want to move the player 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_Team()
            submenu_1()
        else:
            print('Choice Correctly !')
            pagar()

def arsenaltoReserve():
    while True:
        try:
            arsenal_Team()
            choice_1a   = input("\n\tInsert the players number you want to move : ")
            if  choice_1a.isdigit() == True:
                choice_1a = int(choice_1a)
            if int(choice_1a) in arsenalTeam:
                a = arsenalTeam[choice_1a]
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_1a} | {arsenalTeam[choice_1a][0].ljust(15)}\t|  {arsenalTeam[choice_1a][1]}\t| {arsenalTeam[choice_1a][2]}  | {arsenalTeam[choice_1a][3]:,}')
                sureUnsureMoveR()
                arsenalReserve[choice_1a] = a
                del arsenalTeam[choice_1a]
                arsenal_Team()
                submenu_1()
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
                pagar()
        except ValueError:
            arsenaltoReserve()

def sureUnsureSetA():
    while True:
        sure = input("\nAre you sure you want to set the players status 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_Team()
            submenu_1()
        else:
            print('\t\t\tChoice Correctly !')
            pagar()

def arsenaltoListed():
    while True:
        try:
            arsenal_Team()
            choice_1b   = input("\n\tInsert the players number you want to set status : ")
            if  choice_1b.isdigit() == True:
                choice_1b = int(choice_1b)
            if int(choice_1b) in arsenalTeam:
                a = arsenalTeam[choice_1b]
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_1b} | {arsenalTeam[choice_1b][0].ljust(15)}\t|  {arsenalTeam[choice_1b][1]}\t| {arsenalTeam[choice_1b][2]}  | {arsenalTeam[choice_1b][3]:,}')
                sureUnsureSetA()
                playerListed[choice_1b] = a
                player_Listed()
                print()
                arsenal_Team()
                submenu_1()
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\n\t\t   Insert Correctly !!")
                pagar()
        except ValueError:
            arsenaltoListed()
 
def sureUnsureExitA():
    while True:
        sure = input("\nAre you sure you want to exit 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t ~~ DONE, Arigatou Gozaimasu ~~")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_Team()
            submenu_1()
            pass
        else:
            print('\n\t\tInsert Correctly !')

def title_1():
    print('''
                --  Manager Instruction  --
            
                    Arsenal :
                    1. Move to Arsenal Reserve
                    2. Set Transfer Status
                    3. Back to Home
                    4. Quit Game
    ''')

def submenu_1():
    while True:
        title_1()
        choice_1 = input('\t\t Please insert your choice : ')
        pagar()
        if  choice_1.isdigit() == True and 1 <= int(choice_1) <= 4:
            choice_1 = int(choice_1)
        if  choice_1 == 1:
            arsenaltoReserve()
        elif choice_1 == 2:
            arsenaltoListed()
        elif choice_1 == 3:
            home()
        elif choice_1 == 4:
            sureUnsureExitA()
            exit()
        else:
            print('\t\t\tChoice Correctly !')
            pagar()

# ============================================================ SUB MENU 2

def arsenal_Reserve():
    print('\n\t\t      ARSENAL RESERVE')
    print('\t\t Player List - General Info :\n')
    print('Index\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
    for a,b in enumerate(arsenalReserve):
        print (f'  {a}\t|  {b} | {arsenalReserve[b][0].ljust(15)}\t|  {arsenalReserve[b][1]}\t| {arsenalReserve[b][2]}  | {arsenalReserve[b][3]:,}')

def sureUnsureMoveA():
    while True:
        sure = input("\n    Are you sure you want to move the player 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_Reserve()
            submenu_2()
        else:
            print('Choice Correctly !')
            pagar()

def reservetoArsenal():
    while True:
        try:
            arsenal_Reserve()
            choice_2a   = input("\nInsert the players number you want to move : ")
            if  choice_2a.isdigit() == True:
                choice_2a = int(choice_2a)
            if int(choice_2a) in arsenalReserve:
                a = arsenalReserve[choice_2a]
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_2a} | {arsenalReserve[choice_2a][0].ljust(15)}\t|  {arsenalReserve[choice_2a][1]}\t| {arsenalReserve[choice_2a][2]}  | {arsenalReserve[choice_2a][3]:,}')
                sureUnsureMoveA()
                arsenalTeam[choice_2a] = a
                del arsenalReserve[choice_2a]
                arsenal_Reserve()
                arsenal_Team()
                submenu_2()
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
                pagar()
        except ValueError:
            reservetoArsenal()

def sureUnsureSetR():
    while True:
        sure = input("\nAre you sure you want to set the players status 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_Reserve()
            submenu_2()
        else:
            print('Choice Correctly !')
            sureUnsureSetR()

def reservetoListed():
    while True:
        try:
            arsenal_Reserve()
            choice_2b   = input("\nInsert the players number you want to set status : ")
            if  choice_2b.isdigit() == True:
                choice_2b = int(choice_2b)
            if int(choice_2b) in arsenalReserve:
                a = arsenalReserve[choice_2b]
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_2b} | {arsenalReserve[choice_2b][0].ljust(15)}\t|  {arsenalReserve[choice_2b][1]}\t| {arsenalReserve[choice_2b][2]}  | {arsenalReserve[choice_2b][3]:,}')
                sureUnsureSetR()
                playerListed[choice_2b] = a
                player_Listed()
                print()
                arsenal_Reserve()
                submenu_2()
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
                pagar()
        except ValueError:
            reservetoListed()

def sureUnsureExitR():
    while True:
        sure = input("\nAre you sure you want to exit 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t ~~ DONE, Arigatou Gozaimasu ~~")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_Reserve()
            submenu_2()
            pass
        else:
            print('\n\t\tInsert Correctly !')

def title_2():
    print('''
                --  Manager Instruction  --
            
                    Arsenal Reserve :
                    1. Move to Arsenal
                    2. Set Transfer Status
                    3. Back to Home
                    4. Quit Game
    ''')

def submenu_2():
    while True:
        title_2()
        choice_2 = input('\t\t Please insert your choice : ')
        pagar()
        if  choice_2.isdigit() == True and 1 <= int(choice_2) <= 4:
            choice_2 = int(choice_2)
        if  choice_2 == 1:
            reservetoArsenal()
        elif choice_2 == 2:
            reservetoListed()
        elif choice_2 == 3:
            home()
        elif choice_2 == 4:
            sureUnsureExitR()
            exit()
        else:
            print('Choice Correctly !')
            pagar()
            submenu_2

# ============================================================ SUB MENU 3
def sureUnsureExitF():
    while True:
        sure = input("\nAre you sure you want to exit 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t ~~ DONE, Arigatou Gozaimasu ~~")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            submenu_3()
            pass
        else:
            print('\n\t\tInsert Correctly !')

def title_3():
    print(f'''
                        --  Arsenal Finances  --
            
            Finances Summary :
            Balance                     : {listFinance[0][1]:,}
            Transfer Budget (Season)    : {listFinance[1][1]:,}
            Transfer Budget (Remaining) : {listFinance[2][1]:,}
            Loans Outstanding           : {listFinance[3][1]:,}      
            Total Wage Budget           : {listFinance[4][1]:,}
            Current Wage Total          : {listFinance[5][1]:,}
    
            
                        --  Manager Instruction  --
            
                            Arsenal Reserve :
                            1. Back to Home
                            2. Quit Game      
    ''')

def finance1():
        print(f'''
                        --  Arsenal Finances  --
                
                Finances Summary :
                Balance                     : {listFinance[0][1]:,}
                Transfer Budget (Season)    : {listFinance[1][1]:,}
                Transfer Budget (Remaining) : {listFinance[2][1]:,}
                Loans Outstanding           : {listFinance[3][1]:,}      
                Total Wage Budget           : {listFinance[4][1]:,}
                Current Wage Total          : {listFinance[5][1]:,}
    ''')

def submenu_3():
    while True:
        title_3()
        choice_3 = input('\t\t Please insert your choice : ')
        pagar()
        if  choice_3.isdigit() == True and 1 <= int(choice_3) <= 2:
            choice_3 = int(choice_3)
        if  choice_3 == 1:
            home()
        elif choice_3 == 2:
            sureUnsureExitF()
            exit()
        else:
            print('Choice Correctly !')
            pagar()
            submenu_3

# ============================================================ SUB MENU 4
def player_Listed():
    print('\t\t      LISTED PLAYER')
    print('\t\t Player List - General Info :\n')
    print('Index\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
    for a,b in enumerate(playerListed):
        print (f'  {a}\t|  {b} | {playerListed[b][0].ljust(15)}\t|  {playerListed[b][1]}\t| {playerListed[b][2]}  | {playerListed[b][3]:,}')

def sureUnsureTrans():
    while True:
        sure = input("\n    Are you sure you want to buy this players 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            player_Listed()
            submenu_4()
        else:
            print('Choice Correctly !')

def buyPlayers():
    while True:
        try:
            player_Listed()
            choice_4a   = input("\nInsert the players number you want to buy : ")
            if  choice_4a.isdigit() == True :
                choice_4a = int(choice_4a)
            if int(choice_4a) in playerListed and int(choice_4a) in arsenalAll:
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_4a} | {playerListed[choice_4a][0].ljust(15)}\t|  {playerListed[choice_4a][1]}\t| {playerListed[choice_4a][2]}  | {playerListed[choice_4a][3]:,}')
                print('\n\t\t-- Transfer unavailable for this player ! --')
                print('\n\t\t   -- Players name is Arsenal players --')
                pagar()
                continue
            choice_4b   = input("\nInsert fee transfer to make offer : ")
            if int(choice_4a) in playerListed and choice_4b.isdigit() == True:
                choice_4b = int(choice_4b)
                b = playerListed[choice_4a]
                if playerListed[choice_4a][3] > (listFinance[2][1]) :
                    print(f'\n-- sorry, you dont have enough money for transfer this player ! --')
                    pagar()
                elif playerListed[choice_4a][3] <= (listFinance[2][1]) and choice_4b <= (playerListed[choice_4a][3]*0.9):
                    print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                    print(f'        |  {choice_4a} | {playerListed[choice_4a][0].ljust(15)}\t|  {playerListed[choice_4a][1]}\t| {playerListed[choice_4a][2]}  | {playerListed[choice_4a][3]:,}')
                    print('\n\tsorry, we want to negotiation more for the price!')
                    pagar()
                elif playerListed[choice_4a][3] <= (listFinance[2][1]) and choice_4b >= (playerListed[choice_4a][3]*0.9):
                    print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                    print(f'        |  {choice_4a} | {playerListed[choice_4a][0].ljust(15)}\t|  {playerListed[choice_4a][1]}\t| {playerListed[choice_4a][2]}  | {playerListed[choice_4a][3]:,}')    
                    sureUnsureTrans()
                    listFinance[2][1] = ((listFinance[2][1]) - choice_4b)
                    finance1()
                    arsenalTeam[choice_4a] = b
                    arsenalTeam[choice_4a][3] = choice_4b
                    playersInNew[choice_4a] = b
                    del playerListed[choice_4a]
                    arsenal_Team()
                    pagar()
                    break
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
                buyPlayer()
        except ValueError:
            buyPlayer()

def playersIn():
    print('\t\t      PLAYERS IN')
    print('\t\t Player List - General Info :\n')
    print('Index\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
    for a,b in enumerate(playersInNew):
        print (f'  {a}\t|  {b} | {playersInNew[b][0].ljust(15)}\t|  {playersInNew[b][1]}\t| {playersInNew[b][2]}  | {playersInNew[b][3]:,}')

def sureUnsureNo():
    while True:
        sure = input("\n    Are you sure you want to change the players status set 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            player_Listed()
            submenu_4()
        else:
            print('Choice Correctly !')

def nosetStatus():
    while True:
        try:
            player_Listed()
            choice_4c   = input("\nInsert the players number you want to set status : ")
            if  choice_4c.isdigit() == True:
                choice_4c = int(choice_4c)
            if int(choice_4c) in playerListed and int(choice_4c) in arsenalAll:
                a = playerListed[choice_4c]
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_4c} | {playerListed[choice_4c][0].ljust(15)}\t|  {playerListed[choice_4c][1]}\t| {playerListed[choice_4c][2]}  | {playerListed[choice_4c][3]:,}')
                sureUnsureNo()
                playerListed[choice_4c] = a
                del playerListed[choice_4c]
                player_Listed()
                submenu_4()
            else:
                print('\n\t  -- The change status unavailable for this player ! --')
                print("\n\t\t-- Players name is not Arsenal player --\n")
                print("\t\t\t   Insert Correctly !!")
                pagar()
        except ValueError:
            nosetStatus()

def sureUnsureExitTI():
    while True:
        sure = input("\nAre you sure you want to exit 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t ~~ DONE, Arigatou Gozaimasu ~~")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            player_Listed()
            submenu_4()
            pass
        else:
            print('\n\t\tInsert Correctly !')

def title_4():
    print('''
                --  Manager Instruction  --
            
                    Transfer In :
                    1. Buy Player
                    2. Players In
                    3. No Set Status
                    4. Back to Home
                    5. Quit Game
    ''')

def submenu_4():
    while True:
        title_4()
        choice_4 = input('\t\t Please insert your choice : ')
        pagar()
        if  choice_4.isdigit() == True and 1 <= int(choice_4) <= 5:
            choice_4 = int(choice_4)
        if choice_4 == 1:
            buyPlayers()
        elif  choice_4 == 2:
            playersIn()
        elif  choice_4 == 3:
            nosetStatus()
        elif choice_4 == 4:
            home()
        elif choice_4 == 5:
            sureUnsureExitTI()
            exit()
        else:
            print('Choice Correctly !')
            pagar()
            submenu_4()

# ============================================================ SUB MENU 5
def arsenal_All():
    print('\t\t      ALL ARSENAL PLAYER')
    print('\t\t Player List - General Info :\n')
    print('Index\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
    for a,b in enumerate(arsenalAll):
        print (f'  {a}\t|  {b} | {arsenalAll[b][0].ljust(15)}\t|  {arsenalAll[b][1]}\t| {arsenalAll[b][2]}  | {arsenalAll[b][3]:,}')

def sureUnsureSell():
    while True:
        sure = input("\n    Are you sure you want to sell this players 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_All()
            submenu_5()
        else:
            print('Choice Correctly !')
            sureUnsureSell()

def sellPlayers():
    while True:
        try:
            arsenal_All()
            choice_5a   = input("\nInsert the players number you want to sell : ")
            if  choice_5a.isdigit() == True:
                choice_5a = int(choice_5a)
            if  int(choice_5a) in arsenalAll:
                b = arsenalAll[choice_5a]
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_5a} | {arsenalAll[choice_5a][0].ljust(15)}\t|  {arsenalAll[choice_5a][1]}\t| {arsenalAll[choice_5a][2]}  | {arsenalAll[choice_5a][3]:,}')
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
                continue
            choice_5b   = int(input("\nInsert fee transfer to make offer : "))
            if choice_5b < (arsenalAll[choice_5a][3])*1.10:
                print(f'\n\t-- Reject offers of {choice_5b:,} or less !--')
                sellPlayers()
            elif choice_5b >= (arsenalAll[choice_5a][3])*1.10:
                # print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                # print (f'        |  {choice_5a} | {playerListed[choice_5a][0].ljust(15)}\t|  {playerListed[choice_5a][1]}\t| {playerListed[choice_5a][2]}  | {playerListed[choice_5a][3]:,}')
                sureUnsureSell()
                listFinance[2][1] = ((listFinance[2][1]) + choice_5b)
                finance1()
                playersOut[choice_5a] = b
                playersOut[choice_5a][3] = choice_5b
                del arsenalAll[choice_5a]
                arsenal_All()
                break
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
                sellPlayers()
        except ValueError:
            sellPlayers()

def players_Out():
    print('\n\t\t      PLAYERS OUT')
    print('\t\t Player List - General Info :\n')
    print('Index\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
    for a,b in enumerate(playersOut):
        print (f'  {a}\t|  {b} | {playersOut[b][0].ljust(15)}\t|  {playersOut[b][1]}\t| {playersOut[b][2]}  | {playersOut[b][3]:,}')

def retire():
    while True:
        try:
            arsenal_All()
            choice_5c   = input("\nInsert the players number will retire : ")
            if  choice_5c.isdigit() == True:
                choice_5c = int(choice_5c)
            if  int(choice_5c) in arsenalAll:
                b = arsenalAll[choice_5c]
                if arsenalAll[choice_5c][2] >= 32:
                    print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                    print (f'        |  {choice_5c} | {arsenalAll[choice_5c][0].ljust(15)}\t|  {arsenalAll[choice_5c][1]}\t| {arsenalAll[choice_5c][2]}  | {arsenalAll[choice_5c][3]:,}')
                    playersRetire[choice_5c] = b
                    playersRetire.clear()
                    arsenal_All()
                    break
                else:
                    print('Players still young, its not time to retire yet !')
                    retire()
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
                retire()
        except ValueError:
            retire()

def sureUnsureExitTO():
    while True:
        sure = input("\nAre you sure you want to exit 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t ~~ DONE, Arigatou Gozaimasu ~~")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_All()
            submenu_5()
            pass
        else:
            print('\n\t\tInsert Correctly !')

def title_5():
    print('''
                --  Manager Instruction  --
            
                    Transfer Out :
                    1. Sell Player
                    2. Players Out
                    3. Retire
                    4. Back to Home
                    5. Quit Game
    ''')

def submenu_5():
    while True:
        title_5()
        choice_5 = input('\t\t Please insert your choice : ')
        pagar()
        if  choice_5.isdigit() == True and 1 <= int(choice_5) <= 4:
            choice_5 = int(choice_5)
        if  choice_5 == 1:
            sellPlayers()
        elif choice_5 == 2:
            playersOut()
        elif choice_5 == 3:
            retire()
        elif choice_5 == 4:
            home()
        elif choice_5 == 5:
            sureUnsureExitTO()
            exit()
        else:
            print('Choice Correctly !')
            pagar()
            submenu_5()

# ============================================================ SUB MENU 6
def sureUnsureCreate():
    while True:
        sure = input("\n    Are you sure you want to create this players 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_All()
            submenu_6()
        else:
            print('Choice Correctly !')

def create():
    while True:
        try:
            arsenal_All()
            choice_6a = input('\nPlease insert players number (4 digit)      : ')
            if len(choice_6a) == 4:
                if choice_6a.isdigit() == True:
                    if int(choice_6a) in arsenalAll and int(choice_6a) in playerListed:
                        print('\nthe players numbers already exist, choose the other one !')
                        pagar()
                    else:
                        choice_6a = int(choice_6a)
                        choice_6b = input('Please insert players name                  : ').capitalize()
                        choice_6c = input('Please insert players position (GK/CB/MF/ST): ').upper()
                        choice_6d = int(input('Please insert players age (2 digit)         : '))
                        choice_6e = int(input('Please insert players value (in digit)       : '))
                        sureUnsureCreate()
                        arsenalAll[choice_6a]=[choice_6b, choice_6c, choice_6d, choice_6e]
                        arsenal_All()
                else:
                    print("players number consist of 4 digit number")
            else:
                print('\nplayers number consist of 4 digit number')
                pagar()            
        except ValueError:
            create()

def sureUnsureUpdate():
    while True:
        sure = input("\n    Are you sure you want to update this players 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            arsenal_All()
            submenu_6()
        else:
            print('Choice Correctly !')

def updateTeam():
    while True:
        try:
            arsenal_All()
            choice_6f   = input("\nInsert the players number will be updated : ")
            if  choice_6f.isdigit() == True:
                choice_6f = int(choice_6f)
            if  int(choice_6f) in arsenalAll:
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_6f} | {arsenalAll[choice_6f][0].ljust(15)}\t|  {arsenalAll[choice_6f][1]}\t| {arsenalAll[choice_6f][2]}  | {arsenalAll[choice_6f][3]:,}')
                print('''
                            --  Manager Instruction  --
            
                    Item :
                    1. Players Number
                    2. Players Name
                    3. Players Position
                    4. Players Age
                    5. Players Value
                    6. Back to Editor Menu
                ''')
                # while True:
                #     # del arsenalAll[choice_6f]
                #     user = int(input("Insert item that you want to update : "))
                #     if user == 1:
                #         usernumber = int(input('\nUpdate players number : '))
                #         arsenalAll[usernumber]  = arsenalAll[choice_6f]
                #         # arsenalTeam[usernumber] = arsenalTeam[choice_6f]
                #         # arsenalReserve[usernumber] = arsenalReserve[choice_6f]
                #         break
                #     elif user == 2:
                #         username   = input('Change players name                 : ').capitalize()
                #         arsenalAll[username][0] = (username)
                #         # arsenalTeam[username][0] = (username)
                #         # arsenalReserve[username][0] = (username)
                #         break
                #     elif user == 3:
                #         userpos    = input('Change players position             : ').upper()
                #         arsenalAll[userpos][1] = (userpos)
                #         # arsenalTeam[userpos][1] = (userpos)
                #         # arsenalReserve[userpos][1] = (userpos)
                #         break
                #     elif user == 4:
                #         userage    = int(input('Change players age                  : '))
                #         arsenalAll[userage][2] = (userage)
                #         # arsenalTeam[userage][2] = (userage)
                #         # arsenalReserve[userage][2] = (userage)
                #         break
                #     elif user == 5:
                #         uservalue  = int(input('Change players value                : '))
                #         arsenalAll[uservalue][3] = (uservalue)
                #         # arsenalTeam[uservalue][3] = (uservalue)
                #         # arsenalReserve[uservalue][3] = (uservalue)
                #         break
                #     elif user == 6:
                #         break
                sureUnsureUpdate()
                # z = arsenalAll[usernumber]
                # arsenalTeam[choice_6f] = z
                # arsenalReserve[choice_6f] = z
                arsenal_All()
                break
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
        except ValueError:
            sellPlayers()

def sureUnsureUpdatePL():
    while True:
        sure = input("\n    Are you sure you want to update this players 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            player_Listed()
            submenu_6()
        else:
            print('Choice Correctly !')


def updateListed():
    while True:
        try:
            player_Listed()
            choice_6g   = input("\nInsert the players number will be updated : ")
            if  choice_6g.isdigit() == True:
                choice_6g = int(choice_6g)
            if  int(choice_6g) in playerListed:
                print('    \n\t| Number|\tPlayer Name  \t| Pos\t| Age |\t Value  ')
                print (f'        |  {choice_6g} | {playerListed[choice_6g][0].ljust(15)}\t|  {playerListed[choice_6g][1]}\t| {playerListed[choice_6g][2]}  | {playerListed[choice_6g][3]:,}')
                usernumber = int(input('\nUpdate players number or old number : '))
                username   = input('Change players name                 : ')
                userpos    = input('Change players position             : ')
                userage    = int(input('Change players age                  : '))
                uservalue  = int(input('Change players value                : '))
                sureUnsureUpdatePL()
                playerListed[usernumber]  = playerListed[choice_6g]
                del playerListed[choice_6g]
                playerListed[usernumber][0] = (username)
                playerListed[usernumber][1] = (userpos)
                playerListed[usernumber][2] = (userage)
                playerListed[usernumber][3] = (uservalue)
                z = playerListed[usernumber]
                arsenalTeam[choice_6g] = z
                arsenalReserve[choice_6g] = z
                player_Listed()
                break
            else:
                print("\n\t\t-- Players name not found --\n")
                print("\t\t     Insert Correctly !!")
        except ValueError:
            updateListed         

def sureUnsureUpdateFI():
    while True:
        sure = input("\n    Are you sure you want to update finances summary 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t DONE, successful processed !")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            submenu_6()
        else:
            print('Choice Correctly !')

def finance():
    while True:
        try:
            finance1()
            print('Lets update your finances team summary (in number) !')
            balance     = int(input("Update Balance or same                     : "))
            season      = int(input("Update Transfer Budget (Season) or same    : "))
            remaining   = int(input("Update Transfer Budget (Remaining) or same : "))
            loan        = int(input("Update Loans Outstanding or same           : "))
            total_wage  = int(input("Update Total Wage Budget or same           : "))
            current     = int(input("Update Current Wage Total or same          : "))

            # Balance                     
            listFinance[0][1] = balance
            # Transfer Budget (Season) : 
            listFinance[1][1] = season
            # Transfer Budget (Remaining):
            listFinance[2][1] = remaining
            # Loans Outstanding:
            listFinance[3][1] = loan
            # Total Wage Budget:
            listFinance[4][1] = total_wage
            # Current Wage Total:
            listFinance[5][1] = current
            finance1()
            break
        except ValueError:
            updateListed   

def title_6():
    print('''
                --  Manager Instruction  --
            
                    Editor :
                    1. Create Players
                    2. Update Players
                    3. Update Listed Players
                    4. Finance
                    5. Back to Home
                    6. Quit Game
    ''')

def submenu_6():
    while True:
        title_6()
        choice_6 = input('\t\t Please insert your choice : ')
        pagar()
        if  choice_6.isdigit() == True and 1 <= int(choice_6) <= 5:
            choice_6 = int(choice_6)
        if  choice_6 == 1:
            create()
        elif choice_6 == 2:
            updateTeam()
        elif choice_6 == 3:
            updateListed()
        elif choice_6 == 4:
            finance()
        elif choice_6 == 5:
            home()
        elif choice_6 == 6:
            sureUnsureExitTI()
            exit()
        else:
            print('Choice Correctly !')
            pagar()
   
# ============================================================ MAIN MENU
def sureUnsureExitHome():
    while True:
        sure = input("\nAre you sure you want to exit 'YES / NO' : ").lower()
        if sure in macamYes:
            print("\n\t\t ~~ DONE, Arigatou Gozaimasu ~~")
            pagar()
            break
        elif sure in macamNo:
            pagar()
            home()
            pass
        else:
            print('\n\t\tInsert Correctly !')

def title():
    print('''
        -- Welcome to Arsenal Football Club --
            
                    Home :
                    1. Arsenal
                    2. Arsenal Reserve
                    3. Finance
                    4. Transfer In
                    5. Transfer Out
                    6. Editor
                    7. Quit Game
    ''')

def pagar():
    print('=================================================================')

def home():
    while True:
        title()
        choice = input('\t       Please insert your choice : ')
        pagar()
        if choice.isdigit() == True and 1 <= int(choice) <= 7:
            choice = int(choice)
        if int(choice) == 1:
            arsenal_Team()
            submenu_1()
        elif int(choice) == 2:
            arsenal_Reserve()
            submenu_2()
        elif int(choice) == 3:
            submenu_3()
        elif int(choice) == 4:
            player_Listed()
            submenu_4()
        elif int(choice) == 5:
            arsenal_All()
            submenu_5()
        elif int(choice) == 6:
            submenu_6()
        elif int(choice) == 7:
            sureUnsureExitHome()
            exit()
        else:
            print('Choice Correctly !')
            pagar()
        



home()
