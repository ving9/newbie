# import sys
#
# args = sys.argv[1:]
# for i in args:
#     print(i)

class FourCal:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setdata(self, num1, num2):
        self.x = num1
        self.y = num2

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y

    def sub(self):
        return self.x - self.y

    def div(self):
        return int(self.x / self.y)



# temp = FourCal()
#
# temp.setdata(4, 2)
# print(temp.x)
# print(temp.y)
# print(temp.add())
# print(temp.mul())
# print(temp.sub())
# print(temp.div())



class MoreFourCal(FourCal):
    def pow(self):
        result = self.x ** self.y
        return result

box = MoreFourCal()

box.setdata(2, 4)
print(box.add())
print(box.pow())



class SafeFourCal(FourCal):
    def div(self):
        if self.y == 0:
            return 0
        else:
            return self.x / self.y

box = SafeFourCal()
box.setdata(2, 0)
print(box.div())


class Family:
    lastname = "park"

name = Family()

print(name.lastname)

name.lastname = "kim"

print(Family.lastname)
print(name.lastname)
# 변경한 객체에서 변수를 변경하면 새롭게 그객체만의 변수 생성 (클래스 변수와 중복되는 이름일 경우 그 변수를 덮어쓴다고 생각)




