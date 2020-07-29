# my_file= open ('Test.txt')
# print (my_file.read())
# my_file.seek(0)
# print (my_file.read())
# my_file.seek(0)
# print (my_file.readline())
# print (my_file.readline())
# print (my_file.readline())
# print (my_file.readlines())
# my_file.close()
try:
    with open('sad.txt', mode='x') as my_file:
        # text = my_file.write(':(')
        # text= my_file.write('hey it\'s me')

        print(my_file.read())
        # print(text)
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err
