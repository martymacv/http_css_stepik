import hashlib
import sys


image_name = sys.argv[1]


def hash_20_chars(text):
    # SHA-1 дает 40 hex символов, обрезаем до 20
    return hashlib.sha1(text.encode()).hexdigest()[:20]


hashed = hash_20_chars(image_name)
print(hashed)
