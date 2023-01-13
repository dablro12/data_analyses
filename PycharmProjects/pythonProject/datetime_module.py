import datetime
#datetime 모듈은 날짜와 시간을 다루는 다양한 클래스를 가지고 있는 라이브러리임

#datetime.datetime(yyyy, mm, dd, hh, mm, ss) : 연월일 및  시간을
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day) #-> <class 'datetime.datetime'>
print(type(pi_day)) #-> <class 'datetime.datetime'>

pi_day = datetime.datetime(2022, 11, 19, 1, 52, 30)
print("지금 시각은 : {}".format(pi_day))

#datetime.datetime.now() 만약 지금 시간을 받아오고 싶을때
today = datetime.datetime.now()
print("지금 시각은 : {}".format(today))

#datetime.timedelta(date = 숫자, hours = 숫자, minutes = 숫자, second = 숫자) : 두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺼셈하듯이 뱨면 됨
today = datetime.datetime.now()
pi_day = datetime.datetime(2022, 11, 18, 1, 55, 55)
print("현재로부터 어제의 날짜 시간 비교 : {}".format(today-pi_day))
print(type(today-pi_day)) #-> <class 'datetime.timedelta'>
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
#5일 3시간 10분 55초 차이를 알고 싶을때
print(today)
print(today+my_timedelta)

#datetime 해부하기
today = datetime.datetime.now() #변수로 써서 만들어주어야함
#또는 datetime.datetime.now().month now의 () 뺴면안됨
print(today) #오늘
print(today.year) #년
print(today.month) #월
print(today.day) #일
print(today.hour) #시
print(today.minute) #분
print(today.second) #초
print(today.microsecond) #마이크로초
print(datetime.datetime.now().month)

#datetime 포맷팅 : strftime("%A, %B %dth %Y") A는 요일(영어로) B는 월(영어로) d는 일, Y는 연도
today = datetime.datetime.now()
# %Y : 년
# %B : 월(영어로)
# %d : 일
# %H : 시
# %M : 분
# %S : 초
print(today)
print(today.strftime("%Y-%B-%d %H:%M:%S" ))