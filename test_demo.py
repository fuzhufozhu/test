import random
import time
list_es = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
list_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sett = set()

start = time.time()

while True:
    es = random.sample(list_es, 2)
    num = random.sample(list_num, 4)
    nums = es + num
    ls = ''.join(nums)
    sett.add(ls)
    if len(sett) == 10000:
        print('运行时间:{}'.format(time.time() - start))
        break


print(sett)