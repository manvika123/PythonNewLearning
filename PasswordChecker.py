import re
pattern= re.compile(r"[A-Za-z0-9#@$%]{8,}\d")   #([A-Za-z0-9$%#@]{7,}[0-9])

password= 'jhdajhMAN12%$#j1'

check= pattern.fullmatch(password)
print (check)