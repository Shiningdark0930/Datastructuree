# 과제 3


import re

text = input("텍스트를 입력하세요:")

emails = re.findall('[a-zA-Z0-9]\S+@[a-zA-Z0-9.]+[a-zA-Z]', text)

if len(emails) == 0:
    print("이메일 주소가 발견되지 않았습니다.")
else:
    print("추출된 이메일 주소:")
    for email in emails:
        print(email)
    