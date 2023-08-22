import random
import string

material = string.ascii_letters + string.digits + string.punctuation

length = 8

password = "".join(random.sample(material, length))

print(password)