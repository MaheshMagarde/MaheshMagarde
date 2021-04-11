'''
class hello:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        self.a = self.m1
        self.b = self.m1+self.m2
        self.c = self.m1+self.m2+self.m3
        return (self.a+self.b+self.c)/3
class Avg(hello):
    def Avg(self):
        pass
    mahesh
'''
'''
from HTMLParser import HTMLParser
import _markupbase
n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)
k = ''
for j in s:
    k += j


class MyHTMLParser1(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]} ')

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)



parser = MyHTMLParser1()
parser.feed(k)
'''
class Slope_Dist():                          #Completed

    def __init__(self,first_pt,sec_pt):
        self.sec_pt = sec_pt
        self.first_pt = first_pt

    def distance(self):
        r = []
        s = []
        r.append(self.first_pt[0])
        s.append(self.first_pt[1])
        r.append(self.sec_pt[0])
        s.append(self.sec_pt[1])

        dist = ((r[0]-r[1])**2 + (s[0]-s[1])**2)**0.5

        return dist
    def slope(self):
        r = []
        s = []
        r.append(self.first_pt[0])
        s.append(self.first_pt[1])
        r.append(self.sec_pt[0])
        s.append(self.sec_pt[1])
        slope = (s[1]-s[0])/(r[1]-r[0])
        # how to insert points example line1 = Slope_Dist((-4,-1),(2,-5))
        return slope

def sp_H():                 #It is HackerRank Prob. Draw H in special Way COMPLETED
    # Replace all ______ with rjust, ljust or center.

    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))

def lcm(x, y):  # completed
    if x > y:
        g = x
    if y > x:
        g = y
    while (True):
        if g % x == 0 and g % y == 0:
            a = g
            break
        g += 1
    return a

def common_factor(a, b):  # completed
    # Using place holder variable
    s = []
    t = []
    r = []
    x = int(a)
    y = int(b)
    for i in range(1, x):
        facx = x / i
        if int(facx) - facx == 0:
            s.append(facx)
    for j in range(1, y):
        facy = y / j
        if int(facy) - facy == 0:
            t.append(facy)
    for cm in s:
        for j in range(len(t)):
            A = t[j]
            if A == cm:
                r.append(A)
    return r

def prime(n):  # Completed
    if n == 1 or n == 0:
        return 'Not prime Nor Composite'
    elif n == 2:
        return 'Prime'
    elif n > 2:
        for i in range(2, n):
            if n % i == 0:
                return 'Composite'
            else:
                pass
        return 'Prime'

def persentage(*args, pers):  # pers means how many % you want to calculate
    h = sum(args) * (pers / 100)
    return h


def vol_spere(r): return 4 / 3 * (3.14) * r ** 3
def vol_cube(s): return s ** 3
def vol_cuboid(l, b, h): return l * b * h
def vol_hemisphere(r): return 2 / 3 * (3.14) * r ** 3
def vol_cylinder(r, h): return (3.14) * (r ** 2) * h
def vol_cone(r, h): return 1 / 3 * (3.14) * (r ** 2) * h

def area_square(s): return s ** 2
def area_rectangle(l, b): return l * b
def triangle(b, h): return (0.5) * b * h
def area_circle(r): return (3.14) * r ** 2

#no. of diagonals in the polygons side (n)
#sum of angles of tha polygons of side (n)
#def mode:

#def mean:

#def median:

#def sum_product(x+y,xy):              #find x and y



