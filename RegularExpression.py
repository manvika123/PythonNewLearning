import re

string = 'search this in this string please Manvika?'
# print(re.search('this', string))  #<re.Match object; span=(10, 14), match='this'>
pattern = re.compile('search this in this string please')
# a= re.search('this', string)
# a= pattern.search('this')
# b= pattern.findall(string)
# c= pattern.fullmatch(string)
d = pattern.match(string)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())
# print(b)
# print(c)
print(d)
