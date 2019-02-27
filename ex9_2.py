'''
Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]
'''


import requests
import sys
from bs4 import BeautifulSoup


def main():
    nodes = []
    resp = requests.get('https://ketqua.net/')
    tree = BeautifulSoup(resp.text)
    for i in range(1, 8):
        node = tree.find('td', attrs={'id': 'rs_{}_0'.format(i)})
        nodes.append(int(node.text))
    for node in nodes:
        if int(my_number[-2:]) == int(str(node)[-2:]):
            Prize = nodes.index(node)
            Prize_number = node
            break
        else:
            Prize = "Wish you best of luck"
    if Prize == "Wish you best of luck":
        print(Prize, nodes)
    else:
        print('You win a lottery')
        print(Prize + 1, Prize_number)


if __name__ == '__main__':
    my_number = ''.join(sys.argv[1:])
    if len(my_number) == 5:
        main()
    else:
        print('You have to input 5 numbers of a lottery')
