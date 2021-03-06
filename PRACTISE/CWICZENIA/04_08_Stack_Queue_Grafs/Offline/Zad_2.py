""" Implementacja dla list sąsiedstwa, czyli:
[[1,2,3],[],[4,5]], G[i]-lista numerów wierz połączonych z i-tym wierzchołkiem

""" 
class Wierzcholek():
    def __init__(self,index=0,polacz=None,index_parrent=None):
        self.visited=False
        self.entry=0
        self.process=0
        #tmp=Wierzcholek()
        self.parrent=None
        self.index=index
        self.polacz=polacz
        self.index_parrent=index_parrent

def tab_to_Wierz(tab):
    n=len(tab)
    tmp=[None]*n
    for i in range(n):
        tmp[i]=Wierzcholek(i,tab[i],None)
    return tmp


def DFSVisit(u,time,tab_ready):
        time+=1
        u.visited=True
        u.entry=time
        #print(u.polacz)
        for i in u.polacz:
            #print("i, to ",i)
            if not tab_ready[i].visited:
                #print("Wszedlem z i",i)
                tab_ready[i].index_parrent=u.index
                #print("Przypisuje dla",i,tab_ready[i].index_parrent)
                #print(tab_ready[i].index_parrent)
                DFSVisit(tab_ready[i],time,tab_ready)
        time+=1
        u.process=time 


def DFS( G ):
    time=0
    tab_ready=tab_to_Wierz(G)
    
    for v in tab_ready:
        if not v.visited: DFSVisit(v,time,tab_ready)
    """ for  i in range(len(tab_ready)):
        print("Wypisuja dla i = ",i,tab_ready[i].index_parrent,end='\n') """
    #print(tab_ready[3].index_parrent)
    tab=[0]*len(tab_ready)
    for  i in range(len(tab_ready)):
        tab[i]=tab_ready[i].index_parrent
    return tab
K = [[1,4],[2],[4],[],[3]]
G = [[1,2],[0,2,3],[3,1,0],[]]
print( DFS(K) )