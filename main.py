def recursive_str(str):
    if len(str) == 0:
       return str

    else:
        return recursive_str(str[1:]) + str[0] 
    

#print(recursive_str("hello world"))



def power4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if (n % 4)==0:
        return power4(n/4)
print(power4(64))    