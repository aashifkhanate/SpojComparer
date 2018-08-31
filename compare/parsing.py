from bs4 import BeautifulSoup
import urllib.request


def foo(userA, userB):
    user1 = "http://www.spoj.com/users/" + userA
    user2 = "http://www.spoj.com/users/" + userB

    list1 = doo(user1)
    list2 = doo(user2)
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


def moo(page):
    url = urllib.request.urlopen(page)
    s = url.read()
    soup = BeautifulSoup(s)
    harshit = soup.find('h2', class_="text-center").getText()
    # print(harshit)
    return harshit


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
                url_prob = "http://www.spoj.com/problems/" + temp + '/'
                lister.append(temp)

    return lister

# print (foo('aashifkhanate', 'yatind01'))
