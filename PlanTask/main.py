def PlanType(m, T):
    p1 = "private"
    p2 = "Boing"
    if m <= 200:
        if T in ("1", "b"):
            TypeP = p2
        else:
            TypeP = p1
    elif 200 < m < 220:
        TypeP = p2
    else:
        return "Invalid number"

    return TypeP


def Distance(d):
    if d <= 100:
        return 100
    elif 100 < d <= 200:
        return 200
    else:
        print("distance to long")
        return d


def dis(tic, lug, c):
    if tic > 200:
        return f"{tic} price not valid"
    res = 0
    if lug <= 20:
        d = tic * 0.20
        res = tic - d
        print("discount luggage of 20% =", res)
    elif 20 < lug < 40:
        d = tic * 0.25
        res = tic - d
        print("discount luggage of 25% =", res)
    else:
        d = tic * 0.30
        res = tic - d
        print("discount luggage of 30% =", res)
    if c in ("1", "b"):
        d = res * 0.05
        res -= d
        print("discount on class of 5% =", res)
    else:
        d = res * 0.01
        res -= d
        print("discount on class of 1% =", res)
    return res


ticket = Distance(int(input("Enter ticket price")))
luggage = int(input("Enter luggage kg : "))
c = input("What your class: ")

print(dis(ticket, luggage, c))
