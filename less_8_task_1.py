import re

PARS_EMAIL = re.compile(r'^\w*@\w\.(ru|com|bk)$')

def email_pars(email_adress):
    dict_email = {}

    try:
        if PARS_EMAIL.match(email_adress):
            res = re.split(r'@', email_adress)
            dict_email['username'] = res[0]
            dict_email['login'] = res[1]
        else:
            raise ValueError

    except ValueError:
        return print(f'ValueError: wrong email: {email_adress}')

    return dict_email

if __name__ == '__main__':

    print(email_pars(input('Input any Email Adress: ')))





