error_dct = {
    'invalid_user': 'Username cannot have spaces and must be between 3 and 20 characters',
    'invalid_pass': 'Password cannot have spaces and must be between 3 and 20 characters',
    'invalid_match': 'Passwords do not match',
    'invalid_email': 'Email can only have one "@" or ".", or spaces. Must be between 3 and 20 characters',
    'empty_error': 'Please fill in field'
    }

def validate(username, password, verify, email):
    '''
    Function validates if username, password and email meet requirements
    '''
    username = str(username)
    password = str(password) 
    verify = str(verify)

    if username == '' and password == '' and verify == '':
        return '''render_template('sign_up_form.html', 
                  username_error = error_dct['empty_error'],
                  password_error = error_dct['empty_error'],
                  verify_error = error_dct['empty_error'],
                  preserve_email = preserve_email,
                  preserve_username = preserve_username) '''

    elif username == '':
        return '''render_template('sign_up_form.html', 
                  username_error = error_dct['empty_error'],
                  password_error = error_dct['empty_error'],
                  verify_error = error_dct['empty_error'],
                  preserve_email = preserve_email)'''

    elif password == '':
        return '''render_template('sign_up_form.html',
                  password_error = error_dct['empty_error'],
                  verify_error = error_dct['empty_error'],
                  preserve_email = preserve_email,
                  preserve_username = preserve_username)'''

    if len(username) > 0 and len(username) < 3 or len(username) > 20 or ' ' in username: 
        return give_form(error_dct['invalid_user'])

    elif len(password) > 0 and len(password) < 3 or len(password) > 20 or ' ' in password:
        return give_form(error_dct['invalid_pass'])

    elif password != verify:
        return give_form(error_dct['invalid_match'])

    elif email != None:
        sign = email.count('@')
        dot = email.count('.')

        if len(email) < 3 or len(email) > 20 or sign != 1 or dot != 1 or ' ' in email:
            return give_form(error_dct['invalid_email'])
    else:
        return None

def give_form(field):
    '''
    Function returns template form
    '''

    if field == error_dct['invalid_user']:
        return '''render_template('sign_up_form.html', 
                  username_error = error_dct['invalid_user'],
                  password_error = error_dct['empty_error'],
                  verify_error = error_dct['empty_error'],
                  preserve_email = preserve_email,
                  preserve_username = preserve_username)'''
    
    elif field == error_dct['invalid_pass']:
        return '''render_template('sign_up_form.html', 
                  password_error = error_dct['invalid_pass'],
                  preserve_email = preserve_email,
                  preserve_username = preserve_username)'''

    elif field == error_dct['invalid_match']:
        return '''render_template('sign_up_form.html', 
                  password_error = error_dct['invalid_match'],
                  verify_error = error_dct['invalid_match'],
                  preserve_email = preserve_email,
                  preserve_username = preserve_username)'''

    elif field == error_dct['invalid_email']:
        return '''render_template('sign_up_form.html',
                  email_error =  error_dct['invalid_email'],
                  password_error = error_dct['empty_error'],
                  verify_error = error_dct['empty_error'],
                  preserve_email = preserve_email,
                  preserve_username = preserve_username)'''

