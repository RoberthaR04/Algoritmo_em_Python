def mult(x,y):
    if y == 0:
        return x
    else:
        return x+mult(x,y-1)
    
print(mult(x,y))