import hashlib
import re



# usage:
# c = Complexity('password')
# c.test_password_complexity() -> bool

# can also do 
# c.spaces()


class Complexity(object):
    def __init__(self, password):
        self.password = password


    # def test_password_complexity(val: str) -> bool:
    #     if 8 > len(val) or len(val) > 32:
    #         return False
    #     return True


    def length(val: str) -> bool:
        return 8 <= len(val) <= 32

    def spaces(val) -> bool:
        if val[0] == ' ' or val[len(val) - 1] == ' ':
            return False

        # Ensure no carriage return, linefeed, /, \
        for idx in range(len(val)):
            if chr(13) == val[idx] or chr(10) == val[idx] or '/' == val[idx] or '\\' == val[idx]:
                return False
        return True

    def consecutiveChars(val) -> bool:
        # no more than two identical consecutive chars, numbers ok though
        for idx in range(len(val) - 2):
            if val[idx] == val[idx + 1] and val[idx + 1] == val[idx + 2]:
                return False
        return True

    def upperLower(val) -> bool:
        return re.search('[A-Z]', val) is not None and re.search('[a-z]', val) is not None

    def number(val) -> bool:
        return re.search('[1-9]', val) is not None

    def special(val) -> bool:
        return re.search('[!@#$%&*()]', val) is not None

    def hash_input_sha256(val) -> bool:
        return hashlib.sha256(val.encode()).hexdigest()
    
    # def test_password_complexity(password) -> bool:        
    #     return selflength(password) and self.spaces(self.password) \
    #         and self.upperLower(self.password) and self.number(self.password)\
    #         and self.consecutiveChars(self.password) and self.special(self.password)
