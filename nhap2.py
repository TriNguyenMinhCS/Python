str = input()
import re
m = re.findall(r'\d', str)
print(m)
r = ''.join(m)
print(r)
