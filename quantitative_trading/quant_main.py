# -*- coding: utf-8 -*-

# 引入自己定义的模块文件
from quantitative_trading import test01_quant_low #导入自定义模块中的文件/类



# 量化交易主方法

# 基于Black - Scholes 公式的期权定价公式
# 参数
spot = 2.45 # 当前价
strike = 2.50 # 行权价
maturity = 0.25 # 到期期限
r = 0.05 # 无风险利率
vol	= 0.25 # 波动率


qm = test01_quant_low.QuantFirstClass()
s = qm.call_option_pricer(spot,strike,maturity,r,vol)

print('原始价格',s)
print('期权价格 : %.4f' % s) # % 可做数据的转换，这里是转换数据的精确度，保留4位有效数字