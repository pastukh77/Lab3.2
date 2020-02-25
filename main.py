import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


def main(TWITTER_URL: str):
    '''
    This fuction prints element of json Twitter file by API and lets you
    to move forward and back in json file.
    '''

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    print('')
    acct = input('Enter Twitter Account:')

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    j = js
    lst = []
    while True:

        if isinstance(j, dict):
            print(j.keys())
            obj_input = input('Choose the key: ')
            lst.append(j)
            if obj_input == '<':
                j = lst[lst.index(j) - 1]
            elif obj_input == '/':
                print('Good luck!')
                break
            else:
                try:
                    try:
                        j = j[obj_input]
                        if j == js:
                            lst.clear()
                    except TypeError:
                        continue
                except KeyError:
                    print('Please, choose the correct key')
            print('')
        elif isinstance(j, list):
            print(j)
            obj_input = input('Enter a number of list: ')
            lst.append(j)
            if obj_input == '<':
                j = lst[lst.index(j) - 1]
                if j == js:
                    lst.clear()
            elif obj_input == '/':
                print('Good luck!')
                break
            else:
                try:
                    j = j[int(obj_input)]
                except ValueError:
                    print('Please, choose the correct index')
            print('')
        else:
            print(j)
            print('This is final object')

            obj_input = input('If you want to go back, please enter "<", or if you want to quit, enter "/" : ')
            lst.append(j)
            if obj_input == '<':
                j = lst[lst.index(j) - 1]
            elif obj_input == '/':
                print('Good luck!')
                break

            else:
                print('Please, choose another option')

            print('')

if __name__ == '__main__':
    main(TWITTER_URL)

