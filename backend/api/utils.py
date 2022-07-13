def base62_encode(num):
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    hash_str = ''

    while int(num) > 0:
        hash_str = s[int(num % 62)] + hash_str
        num = num / 62

    return hash_str

