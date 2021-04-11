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




