import bcrypt
def verify_password(input_password, stored_hashed_password):
    input_bytes = input_password.encode('utf-8')      
    stored_hash_bytes = stored_hashed_password.encode('utf-8')
    return bcrypt.checkpw(input_bytes, stored_hash_bytes) 
