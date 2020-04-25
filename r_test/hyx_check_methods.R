# Title     : TODO
# Objective : TODO
# Created by: wang gang
# Created on: 2020/4/25

# 小胡的r脚本

#基本检验

my_data <- PlantGrowth
####内置数据集
#正态性检验

# QQ图法
qqnorm(my_data$weight)#画图
qqline(my_data$weight)

#Shapiro-Wilk(W检验)
shapiro.test(my_data$weight)

#KS检验：可检验样本数据符合某一分布,适合大样本
#若有重复值，会报错，此时应该加上jitter

ks.test(jitter(my_data$weight),"pnorm",mean(my_data$weight),sd(my_data$weight))
#nortest包里的lillie.test()可以实行更精确的Kolmogorov-Smirnov检验
library(nortest)
lillie.test(my_data$weight)


#方差齐性检验

#Bartlett检验：参数检验，适合于正态总体
bartlett.test(weight ~ group,data = my_data)
#Levene检验：参数检验，适合于非正态总体（car包）
leveneTest(weight ~ group,data = my_data)
#Fligner-Killeen检验：非参数检验
fligner.test(weight ~ group,data = my_data)


#独立性检验

#游程检验
library(lawstat)
runs.test(my_data$weight,plot.it = T)
