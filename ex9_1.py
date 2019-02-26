import requests
import json
import sys


def main():
	infos = sys.argv[1:]
	data = requests.get('https://api.github.com/users/pymivn/repos')
	repos = json.loads(data.text)
	for repo in repos:
		for info in infos:
			print(repo[info])


if __name__ == '__main__':
	main()