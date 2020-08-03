try:
    import random
except ModuleNotFoundError:
    print('Module not found. Please run pip install -r requirements.txt to install it.')
    exit()


def ps_gen(length=1):
    """
    Generates a randon pw from the string 's'
    """
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*/?abcdefghijklmnopqrstuvwxyz"
    pw = "".join(random.sample(s, length))
    return pw
