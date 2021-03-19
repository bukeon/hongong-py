import datetime as dt

print("# 현재 시각 출력하기")
now = dt.datetime.now()

print(f"{now.year} 년")
print(f"{now.month} 월")
print(f"{now.day} 일")
print(f"{now.hour} 시")
print(f"{now.minute} 분")
print(f"{now.second} 초")
print( )

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = (f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초")
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()