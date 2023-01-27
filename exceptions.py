from math import sqrt

# 1.PERIMETER OF RECTANGLE
def perimetercalc(w: int, h: int):
    if w < 0:
        raise ValueError("The given width %d is negative" %w)
    if h < 0:
        raise ValueError("The given height %d is negative" %h)

    return 2*(w+h)
def execute_perimeter():
    try:
        print("Lets calculate the perimeter of a rectangle. ")
        w = int(input("Enter the width: "))
        h = int(input("Enter the height: "))
        p = perimetercalc(w, h)
        print("The perimeter is %d" %p)
    except ValueError as err:
        print("Invalid input: %s" %err)

# 2.SQUARE ROOT
def calc_sqrt(k: float):
    if k < 0:
        raise ValueError("The number %d you provided is invalid"%k)
    return sqrt(k)
def execute_sqrt():
    try:
        k = float(input("What number do you want to find the square root for? "))
        a = calc_sqrt(k)
        print("The square root of ",k," is %e"%a)
    except ValueError as error:
        print("Invalid input: %s"%error)

# 3. DIVIDE BY MANY
def div_by_many(p:float, qs: list):
    list = []
    for q in qs:
        if q == 0:
            raise ValueError("Index " + str(qs.index(q)) + " in list is 0")
        list.append(p/q)
    print(list)
    return list



