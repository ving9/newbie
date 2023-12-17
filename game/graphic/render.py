# render.py
# from game.sound.echo import echo_test
from ..sound.echo import echo_test
# relative 접근자 : 모듈 안에서만 사용 (.. = 부모 디렉토리 의미)

def render_test():
    print("render")
    echo_test()

