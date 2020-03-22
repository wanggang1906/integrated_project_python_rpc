# -*- coding: utf-8 -*-
# 基于Black - Scholes 公式的期权定价公式
from math import log, sqrt, exp
from scipy.stats import norm
import time
import numpy as np
from matplotlib import pylab
import seaborn as sns # 基于matplotlib的数据可视化库

class QuantFirstClass(object):

    _spo0t =	2.45 # _XX 表示保护成员，不能用from moudle import *导入
    __strik0e	= 2.50 # __XX 表示私有成员，只有类对象能访问，子类也不能访问，但在对象外部可通过 对项名._类名__XX 访问
    __maturit0y__ = 0.25 # __XX__ 表示系统定义的特殊成员

    # 欧式期权的简单计算
    def call_option_pricer(self,spot, strike, maturity, r, vol):
        d1 = (log(spot/strike) + (r + 0.5 * vol *vol) * maturity) / vol / sqrt(maturity)
        d2 = d1 - vol * sqrt(maturity)
        price = spot * norm.cdf(d1) - strike * exp(-r*maturity) * norm.cdf(d2)
        return price

    #
    def use_numpy_speed(self,sport,maturity,r,vol):
        portfolioSize = range(1,10000,500)
        timeSpent = []

        for size in portfolioSize:
            now = time.time()
            strikes = np.linspace(2.0,3.0,size)
            for i in range(size):
                res = self.call_option_pricer(self,sport,strikes[i],maturity,r,vol)
                timeSpent.append(time.time() - now)

    def show_time_difference(self,font,portfolioSize,timeSpent):
        font.set_size(15)
        sns.set(style="ticks")
        pylab.figure(figsize=(12,8))
        pylab.bar(portfolioSize,timeSpent,color = 'r',width=300)
        pylab.grid(True)
        pylab.title(u'期权计算时间耗时（单位：秒）',fontproperties = font,fontsize = 18)
        pylab.ylabel(u'时间（s）',fontproperties = font,fontsize = 15)
        pylab.xlabel(u'组合数量',fontproperties = font,fontsize = 15)

if __name__ == "__main__":
    # 当.py文件被直接运行时，if _name_ == '_main_'之下的代码块将被运行；
    # 当.py文件以模块形式被导入时，if _name_ == '_main_'之下的代码块不被运行
    qm = QuantFirstClass()

