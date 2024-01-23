'''
CIS 122 Spring 2022 Project 8-2
Author(s): Steven Sanchez-Jimenez
Credit: CIS 122 Resources, Office Hours, Annika Huston
Description: Password Checker, Creating a password with
requirements and limitations
'''

import doctest

def uppercase(p):
    '''(
    u: str) -> bool

    return True if any char in u is uppercase
    otherwise return False
    
    >>> uppercase('CIS122')
    True
    
    >>> uppercase('Ducks')
    True
    
    >>> uppercase('ducks')
    False
    '''
    
    for ch in p:
        if ch.isupper():
            return True
    return False #good

def digit(p):
    '''
    checks for at least one digit

    >>> digit('qwerty')
    False
    
    >>> digit('qwerty4')
    True
    '''

    for di in p:
        if di.isdigit():
            return True
    return False 

def char_ct(p):
    '''
    checks if password meets required length (6 characters)

    >>> char_ct('Duck')
    False

    >>> char_ct('duckies')
    True

    >>> char_ct('fadf$')
    False
    '''
    if len(p) >= 6:
        return True
    else:
        return False #good

def spec_char_check(p):
    '''
    checks for special characters in password
    
    >>> spec_char_check('qwert$')
    True

    >>> spec_char_check('qwErtS')
    False

    >>> spec_char_check('Qwrty')
    False
    '''
    i = '!@#$%^&'
    for x in p:
        if x in i:
            return True
    return False

def echeck(p):
    '''
    checks for 'e' or 'E' in password
    
    >>> echeck('qwerty')
    False

    >>> echeck('qwErty')
    False

    >>> echeck('Qwrty')
    True
    '''
    
    for x in p:
        if x == 'E':
            return False
        if x == 'e':
            return False
    return True

def password_check(p):
    '''
    checks if password (p) meets all password requirements
    
    >>> password_check('A99#!')
    False
    
    >>> password_check('')
    False
    
    >>> password_check('#Qwerty')
    False
    
    >>> password_check('#qwerty')
    False
    
    >>> password_check('Qwerty99')
    False
    
    >>> password_check('123456')
    False
    
    >>> password_check('#Qwzrty')
    False
    
    >>> password_check('#Qw9rty')
    True
    
    >>> password_check('OK99!!')
    True
    '''
    
    if not uppercase(p):
        return False
    elif not digit(p):
        return False
    elif not char_ct(p):
        return False
    elif not echeck(p):
        return False
    elif not spec_char_check(p):
        return False
    else:
        return True

print(doctest.testmod())

def main():
    '''
    driver for password_check
    '''

    while True:
        password = input('enter password: ')

        check = password_check(password)
        if check == True:
            print('password is valid')
            break
        else:
            print('password is not valid')

main()
