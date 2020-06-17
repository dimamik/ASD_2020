""" 
Dzmitry Mikialevich
1. Ogolnie algorytm polega na:
1) Iterujemy po kolei po przedzialach, i:
    1) Patrzymy na intersection jego lewego i prawego końców i jeśli:
        1) Nie ma żadnych przecięć: Dodajemy jego długość do wyniku
        2) Ma przecięcie z prawej i/lub z lewej strony:
            1) Łączę przedział odpowiednio usuwając obydwa (ten na którym jestesmy i lewy i/lub prawy) i dodając ich sumę. Jak mamy i lewy i prawy, to odpowiednio robię to najpierw dla lewego a potem dla prawego
            2) Dodaję długość otrzymanego przedziału do tablicy, bo mam gwarancję, że mam maksymalne przedziały (lewy i/lub prawy) 
Ogólna złożoność algorytmu -> O(n^2) - pesymistyczna, O(nlogn)- oczekiwana,
Mam w tab[-1] wartosc 0 (ostatnia wartosc tablicy) i dlatego algorytm sie nie zepsuje
Bo intersect może zwrócić n przedziałów
Gdzies brakuje nawiasu i nie mam czasu to poprawic(
 """

from inttree import *

# przykladowy test uzycia drzewa przedzialowego 
# T = tree([1, 2, 3, 4, 5])
# tree_insert(T,(1, 4))
# tree_insert(T,(2, 5))
# tree_print(T)
# tree_remove(T,(1, 4))
# print()
# tree_print(T)
# tree_insert(T,(1, 3))
# print(tree_intersect(T, 3))
# exit(0)



def intervals( I ):
    tab_of_numbers=[]
    for i in range(len(I)):
        tab_of_numbers.append(I[i][0])
        tab_of_numbers.append(I[i][1])
    tab_of_numbers=sorted(set(tab_of_numbers))
    tab_to_ret=[0]*len(I)
    #print(tab_of_numbers)
    T= tree(tab_of_numbers)
    for i in range(len(I)):
        # W tym przypadku mamy nie przecinający się z lewej i prawej strony 
        
        right=len(tree_intersect(T,I[i][1]))==0
        left=len(tree_intersect(T,I[i][0]))==0
        print(left,right)
        if ( left and right):
            tree_insert(T,I[i])
            l=I[i][1]-I[i][0]
            tab_to_ret[i]=max(tab_to_ret[i-1],l)
        elif not right and left:
            #Teraz mamy wybrac maksymalny przedzial z returna intersection
            k=tree_intersect(T,I[i][1])
            tmp_max_1=0
            max_el=(0,0)
            for el in k:
                if tmp_max_1<el[1]:
                    max_el=el
            tree_remove(T,max_el)
            tree_remove(T,I[i])
            tree_insert(T,(min(I[i][0],max_el[0]),max_el[1]))
            tab_to_ret[i]=max(tab_to_ret[i-1],max_el[1]-min(I[i][0],max_el[0]))
        elif (right and not left):
            #Teraz mamy wybrac maksymalny przedzial z returna intersection
            k=tree_intersect(T,I[i][0])
            min_el=[999,0]
            for el in k:
                if min_el[0]>el[0]:
                    min_el[0]=el[0]
                    min_el[1]=el[1]

            tree_remove(T,min_el)
            tree_remove(T,I[i])
            tree_insert(T,(min_el[0],max(I[i][1],min_el[1])))
            tab_to_ret[i]=max(tab_to_ret[i-1],max(I[i][1],min_el[1])-min_el[0])

        elif not left and not right:
            k=tree_intersect(T,I[i][1])
            max_el=[0,-9999]
            for el in k:
                if max_el[1]<el[1]:
                    max_el[0]=el[0]
                    max_el[1]=el[1]
            tree_remove(T,max_el)
            tree_remove(T,I[i])
            tree_insert(T,(min(I[i][0],max_el[0]),max_el[1]))
            LeftSide=(min(I[i][0],max_el[0]),max_el[1])
            k=tree_intersect(T,I[i][0])
            min_el=[999,0]
            for el in k:
                if min_el[0]>el[0]:
                    min_el[0]=el[0]
                    min_el[1]=el[1]
            tree_remove(T,min_el)
            tree_remove(T,I[i])
            tree_insert(T,(min_el[0],max(I[i][1],max_el[1])))
            #tree_print(T)
            tab_to_ret[i]=max(tab_to_ret[i-1],max(I[i][1],max_el[1])-min_el[0])
    return tab_to_ret






# uruchamia bazowe testy uzywajac funkcji intervals do obliczania wyniku
# wypisuje na koncu "OK!" jesli testy zaliczone
run_tests(intervals)





