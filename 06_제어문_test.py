import sys 

# 메뉴 출력 메시지
display = '''
-----------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-----------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ""  # 사용자 입력을 저장할 변수
# 초기 명함 데이터 (이름, 전화번호, 주소, 이메일)
namecard = [['강재완','111-222-3333','부산','kang@gmail.com'], ['홍길동','333-4444-5555','서울','hong@gmail.com']]

# 무한 루프를 통해 프로그램 실행
while True:
  menu = input(display)  # 사용자로부터 메뉴 선택 입력 받음
  
  if menu == '1':  # 명함 입력 기능
    print('명함입력')
    name = input(' 이름 >>> ')
    tel = input(' 전화번호 >>> ')
    address = input(' 주소>>> ')
    
    while True:
      email = input(' 이메일 >>> ')
      check = 0  # 중복 이메일 여부 확인 변수
      for index in range(len(namecard)):
        if namecard[index][3] == email:  # 이메일이 이미 존재하면
          check = 1  # 중복 확인 변수 변경
          break  # 중복 발견 시 루프 종료
      
      if check == 0:  # 이메일이 중복되지 않으면 입력 허용
        break
    
    # 새 명함 데이터를 리스트에 추가
    namecard.append([name, tel, address, email])
    print(namecard)  # 업데이트된 명함 리스트 출력
  
  elif menu == '2':  # 명함 수정 기능
    print('명함수정')
    email = input('수정할 데이터의 이메일을 입력 >>> ')
    check = 0  # 수정할 데이터 확인 변수
    
    for index in range(len(namecard)):
      if namecard[index][3] == email:  # 입력한 이메일이 존재하는 경우
        check = 1  # 데이터 존재 여부 확인
        
        while True:
          item = input('수정할 항목을 선택하세요(1.이름 2.전화번호 3.주소 4.종료)')
          if item == '4':  # 4 입력 시 수정 종료
            break
          item = int(item)
          if item in (1, 2, 3):  # 유효한 선택값인지 확인
            namecard[index][item-1] = input('수정할 값을 입력 >>> ')
    
    if check == 0:  # 해당 이메일이 존재하지 않는 경우
      print('No Data')
  
  elif menu == '3':  # 명함 삭제 기능
    print('명함삭제')
    email = input('삭제할 데이터의 이메일을 입력 >>> ')
    check = 0  # 삭제 여부 확인 변수
    
    for index in range(len(namecard)):
      if namecard[index][3] == email:  # 해당 이메일이 존재하는 경우
        check = 1  # 삭제할 데이터가 존재함을 확인
        print('삭제 >>>', namecard.pop(index))  # 해당 데이터를 리스트에서 제거
        break  # 삭제 후 루프 종료
    
    if check == 0:  # 해당 이메일이 존재하지 않는 경우
      print('No data')
  
  elif menu == '4':  # 명함 목록 보기 기능
    print('명함목록보기')
    print('='*55)
    for card in namecard:  # 명함 리스트 출력
      print(f'{card[0]:10},{card[1]:15},{card[2]:10},{card[3]:10}')
    print('='*55)
  
  elif menu == '5':  # 프로그램 종료
    print('프로그램 종료')
    sys.exit()  # 시스템 종료
  
  else:  # 잘못된 메뉴 입력 처리
    print('메뉴선택을 잘못하셨습니다.')