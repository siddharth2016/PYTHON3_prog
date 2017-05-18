#BATMAN AND TIC-TAC-TOE                 
for i in range(int(input())):
    mat = []
    for j in range(4):
        mat = mat + [str(input())]
    #print(mat)
    f1 = 0
    countdot = countdot1 = countdot2 = countdot3 = countdot4 = countdot5 = countdot6 = countdot7 = countdot8 = 0
    countx = countx1 = countx2 = countx3 = countx4 = countx5 = countx6 = countx7 = countx8 = 0
    for j in range(4):
        for k in range(4):
            if mat[j][k]=='x':
                countx += 1
            if mat[j][k]=='.' and countdot!=1:
                countx += 1
                countdot = 1
            elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot==1):
                countx = 0
                countdot = 0
            if countx>=3:
                print("YES")
                f1 = 1
                break
                
            if j==k:
                if mat[j][k]=='x':
                    countx2 += 1
                if mat[j][k]=='.' and countdot2!=1:
                    countx2 += 1
                    countdot2 = 1
                elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot2==1):
                    countx2 = 0
                    countdot2 = 0
                if countx2>=3:
                    print("YES")
                    f1 = 1
                    break
                
                    
            if (j==0 and k==1) or (j==1 and k==2) or (j==2 and k==3):
                if mat[j][k]=='x':
                    countx3 += 1
                if mat[j][k]=='.' and countdot3!=1:
                    countx3 += 1
                    countdot3 = 1
                elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot==1):
                    countx3 = 0
                    countdot3 = 0
                if countx3>=3:
                    print("YES")
                    f1 = 1
                    break
                
                
                if mat[k][j]=='x':
                    countx4 += 1
                if mat[k][j]=='.' and countdot4 != 1:
                    countx4 += 1
                    countdot4 = 1
                elif (mat[k][j]=='o') or (mat[k][j]=='.' and countdot4==1):
                    countx4 = 0
                    countdot4 = 0
                if countx4>=3:
                    print("YES")
                    f1 = 1
                    break
                
                    
            if (j==0 and k==3) or (j==1 and k==2) or (j==2 and k==1) or (j==3 and k==0):
                if mat[j][k]=='x':
                    countx5 += 1
                if mat[j][k]=='.' and countdot5!=1:
                    countx5 += 1
                    countdot5 = 1
                elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot5==1):
                    countx5 = 0
                    countdot5 = 0
                if countx5>=3:
                    print("YES")
                    f1 = 1
                    break
                
                if mat[k][j]=='x':
                    countx8 += 1
                if mat[k][j]=='.' and countdot8!=1:
                    countx8 += 1
                    countdot8 = 1
                elif (mat[k][j]=='o') or (mat[k][j]=='.' and countdot8==1):
                    countx8 = 0
                    countdot8 = 0
                if countx8>=3:
                    print("YES")
                    f1 = 1
                    break
                
                    
            if (j==0 and k==2) or (j==1 and k==1) or (j==2 and k==0):
                if mat[j][k]=='x':
                    countx6 += 1
                if mat[j][k]=='.' and countdot6!=1:
                    countx6 += 1
                    countdot6 = 1
                elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot6==1):
                    countx6 = 0
                    countdot6 = 0
                if countx6>=3:
                    print("YES")
                    f1 = 1
                    break
            
            if (j==1 and k==3) or (j==2 and k==2) or (j==3 and k==1):
                if mat[j][k]=='x':
                    countx7 += 1
                if mat[j][k]=='.' and countdot7!=1:
                    countx7 += 1
                    countdot7 = 1
                elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot7==1):
                    countx7 = 0
                    countdot7 = 0
                if countx7>=3:
                    print("YES")
                    f1 = 1
                    break
                
                 
        if f1==1:
            break
        else:
            countdot = 0
            countx = 0
        
    if f1!=1:
        for j in range(4):
            for k in range(4):
                if mat[k][j]=='x':
                    countx1 += 1
                if mat[k][j]=='.' and countdot1!=1:
                    countx1 += 1
                    countdot1 = 1
                elif (mat[k][j]=='o') or (mat[k][j]=='.' and countdot1==1):
                    countx1 = 0
                    countdot1 = 0
                if countx1>=3:
                    print("YES")
                    f1 = 1
                    break
            if f1 == 1:
                break
            else:
                countdot1=countx1=0
        if f1!=1:
            countx1=countdot1=0
            for j in range(4):
                for k in range(3,-1,-1):
                    if mat[k][j]=='x':
                        countx1 += 1
                    if mat[k][j]=='.' and countdot1!=1:
                        countx1 += 1
                        countdot1 = 1
                    elif (mat[k][j]=='o') or (mat[k][j]=='.' and countdot1==1):
                        countx1 = 0
                        countdot1 = 0
                    if countx1>=3:
                        print("YES")
                        f1 = 1
                        break
                if f1 == 1:
                    break
                else:
                    countdot1=countx1=0
            if f1!=1:
                countx=countdot=0
                for j in range(4):
                    for k in range(3,-1,-1):
                        if mat[j][k]=='x':
                            countx += 1
                        if mat[j][k]=='.' and countdot!=1:
                            countx += 1
                            countdot = 1
                        elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot==1):
                            countx = 0
                            countdot = 0
                        if countx>=3:
                            print("YES")
                            f1 = 1
                            break
                    if f1 == 1:
                        break
                    else:
                        countx=countdot=0
                if f1!=1:
                    countx2=countdot2=0
                    for j in range(3,-1,-1):
                        for k in range(3,-1,-1):
                            if j==k:
                                if mat[j][k]=='x':
                                    countx2 += 1
                                if mat[j][k]=='.' and countdot2!=1:
                                    countx2 += 1
                                    countdot2 = 1
                                elif (mat[j][k]=='o') or (mat[j][k]=='.' and countdot2==1):
                                    countx2 = 0
                                    countdot2 = 0
                                if countx2>=3:
                                    print("YES")
                                    f1 = 1
                                    break
                        if f1==1:
                            break
                    if f1!=1:
                        print("NO")
                        
        
