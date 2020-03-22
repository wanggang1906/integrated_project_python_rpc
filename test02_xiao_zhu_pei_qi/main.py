import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


import turtle as t # 画图工具库,python内置


from test02_xiao_zhu_pei_qi import bizi
from test02_xiao_zhu_pei_qi import head
from test02_xiao_zhu_pei_qi import ear
from test02_xiao_zhu_pei_qi import eyes
from test02_xiao_zhu_pei_qi import sai
from test02_xiao_zhu_pei_qi import mouse
from test02_xiao_zhu_pei_qi import body
from test02_xiao_zhu_pei_qi import hands
from test02_xiao_zhu_pei_qi import legs

#from legs import draw_legs
#from weiba import draw_weiba
# 导入模块中的文件，通过文件.方法调用里面的方法
from test02_xiao_zhu_pei_qi import weiba



def main():
    """
    主函数
    :return: null
    """
    t.pensize(4)
    t.colormode(255)
    t.color((255, 155, 192), "pink")
    t.setup(840, 500)
    t.speed(10)

    bizi.draw_bizi()
    head.draw_head()
    ear.draw_ear()
    eyes.draw_eyes()
    sai.draw_sai()
    mouse.draw_mouse()
    body.draw_body()
    hands.draw_hands()
    # draw_legs()
    legs.draw_legs()
    #draw_weiba()
    weiba.draw_weiba()
    t.exitonclick()


if __name__ == '__main__':
    main()
