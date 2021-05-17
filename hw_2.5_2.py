import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
	'fhjhafhdfa.txt']

a = open(random.choice(names), 'w+')
# print(a)


def func(lst):
    for i in lst:
        try:
            f = open(i, 'r+')
        except FileNotFoundError:
            print("Такого файла не существует")
        else:
            f.write('Abdimusa')
func(names)
