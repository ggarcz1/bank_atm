import hashlib
import re

class Complexity(object):
    def __init__(self, password):
        self.password = password

    def length(val):
        return 8 <= len(val) <= 32

    def spaces(val):
        if val[0] == ' ' or val[len(val) - 1] == ' ':
            return False

        # Ensure no carriage return, linefeed, /, \
        for idx in range(len(val)):
            if chr(13) == val[idx] or chr(10) == val[idx] or '/' == val[idx] or '\\' == val[idx]:
                return False
        return True

    def consecutiveChars(val):
        # no more than two identical consecutive chars, numbers ok though
        for idx in range(len(val) - 2):
            if val[idx] == val[idx + 1] and val[idx + 1] == val[idx + 2]:
                return False
        return True

    def upperLower(val):
        return re.search('[A-Z]', val) is not None and re.search('[a-z]', val) is not None

    def number(val):
        return re.search('[1-9]', val) is not None

    def special(val):
        return re.search('[!@#$%&*()]', val) is not None

    def hash_input_sha256(val):
        return hashlib.sha256(val.encode()).hexdigest()

    # def test_password_complexity(self):        
    #     return self.length(self.password) and self.spaces(self.password) \
    #         and self.upperLower(self.password) and self.number(self.password)\
    #         and self.consecutiveChars(self.password) and self.special(self.password)
    
    def test_password_complexity(self):        
        return self.length(self.password) and self.spaces(self.password) \
            and self.upperLower(self.password) and self.number(self.password)\
            and self.consecutiveChars(self.password) and self.special(self.password)


