import math
def MINIMAX_ALGO(D,I,T,S,T_D):
    if (D == T_D):  
        return (S[D][I],S)
    if (T):
        a=MINIMAX_ALGO(D + 1,I*2,False,S,T_D)
        b=MINIMAX_ALGO(D + 1,I*2+1,False,S,T_D)
        mx=max(a[0][1],b[0][1])
        S=b[1]
        S[D][I][1]=mx
        return ((S[D][I][0],mx),S)
    else: 
        c=MINIMAX_ALGO(D + 1,I*2,True,S,T_D)
        d=MINIMAX_ALGO(D + 1,I*2+1,True,S,T_D)
        mn=min(c[0][1],d[0][1])
        S=d[1]
        S[D][I][1]=mn
        return ((S[D][I][1],mn),S)


Utility_Values = [
    [['A',None]],
    [['B',None],['C',None]],
    [['D',None],['E',None],['F',None],['G',None]],
    [('H',-1),('I',3),('J',5),('K',1),('L',-6),('M',-4),('N',0),('O',9)]
]
Tree_Depth = 3
print("Tree Depth: ",Tree_Depth)
result=MINIMAX_ALGO(0,0,True,Utility_Values,Tree_Depth)
print("The Optimal Value is : ",result[0][1])  
path=[]
path.append(result[0][0])
for i in range(1,Tree_Depth+1):
    for j in range(0,len(result[1][i])):
        if result[1][i][j][1]==result[0][1]:
            path.append(result[1][i][j][0])
            break
print("Path: ",path)