# # import game.sound.echo
#
# game.sound.echo.echo_test()


# from game.sound import echo
#
# echo.echo_test()


# from game.sound.echo import echo_test
#
# echo_test()


# from game.sound import *
#
# echo.echo_test()


# from game.graphic.render import *
#
# render_test()

# from game.graphic import *
#
# render.render_test()

# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)
#
# try:
#     arr = [1, 2, 3]
#     count = arr[3]
# except IndexError as er:
#     print(er)

# class Bird:
#     def fly(self):
#         raise NotImplementedError  # 상속할 클래스들은 fly라는 함수를 무조건 만들게 하기 위한 것
#
# class Eagel(Bird):
#     pass
#
# eagle = Eagel()
# eagle.fly()


class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
