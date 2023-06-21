#Euclid's Algorithm with Python

def GDC(a,b):

    if b == 0:
        return a
    else:
        return GDC(b,a % b)
    

print(GDC(40,6))