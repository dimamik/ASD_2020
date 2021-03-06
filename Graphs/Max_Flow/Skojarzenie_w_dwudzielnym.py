def ZbudujSiecResidualną(G,P):
    """ Budowanie sieci residualnej """
    R=[None]*len(G)
    for i in range(len(G)):
        R[i]=[-1]*len(G)
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0:
                R[i][j]=G[i][j]
                R[j][i]=P[i][j]
                if R[j][i]==0:
                    R[j][i]=-1
                if R[i][j]==0:
                    R[i][j]=-1
    return R

def Sciezka_Powieksz(R,s,t):
    Q=[]
    tab_d=[float("inf")]*len(R)
    tab_p=[-1]* len(R)
    tab_v = [False] * len(R)
    tab_v[s]=True
    tab_d[s]=0
    Q.append(s)
    while len(Q)>0:
        u=Q.pop()
        for v in range(len(R)):
            if R[u][v]!=-1 and not tab_v[v]:
                tab_v[v]=True
                tab_d[v]=tab_d[u]+1
                tab_p[v]=u
                Q.append(v)
    min_flow=999
    u=tab_p[t]
    v=t
    while u!=-1:
        min_flow=min(R[u][v],min_flow)
        v=u
        u=tab_p[v]

    if min_flow>100:
        min_flow=-1
    return min_flow,tab_p




def Floyd_Fulkerson(G,s,t):
    """ 
    G - graf NIESKIEROWANY pojemnosci w postaci macierzy incydencji
     """
    P = [None]*len(G)
    for i in range(len(G)):
        P[i]=[0] * len(G)
    
    """ Znajdz sciezke powiekszajaca w sieci residualnej """
    max_flow=0
    R=ZbudujSiecResidualną(G,P)
    min_c_flow,tab_p=Sciezka_Powieksz(R,s,t)
    while min_c_flow>0:
        """ Rysuje droge przeplywu """
        u=tab_p[t]
        v=t
        output=[]
        while u!=-1:
            """ print("(",u,"->",v,")", end=" ") """
            output.append((u,v))
            v=u
            u=tab_p[v] 
        """ print(min_c_flow) """
        output=sorted(output)
        output.append(' Płynie -> ')
        output.append(min_c_flow)
        print(output)
        max_flow+=min_c_flow
        u=tab_p[t]
        v=t
        while u!=-1:
            G[u][v]-=min_c_flow
            P[u][v]+=min_c_flow
            v=u
            u=tab_p[v]
        R=ZbudujSiecResidualną(G,P)
        min_c_flow,tab_p=Sciezka_Powieksz(R,s,t)
    return max_flow

def SkojarzenieDwudzielny(tab_v,first_group,second_group):
    """ 
    Takes: 
        DWUDZIELNY GRAPH NIESKIEROWANY tab_v w postaci macierzy incydencji
        first_group = [0,1,2,3] -> wierzcholki z lewej strony graphu dwudzielnego
        second_group = [0,1,2,3] -> wierzcholki z prawej strony graphu dwudzielnego
    Automatycznie Dodaje do grafu 2 wierzcholki s and f
    Returns: Ilosc Skojarzen w grafie dwudzielnym
     """
    tab_v.append([0 for _ in range(len(tab_v))])
    tab_v.append([0 for _ in range(len(tab_v)-1)])
    for i in range(len(tab_v)):
        tab_v[i].append(0)
        tab_v[i].append(0)
    for i in range(len(first_group)):
        tab_v[len(tab_v)-2][first_group[i]]=1
    for i in range(len(second_group)):
        tab_v[second_group[i]][len(tab_v)-1]=1
    return Floyd_Fulkerson(tab_v,len(tab_v)-2,len(tab_v)-1)
tab_v=[
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,1,1],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]
print(SkojarzenieDwudzielny(tab_v,[0,1,2,3],[4,5,6,7]))