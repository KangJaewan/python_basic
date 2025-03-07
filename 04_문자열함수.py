# a = 'hobby'
# print(a.count('b'))

# 이메일 주소를 입력받습니다. 입력시 ***@** 형태입니다.
# 입력받아서 아이디만 출력해 주세요.
# 이메일 주소는 최소 5글자를 넘어야 됩니다. 
# 최대 20글자까지 가능합니다. 
# 반드시 글자 중간에 @ 문자가 포함되어야 합니다. 
# input()을 이용하여 입력을 받습니다. 
# 받은 값은 email 이름의 변수에 저장됩니다. 
# email에 저장되어 있는 값에서 Index()를 이용하여 @의 위치를 확인합니다. 
# 찾은 위치값은 index라는 이름으로 저장합니다. 
# print()를 이용하여 email의 값에서 
# 처음부터 index에 저장되어 있는 값까지 슬라이싱 합니다. 
# 슬라이싱 한 값을 data 변수에 저장합니다. 
# data변수에 있는 값을 print()를 이용해서 출력합니다.

email = input(" 이메일 주소를 입력하세요 >>> ")
print('값은 5~20 범위에서',len(email))
print('값은 1이 나와야됨',email.count('@'))
index = email.index('@')
data = email[:index]
print(data)

# 주민등록번호를 입력받아서 다음을 출력해 줍니다. 
# 성별(남자,여자)
# 생년월일(00년 2월 1일생)
# 뒷자리 숫자를 첫글자는 그대로 나머지는 *로 변경해서 출력 
# 입력시 글자 앞, 뒤로 공백이 포함될 수 있습니다. 공백에 대한 처리도 하세요.

resident_number = input("주민등록번호를 입력하세요 (예: 000101-1234567): ").strip()
parts = resident_number.split("-")


gender_code = parts[1][0]  # 성별 코드 (주민번호 뒷자리 첫 번째 숫자)


# 성별 판별 (문자열 메소드만 사용)
gender = "남자" * (int(gender_code) % 2) + "여자" * ((int(gender_code) + 1) % 2)


birth_info = f"{parts[0][:2]}년생 {int(parts[0][2:4])}월 {int(parts[0][4:6])}일생"


masked_back = parts[0] + "-" + parts[1][0] + "+" * 6


print(f"성별: {gender}")
print(f"생년월일: {birth_info}")
print(f"뒷자리: {masked_back}")