def add(n1:int ,n2:int):
    if isinstance(n1,str) or isinstance(n2,str):
        return None
    return n1 + n2

def subtract(n1,n2):
    if isinstance(n1,str) or isinstance(n2,str):
        return None
    return n1 - n2

def multiply(n1,n2):
    if (isinstance(n1,str) or isinstance(n2,str)):
        return None
    return (n1 * n2)