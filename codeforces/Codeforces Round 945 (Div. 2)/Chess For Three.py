def chess(p1, p2, p3):
    draws=0
    total_points = p1 + p2 + p3
    lista = [p1, p2, p3]
    if total_points % 2 != 0:
        return -1
    while lista[1]!=0:
        lista.sort()
        if lista[0] == 0:
            lista.delete(0)
        
    
    
    
def elinar0(lista):
    lista = [x for x in lista if x != 0]
    return lista    

t = int(input())
for i in range(t):
    p1, p2, p3 = map(int, input().split())
    max_draws = chess(p1, p2, p3)
    print(max_draws)
#code sin arreglar