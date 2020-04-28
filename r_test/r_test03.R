# Title     : TODO
# Objective : TODO
# Created by: wang gang
# Created on: 2020/4/25

Sys.setlocale("LC_ALL","Chinese") # 设置中文字符集---但是没用
library(ggplot2) # 加载包
rm(list = ls()) # 清空变量
dat <- data.frame( # 赋值
  time = factor(c("Lunch","Dinner"), levels=c("Lunch","Dinner")),
  total_bill = c(14.89, 17.23)
)
print("dat数据为：")
print(dat)

ggplot(data=dat, aes(x=time, y=total_bill, fill=time)) +
geom_bar(stat="identity")

print(ggplot)

