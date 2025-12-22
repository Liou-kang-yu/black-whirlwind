import bcrypt
def hash_password(password):

    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()                   
    hashed_pw = bcrypt.hashpw(password_bytes, salt) 
    return hashed_pw.decode('utf-8') 
