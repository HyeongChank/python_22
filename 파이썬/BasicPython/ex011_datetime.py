# datetime
import datetime
now = datetime.datetime.now()
print(now.year,"년")
print(now.month)
print(now.day)
print(now.hour,"시", now.minute,"분", now.second,"초")

if now.hour < 12:
    print("현재 시각은 {}시 {}분로 오전입니다".format(now.hour, now.minute))
if now.hour >= 12:
    print("현재 시각은 {}시 {}분로 오후입니다".format(now.hour, now.minute))
    
a = now.month
if 3 <= int(a) <= 5:
    print("이번 달은 {}월로 봄이다".format(a))
if 6 <= int(a) <= 8:
    print("이번 달은 {}월로 여름이다".format(a))
if 9 <= int(a) <= 11:
    print("이번 달은 {}월로 가을이다".format(a))    
if a == 12 or 1 <= int(a) <= 2:
    print("이번 달은 {}월로 겨울이다".format(a))
