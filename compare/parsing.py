from bs4 import BeautifulSoup
import urllib.request

def foo(userA, userB):
    url = "http://www.spoj.com/users/"
    list1 = doo(url + userA)
    list2 = doo(url + userB)
    listf = []
    for i in list2:
        flag = 0
        for j in list1:
            if i == j:
                flag = 1
                break
        if flag == 0:
            listf.append(i)
    return listf


def doo(page):
    url = urllib.request.urlopen(page)
    s = url.read()
    soup = BeautifulSoup(s)
    all_tables = soup.find('table', class_="table table-condensed")
    lister = []
    if all_tables is not None:
        hello = all_tables.find_all('a')
        for hi in hello:
            temp = hi.getText()
            if temp is not '':
                lister.append(temp)
    return lister
