# #f = open('새파일.txt','a')
# #result = f.write('문서에 저장되는 내용입니다.\n')
# #print(result)
# #print(len('문서에 저장되는 내용입니다.'))
# #f.close()

# f = open('새파일.txt')

# #for line in f.readlines():
# #    print(line)

# # print(f.readline())
# # while True:
# #     line = f.readline()
# #     print(line)
# #     if not line :
# #         break
# # f.close

# print(f.read())

# f.close()

#-----------------------------

import json

data = {'name':'홍길동','age':'22'}
with open('myinfo.json','w') as f:
    json.dump(data,f,indent=2,ensure_ascii=False)

with open('myinfo.json') as f:
    data = json.load(f)

print(type(data))
print(data)

#-----------------------------

import pickle

data = {'name':'홍길동','age':'22'}

with open('myinfo.pickle','wb') as f:
    pickle.dump(data,f)

with open('myinfo.pickle','rb') as f:
    data = pickle.load(f)

print(type(data))
print(data)
