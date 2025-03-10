## 명함관리 프로그램
# 1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료

import sys 

display = '''
-----------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-----------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ""
namecard = [['강재완','111-222-3333','부산','kang@gmail.com'], ['홍길동','333-4444-5555','서울','hong@gmail.com']]

while True:
  menu = input(display)
  if menu == '1':
    print('명함입력')
    name = input(' 이름 >>> ')
    tel = input(' 전화번호 >>> ')
    address = input(' 주소>>> ')
    while True:
     email = input(' 이메일 >>> ')
     check = 0 # 이메일이 존재하는지 확인하는 변수
     for index in range(len(namecard)):
     #for index, card in enumerate(namecard)
      if namecard[index][3] == email :
        check = 1 # 이메일이 존재하면 1로 변경
        break
     if check == 0:
        break
    namecard.append([name,tel,address,email])
    print(namecard)
  elif menu == '2':
    print('명함수정')
    email = input('수정할 데이터의 이메일을 선택')
    check = 0
    for index in range(len(namecard)):
     if namecard[index][3] == email :
       check = 1
       while True:
         item = input('수정할 항목을 선택하세요(1.이름 2.전화번호 3.주소 4.종료)')
         if item == '4' :
           break
         item = int(item)
         if item in (1,2,3):
           namecard[index][item-1] = input('수정할 값을 입력 >>> ')
    if check == 0 :
        print('No Data')
  elif menu == '3':
    print('명함삭제')
    email = input('삭제할 데이터의 이메일을 입력 >>> ')
    check = 0
    for index in range(len(namecard)):
     if namecard[index][3] == email :
       check = 1
       print('삭제 >>>', namecard.pop(index))
    if check == 0 :
      print('No data')
  elif menu == '4':
    print('명함목록보기')
    print('='*55)
    for card in namecard:
      print(f'{card[0]:10},{card[1]:15},{card[2]:10},{card[3]:10}')
    print('='*55)
  elif menu == '5':
    print('프로그램 종료')
    sys.exit()
  else:
    print('메뉴선택을 잘못하셨습니다.')