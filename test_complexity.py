from complexity import Complexity

password = 'qwerty'

c = Complexity(password)

print(c.test_password_complexity() == False)
c = Complexity('HEll12!@3ls')
print(c.test_password_complexity() == True)

