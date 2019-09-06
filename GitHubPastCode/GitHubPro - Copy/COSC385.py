def IsDigit(a):
    x = int(a)  #input("Enter your number")
    if (x / 1 == x):
        return ("Yes")


def IsPossitive(a):
    x = a
    if (int(x) >= 0):
        return ("Yes")


def checkBin(a):
    p = set(a)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        return ("Yes")

    else:
        return ("No")


a = input("inter a unsigned number:")


def all(a):
    if (IsDigit(a == True)):
        if (IsPossitive(a == True)):
            if (checkBin(a) == 'Yes'):
                return " This is an unsigned (integer or real) number"
            else:
                return (" this is not an unsigned (integer or real) number")
        else:
            return (" this is not an unsigned (integer or real) number")
    else:
        return (" this is not an unsigned (integer or real) number")


print(all(a))
