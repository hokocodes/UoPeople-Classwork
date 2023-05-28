def is_divisible(a, b): #function for finding if a is divisible by b
    if a % b == 0:
        return True
    else:
        return False



def is_power(a, b): #function for finding if a is the power of b
    if (b==0) or (b==1) : # base case
        return True
    elif is_divisible(a, b) and is_power(a/b, b) == True: #recursion
        return True
    else:
        return False
    

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
