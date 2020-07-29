import random


class Password:
    def ps_gen(self, length):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*/?abcdefghijklmnopqrstuvwxyz"
        # Generates a randon pw from the string 's'
        pw = "".join(random.sample(s, length))
        return pw
