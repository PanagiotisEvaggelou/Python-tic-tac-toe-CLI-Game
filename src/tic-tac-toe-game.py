def cr_table(value2):
    AZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    for x in range(value2+1):
        if x!=0:
            print('   ', x, end = '')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')
    for x in range(value2): 
        print('\n', end='')
        print(AZ[x], end='')
        for y in range(value2+1):
            print('|','   ', end='')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')

def mark_table(value2,table):
    AZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in range(value2+1):
        if x!=0:
            print('   ', x, end = '')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')
    for x in range(value2): 
        print('\n', end='')
        print(AZ[x], end='')
        for y in range(value2+1):
            if y<value2:
                if table[x][y]==1:
                    print('|','  O', end='')
                elif table[x][y]==2:
                    print('|','  X', end='')
                else:
                    print('|','   ', end='')
            else:
                print('|','   ', end='')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')

def markstar1(value2,table,listwin):
    print('Τα σύμβολα "*" προσδιορίζουν την νικητήρια τετράδα.\n')
    AZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in range(value2+1):
        if x!=0:
            print('   ', x, end = '')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')
    for x in range(value2): 
        print('\n', end='')
        print(AZ[x], end='')
        for y in range(value2+1):
            if y<value2:
                if table[x][y]==1:
                    tr=0
                    for l in range(4):
                        if x==listwin[l][0] and y==listwin[l][1]:
                            print('|','  *', end='')
                            tr=1
                    if tr==0:
                        print('|','  O', end='')   
                elif table[x][y]==2:
                    print('|','  X', end='')
                else:
                    print('|','   ', end='')
            else:
                print('|','   ', end='')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')

def markstar2(value2,table,listwin):
    print('Τα σύμβολα "*" προσδιορίζουν την νικητήρια τετράδα.\n')
    AZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in range(value2+1):
        if x!=0:
            print('   ', x, end = '')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')
    for x in range(value2): 
        print('\n', end='')
        print(AZ[x], end='')
        for y in range(value2+1):
            if y<value2:
                if table[x][y]==2:
                    tr=0
                    for l in range(4):
                        if x==listwin[l][0] and y==listwin[l][1]:
                            print('|','  *', end='')
                            tr=1
                    if tr==0:
                        print('|','  X', end='')   
                elif table[x][y]==1:
                    print('|','  O', end='')
                else:
                    print('|','   ', end='')
            else:
                print('|','   ', end='')
    print('\n', end='')
    for x in range(5*value2):
        print('-', end = '')



def p_1(value3,value2):
    full=0
    for i in reversed(range(value2)):
        if table[i][int(value3)-1] == 0:
            table[i][int(value3)-1] = 1
            full=1
            break
    if full==0:
        value3 = int(input('Η συγκεκριμένη στήλη είναι γεμάτη, παρακαλώ επέλεξε μία διαφορετική στήλη: '))
        p_1(value3,value2)


def p_2(value4,value2):
    full=0
    for i in reversed(range(value2)):
        if table[i][int(value4)-1] == 0:
            table[i][int(value4)-1] = 2
            full=1
            break
    if full==0:
        value4 = int(input('Η συγκεκριμένη στήλη είναι γεμάτη, παρακαλώ επέλεξε μία διαφορετική στήλη: '))
        p_2(value4,value2)


def check(table,value2):

    listwin=[[0],[0],[0],[0]]
    for i in range(value2):
        point1 = 0
        point2 = 0
        for j in range(value2):
            if table[i][j] == 1:
                if point2==0:
                    point1=point1+1
                    listwin[point1-1]=[i,j]
                else:
                    point2 = 0
                    point1 = 1
                    listwin[point1-1]=[i,j]
            elif table[i][j] == 2:
                if point1==0:
                    point2=point2+1
                    listwin[point2-1]=[i,j]
                else:
                    point1 = 0
                    point2 = 1
                    listwin[point2-1]=[i,j]
            elif table[i][j] == 0:
                point1 = 0
                point2 = 0

            if point1 == 4:
                print('\n')
                markstar1(value2,table,listwin)
                return 1
            elif point2 == 4:
                print('\n')
                markstar2(value2,table,listwin)
                return 2
    
    listwin=[[0],[0],[0],[0]]
    for j in range(value2):
        point1 = 0
        point2 = 0
        for i in range(value2):
            if table[i][j] == 1:
                if point2==0:
                    point1=point1+1  
                    listwin[point1-1]=[i,j]
                else:
                    point2 = 0
                    point1 = 1
                    listwin[point1-1]=[i,j]
            elif table[i][j] == 2:
                if point1==0:
                    point2=point2+1
                    listwin[point2-1]=[i,j]
                else:
                    point1 = 0
                    point2 = 1
                    listwin[point2-1]=[i,j]
            elif table[i][j] == 0:
                point1 = 0
                point2 = 0
            if point1 == 4:
                print('\n')
                markstar1(value2,table,listwin)
                return 1
            elif point2 == 4:
                print('\n')
                markstar2(value2,table,listwin)
                return 2
    
    max_col = value2
    max_row = value2
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    fdiagxy = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    bdiagxy = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(table[y][x])
            rows[y].append(table[y][x])
            fdiag[x+y].append(table[y][x])
            fdiagxy[x+y].append([y,x])
            bdiag[x-y-min_bdiag].append(table[y][x])
            bdiagxy[x-y-min_bdiag].append([y,x])

    #print(cols)
    #print(rows)
    #print(fdiag)
    #print(bdiag)

    listwin=[[0],[0],[0],[0]]
    for x in range(len(fdiag)):
        point1=0
        point2=0
        for j in range(len(fdiag[x])):
            if len(fdiag[x])>=4:
                if fdiag[x][j]==1:
                    if point2==0:
                        point1=point1+1
                        listwin[point1-1]=fdiagxy[x][j]
                    else:
                        point2 = 0
                        point1 = 1
                        listwin[point1-1]=fdiagxy[x][j]
                elif fdiag[x][j] == 2:
                    if point1==0:
                        point2=point2+1
                        listwin[point2-1]=fdiagxy[x][j]
                    else:
                        point1 = 0
                        point2 = 1
                        listwin[point2-1]=fdiagxy[x][j]
                elif fdiag[x][j] == 0:
                    point1 = 0
                    point2 = 0
                if point2==4:
                    print('\n')
                    markstar2(value2,table,listwin)
                    return 2
                elif point1==4:
                    print('\n')
                    markstar1(value2,table,listwin)
                    return 1

    listwin=[[0],[0],[0],[0]]
    for x in range(len(bdiag)):
        point1=0
        point2=0
        if len(bdiag[x])>=4:
            for j in range(len(bdiag[x])):
                if bdiag[x][j]==1:
                    if point2==0:
                        point1=point1+1
                        listwin[point1-1]=bdiagxy[x][j]
                    else:
                        point2 = 0
                        point1 = 1
                        listwin[point1-1]=bdiagxy[x][j]
                elif bdiag[x][j] == 2:
                    if point1==0:
                        point2=point2+1
                        listwin[point2-1]=bdiagxy[x][j]
                    else:
                        point1 = 0
                        point2 = 1
                        listwin[point2-1]=bdiagxy[x][j]
                elif bdiag[x][j] == 0:
                    point1 = 0
                    point2 = 0
                if point2==4:
                    print('\n')
                    markstar2(value2,table,listwin)
                    return 2
                elif point1==4:
                    print('\n')
                    markstar1(value2,table,listwin)
                    return 1

    return 0    

def checkwin(table,value2):
    if check(table,value2)==1:
        print('\n')
        print('Συγχαρητήρια, πήρε πόντο ο Παίκτης 1!')
        return 1
    elif check(table,value2)==2:
        print('\n')
        print('Συγχαρητήρια, πήρε πόντο ο Παίκτης 2!')
        return 2
    else:
        Full=0
        for i in range(value2):
            for j in range(value2):
                if table[i][j]==0:
                    Full=1
        if Full==0:
            print('\n')
            print('Το ταμπλό είναι γεμάτο, το παιχνίδι έληξε.')
            return -1
        else:
            return 0

def listwin_ret(table,value2):

    listwin=[[0],[0],[0],[0]]
    for i in range(value2):
        point1 = 0
        point2 = 0
        for j in range(value2):
            if table[i][j] == 1:
                if point2==0:
                    point1=point1+1
                    listwin[point1-1]=[i,j]
                else:
                    point2 = 0
                    point1 = 1
                    listwin[point1-1]=[i,j]
            elif table[i][j] == 2:
                if point1==0:
                    point2=point2+1
                    listwin[point2-1]=[i,j]
                else:
                    point1 = 0
                    point2 = 1
                    listwin[point2-1]=[i,j]
            elif table[i][j] == 0:
                point1 = 0
                point2 = 0
            if point1 == 4:
                return listwin
            elif point2 == 4:
                return listwin
    
    listwin=[[0],[0],[0],[0]]
    for j in range(value2):
        point1 = 0
        point2 = 0
        for i in range(value2):
            if table[i][j] == 1:
                if point2==0:
                    point1=point1+1  
                    listwin[point1-1]=[i,j]
                else:
                    point2 = 0
                    point1 = 1
                    listwin[point1-1]=[i,j]
            elif table[i][j] == 2:
                if point1==0:
                    point2=point2+1
                    listwin[point2-1]=[i,j]
                else:
                    point1 = 0
                    point2 = 1
                    listwin[point2-1]=[i,j]
            elif table[i][j] == 0:
                point1 = 0
                point2 = 0
            if point1 == 4:
                return listwin
            elif point2 == 4:
                return listwin
    
    max_col = value2
    max_row = value2
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    fdiagxy = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    bdiagxy = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(table[y][x])
            rows[y].append(table[y][x])
            fdiag[x+y].append(table[y][x])
            fdiagxy[x+y].append([y,x])
            bdiag[x-y-min_bdiag].append(table[y][x])
            bdiagxy[x-y-min_bdiag].append([y,x])

    listwin=[[0],[0],[0],[0]]
    for x in range(len(fdiag)):
        point1=0
        point2=0
        for j in range(len(fdiag[x])):
            if len(fdiag[x])>=4:
                if fdiag[x][j]==1:
                    if point2==0:
                        point1=point1+1
                        listwin[point1-1]=fdiagxy[x][j]
                    else:
                        point2 = 0
                        point1 = 1
                        listwin[point1-1]=fdiagxy[x][j]
                elif fdiag[x][j] == 2:
                    if point1==0:
                        point2=point2+1
                        listwin[point2-1]=fdiagxy[x][j]
                    else:
                        point1 = 0
                        point2 = 1
                        listwin[point2-1]=fdiagxy[x][j]
                elif fdiag[x][j] == 0:
                    point1 = 0
                    point2 = 0
                if point2==4:
                    return listwin
                elif point1==4:
                    return listwin

    listwin=[[0],[0],[0],[0]]
    for x in range(len(bdiag)):
        point1=0
        point2=0
        if len(bdiag[x])>=4:
            for j in range(len(bdiag[x])):
                if bdiag[x][j]==1:
                    if point2==0:
                        point1=point1+1
                        listwin[point1-1]=bdiagxy[x][j]
                    else:
                        point2 = 0
                        point1 = 1
                        listwin[point1-1]=bdiagxy[x][j]
                elif bdiag[x][j] == 2:
                    if point1==0:
                        point2=point2+1
                        listwin[point2-1]=bdiagxy[x][j]
                    else:
                        point1 = 0
                        point2 = 1
                        listwin[point2-1]=bdiagxy[x][j]
                elif bdiag[x][j] == 0:
                    point1 = 0
                    point2 = 0
                if point2==4:
                    return listwin
                elif point1==4:
                    return listwin

    return 0

def clear_stars():
    listwin = listwin_ret(table,value2)
    for i in range(value2):
        for j in range(value2):
            for l in range(4):
                if i==listwin[l][0] and j==listwin[l][1]:
                    table[i][j] = 0

    for j in range(value2):
        for i in reversed(range(1,value2)):
            if table[i][j] == 0:
                if table[i-1][j] != 0:
                    table[i][j] = table[i-1][j]
                    table[i-1][j] = 0


def checkforwinagain(table,value2):
    if check(table,value2)==1:
        print('\n')
        print('Συγχαρητήρια, νίκησε ο Παίκτης 1!')
        return 1
    elif check(table,value2)==2:
        print('\n')
        print('Συγχαρητήρια, νίκησε ο Παίκτης 2!')
        return 2
    else:
        return 0


def rounds(wins1,wins2):
    win=0
    num=1
    while win==0:
        if num%2!=0:
            if num>2:
                print('\n')
                v = input('Πατήστε οποιοδήποτε πλήκτρο για να συνεχίσετε. \nΓια παύση του παιχνδιού και αποθήκευση σε αρχείο επιλέξτε "s": ')
                if v =='s' or v == 'S' or v == 'Σ' or v == 'σ':
                    import csv
                    onoma = input('Δώσε όνομα αρχείου: ')
                    with open(onoma+'.csv', mode='w', newline='') as f:
                        w = csv.writer(f)
                        w.writerows(table)

                    print('Το παιχνίδι αποθηκεύτηκε!')
                    return 0
                    

            print('\n')
            value3 = int(input('Παίκτης 1: Επέλεξε στήλη για το πιόνι σου:'))
            while value3<1 or value3>value2:
                value3 = int(input('Ο αριθμός στήλης που δώθηκε είναι έξω από τα όρια του ταμπλό, παρακαλώ επέλεξε μία άλλη στήλη: '))
            p_1(value3,value2)

            print('\n', end='')
            mark_table(value2,table)

            result = checkwin(table,value2)
            if result > 0:
                win=1
                wins1=wins1+1
                if result == 1:
                    print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                elif result == 2:
                    print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                nexr = input('Θέλετε να παίξετε νέο γύρο(Ν/Ο);')
                if nexr == 'N' or nexr == 'Ν' or nexr == 'ν' or nexr == 'n':

                    clear_stars()

                    garbage = table.pop(value2)
                    print('\n')
                    print('Νέος γύρος>----------------------------------')
                    print('\n', end='')
                    mark_table(value2,table)
                    table.append([wins1,wins2])


                    checkagain = 1
                    while checkagain == 1 or checkagain == 2:
                        checkagain = checkforwinagain(table,value2)
                        if checkagain == 1:
                            wins1=wins1+1
                            print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                            clear_stars()
                            garbage = table.pop(value2)
                            print('Νέος γύρος>----------------------------------')
                            print('\n', end='')
                            mark_table(value2,table)
                            table.append([wins1,wins2])
                        elif checkagain == 2:
                            wins2 = wins2 + 1
                            print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                            clear_stars()
                            garbage = table.pop(value2)
                            print('Νέος γύρος>----------------------------------')
                            print('\n', end='')
                            mark_table(value2,table)
                            table.append([wins1,wins2])
                    

                    if rounds(wins1,wins2) == -1:
                        return -1
                elif nexr == 'O' or nexr == 'o' or nexr == 'ο' or nexr == 'Ο':
                    if wins1>wins2:
                        
                        print('\nΣυγχαρητήρια, νίκησε ο Παίκτης 1!')
                        print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    elif wins1<wins2:
                        print('\nΣυγχαρητήρια, νίκησε ο Παίκτης 2!')
                        print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    else:
                        print('\nΣυγχαρητήρια, βγήκατε ισοπαλία!')
                        print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    return -1
            elif result == -1:
                if wins1>wins2:
                    print('Συγχαρητήρια, νίκησε ο Παίκτης 1!')
                    print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                elif wins1<wins2:
                    print('Συγχαρητήρια, νίκησε ο Παίκτης 2!')
                    print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                else:
                    print('Συγχαρητήρια, βγήκατε ισοπαλία!')
                    print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    return -1

            num=num+1
        else:
            
            print('\n')
            value4 = int(input('Παίκτης 2: Επέλεξε στήλη για το πιόνι σου: '))
            while value4<1 or value4>value2:
                value4 = int(input('Ο αριθμός στήλης που δώθηκε είναι έξω από τα όρια του ταμπλό, παρακαλώ επέλεξε μία άλλη στήλη: '))
            p_2(value4,value2)

            print('\n', end='')
            mark_table(value2,table)

            result = checkwin(table,value2)
            if result > 0:
                win=1
                wins2=wins2+1
                if result == 1:
                    print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                elif result == 2:
                    print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                nexr = input('Θέλετε να παίξετε νέο γύρο(Ν/Ο); ')
                if nexr == 'N' or nexr == 'Ν' or nexr == 'ν' or nexr == 'n':

                    clear_stars()

                    garbage = table.pop(value2)
                    print('\n')
                    print('Νέος γύρος>----------------------------------')
                    print('\n', end='')                
                    mark_table(value2,table)
                    table.append([wins1,wins2])

                    checkagain = 1
                    while checkagain == 1 or checkagain == 2:
                        checkagain = checkforwinagain(table,value2)
                        if checkagain == 1:
                            wins1=wins1+1
                            print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2) 
                            clear_stars()
                            garbage = table.pop(value2)
                            print('Νέος γύρος>----------------------------------')
                            print('\n', end='')
                            mark_table(value2,table)
                            table.append([wins1,wins2])
                        elif checkagain == 2:
                            wins2 = wins2 + 1
                            print('\nΣκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2) 
                            clear_stars()
                            garbage = table.pop(value2)
                            print('Νέος γύρος>----------------------------------')
                            print('\n', end='')
                            mark_table(value2,table)
                            table.append([wins1,wins2])

                    if rounds(wins1,wins2) == -1:
                        return -1
                elif nexr == 'O' or nexr == 'o' or nexr == 'ο' or nexr == 'Ο':
                    if wins1>wins2:
                        print('\nΣυγχαρητήρια, νίκησε ο Παίκτης 1!')
                        print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    elif wins1<wins2:
                        print('\nΣυγχαρητήρια, νίκησε ο Παίκτης 2!')
                        print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    else:
                        print('\nΣυγχαρητήρια, βγήκατε ισοπαλία!')
                        print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    return -1
            elif result == -1:
                if wins1>wins2:
                    print('Συγχαρητήρια, νίκησε ο Παίκτης 1!')
                    print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                elif wins1<wins2:
                    print('Συγχαρητήρια, νίκησε ο Παίκτης 2!')
                    print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                else:
                    print('Συγχαρητήρια, βγήκατε ισοπαλία!')
                    print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
                    return -1
            

            num=num+1

print('Καλωσήλθατε στο παιχνίδι!')
value1 = input('Επιθυμείτε νέο παιχνίδι (Ν) ή φόρτωση παιχνιδιού από αρχείο (S); ')

if value1 == 'N' or value1 == 'n' or value1 == 'Ν' or value1 == 'ν':
    value2 = int(input('Δώστε αριθμό στηλών παιχνιδιού (5-10): '))
    while (value2<5 or value2>10):
        value2 = int(input('Ο αριθμός στηλών που δώσατε δεν υποστηρίζεται, παρακαλώ εισάγεται έναν αριθμό μεταξύ του 5 και του 10: '))
    table = list(range(value2))
    for i in range(value2):
        a = list(range(value2))
        table[i] = a
        for j in range(value2):
            table[i][j] = 0
    
    print('\n', end='')
    cr_table(value2)

    wins1=0
    wins2=0
    table.append([wins1,wins2])

    result_rounds = rounds(wins1,wins2)
    if result_rounds == -1:
        print("Τέλος παιχνιδιού>-----------------------------------")

elif value1 == 'S' or value1 == 's' or value1 == 'σ' or value1 == 'Σ':
    import csv
    onoma = input('Δώσε όνομα αρχείου: ')
    with open(onoma+'.csv', mode='r') as f:
        r = csv.reader(f)
        table = list(r)
    
    value2 = len(table)-1
    print('\n', end='')
   
    for i in range(value2):
        for j in range(value2):
            table[i][j]=int(table[i][j])
            
    

    mark_table(value2,table)

    wins1=int(table[value2][0])
    wins2=int(table[value2][1])
    print('\n')
    print('Σκορ = Παίκτης 1:',wins1,'/ Παίκτης 2:',wins2)
    print('Συνέχεια παρτίδας>----------------------------------')
    if rounds(wins1,wins2) == -1:
        print("Τέλος παιχνιδιού>-----------------------------------")
