'''
Viết script lấy top **N** câu hỏi được vote cao nhất của
tag **LABEL** trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs
'''


import requests
import sys
from bs4 import BeautifulSoup


def main():
    N = int(sys.argv[1])
    resp = requests.get('https://stackoverflow.com/questions?sort=votes')
    tree = BeautifulSoup(resp.text)
    nodes = []
    nodes = tree.findAll('a', {'class': 'question-hyperlink'})
    i = 1
    while len(nodes) < N:
        i += 1
        link = 'https://stackoverflow.com/questions?sort=votes{}'.format(i)
        resp = requests.get(link)
        tree = BeautifulSoup(resp.text)
        nodes += tree.findAll('a', {'class': 'question-hyperlink'})
    nodes = nodes[:N]
    print(nodes)
    for node in nodes:
        print(node.text)
        print('https://stackoverflow.com' + node.get_attribute_list('href')[0])


if __name__ == '__main__':
    main()
