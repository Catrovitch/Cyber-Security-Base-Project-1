



def validate_login(username, password, account):

    if username == account.username and password == account.password:
        return True
    
    return False