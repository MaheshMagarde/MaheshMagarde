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
import matplotlib.pyplot as plt
import numpy as np
import random as rm

class Slope_Dist_Graph():                          #Completed

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

        return  dist
    def slope(self):
        r = []
        s = []
        r.append(self.first_pt[0])
        s.append(self.first_pt[1])
        r.append(self.sec_pt[0])
        s.append(self.sec_pt[1])
        slope = (s[1]-s[0])/(r[1]-r[0])

        return slope
    def graph(self):
        x = np.arange(0,100)
        y = (self.slope() * (x - self.first_pt[0])) + self.first_pt[1]
        plt.plot(x,y)
        plt.show()
        # line1 = Slope_Dist((1,2),(2,3))

def enycryption(Sentance):
    Translation = ''
    for i in Sentance:
        if i in 'Aa': Translation+='#'
        elif i in 'Bb': Translation+='~'
        elif i in 'Cc': Translation += '`'
        elif i in 'Dd': Translation +='!'
        elif i in 'Ee': Translation +='ṇ'
        elif i in 'Ff': Translation +='?'
        elif i in 'Gg': Translation += '/'
        elif i in 'Hh': Translation +='ā'      # ctrl + alt + a = ā
        elif i in 'Ii': Translation += '₹'        # ctrl + alt + 4 = ₹
        elif i in 'Jj': Translation +='%'
        elif i in 'Kk': Translation +='^'
        elif i in 'Ll': Translation +='&'
        elif i in 'Mm': Translation +='*'
        elif i in 'Nn': Translation +='-'
        elif i in 'Oo': Translation +='_'
        elif i in 'Pp': Translation +='æ'      #ctrl + alt + q = æ
        elif i in 'Qq': Translation +='ē'      #ctrl + alt + e = ē
        elif i in 'Rr': Translation +='|'
        elif i in 'Ss': Translation +=';'
        elif i in 'Tt': Translation +='/'
        elif i in 'Uu': Translation +='r̥'       #ctrl + alt + r = r̥
        elif i in 'Vv': Translation +='ū'      #ctrl + alt + u = ū
        elif i in 'Ww': Translation +='<'
        elif i in 'Xx': Translation +='>'
        elif i in 'Yy': Translation +=','
        elif i in 'Zz': Translation +='$'
        else: Translation+Sentance
    print('Please copy that code:',Translation)

def sp_H():
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

def factors(n):
    s=[n]
    even_fac = []
    for i in range(1,n):
        if n%i==0:
            s.append(i)
    for j in s:
        if j%2==0:
                even_fac.append(j)
    print(f'No. of factors are {len(s)}')
    print(f'Even No. of factors {len(even_fac)}\nOdd No. of Factor {(len(s))-(len(even_fac))}')
    print(s)

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

def Read_my_mind():
    hlf = rm.randrange(0, 1000, 10)
    print("Hello....!Can i read your mind..... I think Yes\nThink any number in your mind")
    YN = input("If done write 'YES':")
    if YN in 'YESYesyes':
        print("Now double that in your mind")
        A = input("If done write 'YES':")
        if A in 'YESYesyes':
            print(f"Now Add {hlf} on that number")
            B = input("If done write 'YES':")
            if B in 'YESYesyes':
                print("Now divide that number by 2")
                C = input("If done write 'YES':")
                if C in 'YESYesyes':
                    print("Now you rember which number you think Substract that number by present number")
                    D = input("If done write 'YES':")
                    if D in 'YESYesyes':
                        print(f"Now, Multiply that number by 5 and your answer is {int((hlf / 2) * 5)}.")
                        print('I Prove you i will able to read your mind If ans is wrong pls try again')
                    else: print("If you not remember please exit and run again")
                else: print('If not able to devide use calculator or try again')
            else: print("Please Exit and Run again")
        else: print("Think small number and run again or use Calculator")
    else: print("Think and run again")

Read_my_mind()

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
def area_triangle(b, h): return (0.5) * b * h
def area_circle(r): return (3.14) * r ** 2

#POLYGONS
def Angle_sum(n): return (n-2)*180                     #Sum of angles of tha polygons of side (n)
def Diagonals_Num(n): return int((n*(n-3))/2)          #Number of diagonals
#def mode:

#def mean:

#def median:

#def sum_product(x+y,xy):              #find x and y



