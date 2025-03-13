#f = open('새파일.txt','a')
#result = f.write('문서에 저장되는 내용입니다.\n')
#print(result)
#print(len('문서에 저장되는 내용입니다.'))
#f.close()

f = open('새파일.txt')

#for line in f.readlines():
#    print(line)

# print(f.readline())
# while True:
#     line = f.readline()
#     print(line)
#     if not line :
#         break
# f.close

print(f.read())

f.cloes()
