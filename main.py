# # ipaddress 모듈의 속성
# import binascii
# import ipaddress as ipa
#
# Addresses = ['192.168.0.5',
#              '2001:0:9d38:6abd:480:f1f:3f57:fffb']
#
# for ipaddr in Addresses:
#     addr = ipa.ip_address(ipaddr)
#     print(f'IP address: {addr!r}')
#     print('IP version:', addr.version)
#
# class Car:
#     def __init__(self, color, speed):  # 초기화 메소드
#         self.color = color  # 인스턴스 변수 정의
#         self.speed = speed
#
#     def speedUp(self, v):  # 가속 메소드. 1번째 매개변수는 self
#         self.speed = self.speed + v
#         return self.speed
#
#     def speedDown(self, v):
#         self.speed = self.speed - v
#         return self.speed
#
# c1 = Car('black', 50)
# c2 = Car('red', 70)
# print('Car c1 : color = %s, speed = %d' % (c1.color, c1.speed))
# print('Car c2 : color = %s, speed = %d' % (c2.color, c2.speed))
# c1.speedDown(10)  # 차 c1의 속도 10만큼 감속
# print('Car c1 : speed = %d' % c1.speed)
#
# class People:
#     def __init__(self, age=0, name=None):
#         self.__age = age  # 클래스 안에서 만든 변수의 이름 앞에 __를 넣으면 외부에서 읽거나 변경하지 못함
#         self.name = name
#
# p1 = People(20, 'Kim')
# print(p1.name)
# print(p1.__age)
#
# # 공용 인터페이스만 제공하고 구현의 세부사항을 감추는 것을 캡슐화 라고 한다.
# # 감춘 인스턴스 변수값을 알고 싶거나 바꾸고 싶을때 사용하도록 접근자와 변숫값을 설정하는 설정자를 구현하는 것이 좋다
#
# class People :
#     def __init__(self, age=0, name=None):
#         self.__age = age
#         self.__name = name
#
#     def getAge(self):
#         return self.__age
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self, age):
#         self.__age = age
#
#     def setName(self, name):
#         self.__name = name
#
# p1  = People(20, "Kim")
# print(p1.getName())
# print(p1.getAge())
#

# for i in range(10):
#     print(i, end=' ')
#
#
# f = open("text.txt", 'w')
# for i in range(1, 11):
#     data = "%d 번쨰 줄 입니다.\n" % i
#     f.write(data)
# f.close()
#
# while 1:
#     data = input()
#     if not data:
#         break
#     print(data)

# f = open("text.txt", 'r')
# data = f.read()
# print(data)
# f.close()