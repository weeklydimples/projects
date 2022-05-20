import time

username = 'brittany'
password = 'password'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access granted')
    print('Please wait')
    time.sleep(5)
    print('Ok... Loading...')
    time.sleep(3)
    print('...')
    time.sleep(5)
    print('...')
    time.sleep(5)
    print('Alright you have security clearance. Pulling up the secret mainframe.')
    time.sleep(4)
    print('...')
    time.sleep(5)
    print('Just Kidding!!')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('You might wanna check both fields...')
