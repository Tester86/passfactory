import os
import random
import pyperclip
import base64

class Password:
    def __init__(self, sec_level, invalid_tokens):
        self.password = ""
        self.sec_level = sec_level
        invalid_caharc_set = set(invalid_tokens)
        invalid_characs = invalid_caharc_set
        all_characs = "abcdefghijklmopqrstuvwxyz1234567890!#_-"
        for i in all_characs:
            if i in invalid_characs:
                all_characs = all_characs.replace(i, "")
        self.characs = all_characs
    def generate(self):
        password = ""
        for i in range(self.sec_level*10):
            choice = random.choice(self.characs)
            if choice in password:
                continue
            else:
                password += choice
        self.password = password
        return self.password
    def copy(self):
        if self.password == "":
            raise Exception("You need to generate a password first")
        else:
            pyperclip.copy(self.password)
    def retrieve(self, elems):
        for i in elems:
            msg = i.encode()
            decoded = base64.b64decode(msg).decode()
            i = decoded
        return elems
    def save(self, filename):
        if os.path.exists(filename):
            f = open(filename, "r")
            content = f.read()
            content_list = content.split()
            f.close()
            if content_list == []:
                f = open(filename, "w")
                f.write(self.password + "\n")
                f.close()
            else:
                f = open(filename, "a")
                f.write(self.password + "\n")
                f.close()
        else:
            f = open(filename, "w")
            f.write(self.password + "\n")
            f.close()
    def stats(self):
        if self.password == "":
            raise Exception("You need to generate a password first")
        else:
            alpha = 0
            nums = 0
            specials = 0
            for i in self.password:
                if i.isalpha():
                    alpha += 1
                elif i.isdigit():
                    nums += 1
                else:
                    specials += 1
            return (alpha, nums, specials)
    def test(self):
        if self.password == "":
            raise Exception("You need to generate a password first")
        else:
            alpha, nums, specials = self.stats()
            grade_sum = alpha + nums + specials
            grade = grade_sum / 2.8
            if grade >= 6.0:
                return True
            else:
                return False


a = Password(2, "")
