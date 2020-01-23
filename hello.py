import hashlib
password = "hello world"
hash_value = hashlib.md5(password).hexdigest()
