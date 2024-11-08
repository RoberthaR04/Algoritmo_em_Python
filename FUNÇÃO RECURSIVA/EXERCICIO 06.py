#positivos k e n e calcule kn
def potencia(k,n):
        if n == 0:
            return 1
        elif n == 1:
            return k
        else:
            return k*potencia(k,n-1) 

print(potencia(2,0))

