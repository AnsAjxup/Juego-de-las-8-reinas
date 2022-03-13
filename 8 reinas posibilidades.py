#numero de reinas que se utilizaran
n=8
contador = 0
columna = [False]*n
diagonal_izquierda = [False]*(n*2)
diagonal_derecha = [False]*(n*2)


#función recursiva que lleva el conteo de posibilidades
def backtrack(y,n,contador):
    if(y==n):
        #retorna
        return contador + 1
    
    for x in range(n):
        
        global columna
        global diagonal_izquierda
        global diagonal_derecha
        
        if(columna[x] or diagonal_izquierda[x+y] or diagonal_derecha[x-y+n-1]): 
            continue
        #inicamos colocando una reina
        columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = True
        #enviamos la fila siguiente
        contador = backtrack(y+1,n,contador)
        #quitamos la reina para probar otras posibilidades
        columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = False
        
    return contador

#imprime el numero de posibilidades          
print(backtrack(0,n,contador))