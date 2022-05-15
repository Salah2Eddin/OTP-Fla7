import string
import random


def random_string():
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return ran