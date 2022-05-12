
from Lions import Lion
from Tigers import Tiger
from Ligers import Liger
from Tigons import Tigon
from Farms import Farm
from Horses import Horse
from Donkeys import Donkey
from Mules import Mule


class Hipo(Farm):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)

    def makeNoise(self):
        print("POPOP")

    def printSize(self):
        print("HUGA")

    def __str__(self):
        return super().__str__()


def met(x, y, g):
    L = Lion(g, True)
    TG = Tigon(g, False)
    LG = Liger(g, False)
    T = Tiger(g, True)
    H = Horse(g, True)
    D = Donkey(g, True)
    M = Mule(g, False)
    E = "ERROR"
    I = "INVALID INPUT"
    if type(x)  not in(type(L),type(T),type(LG),type(TG),type(H),type(D),type(M)):
        return I
    elif type(y)  not in(type(L),type(T),type(LG),type(TG),type(H),type(D),type(M)):
        return I
    if (x.getisMale() and not y.getisMale()) and (x.getisFertile() and y.getisFertile()):
        if type(x) == type(y):
            if (type(x) == type(L)) and (type(y) == type(L)):
                return L
            elif type(x) == type(T) and type(y) == type(T):
                return T
            elif type(x) == type(H) and type(y) == type(H):
                return H
            elif type(x) == type(D) and type(y) == type(D):
                return D
            elif type(x) == type(LG) and type(y) == type(LG):
                return LG
            elif type(x) == type(TG) and type(y) == type(TG):
                return TG
            elif type(x) == type(M) and type(y) == type(M):
                return M
        elif type(x) != type(y):
            if type(H) in (type(x), type(y)) and type(D) in (type(x), type(y)):
                return M
            elif type(L) in (type(x), type(y)) and type(T) in (type(x), type(y)):
                return LG
            if type(T) in (type(x), type(y)) and type(L) in (type(x), type(y)):
                return TG
            else:
                return E
    else:
        return E


a = Horse(True, True)
b = Donkey(False, True)

new_baby = met(a, b, True)
print("type a and b")
print(type(a))
print(type(b))

print("type new baby")
print(type(new_baby))
print(new_baby)
new_baby.makeNoise()
new_baby.gallop()
