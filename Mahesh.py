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