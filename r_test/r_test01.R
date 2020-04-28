# Title     : TODO
# Objective : TODO
# Created by: wang gang
# Created on: 2020/4/21
# r测试
# r的基本操作


a <- array(c('green','yellow'),dim = c(3,3,2))
# c()将元素组合成向量，向量是基本数据类型，许多原子向量可组成数组
print(a)

#因子
apple_colors <- c('green','green','yellow','red','red','red','green')
factor_apple <- factor(apple_colors)

print(factor_apple)
print(nlevels(factor_apple))

#数据帧
BMI <- data.frame(
	gender = c("Male","Male","Female"),
	heighe = c(152,171.5,165),
	weight = c(81,93,78),
	Age = c(42,38,26)
)
print(BMI)

#变量类型
var_x <- "hello"
cat("var_x type",class(var_x),"\n")

var_x <- 34.5
cat("var_x type",class(var_x),"\n")

var_x <- 27L
cat("var_x type",class(var_x),"\n")

#查看环境中的变量
print(ls())

#删除变量
rm(list = ls())
print(ls())

#饼装图
# Create data for the graph.
x <- c(11, 30, 39, 20)
labels <- c("70后", "80后", "90后", "00后")
pie(x,labels)#直接显示

#存储图片
# Give the chart file a name.
png(file = "birth_of_age.jpg")

# Plot the chart.
pie(x,labels)

# Save the file.
dev.off()

#获取图片的存储路径
getwd()

#不存储图片画直方图
H <- c(7,12,28,3,41)
barplot(H)#条状图

#箱型图--错误
input <- mtcars[,c('mpg','cyl')]
print(head(input))

png(file = "bosplot.png")
boxplot(mpg ~ cyl,data = mtcars,xlab = "气缸数"，
	ylab = "没加仑里程"，main = "里程数据")

dev.off()

#箱型图
x <- c(35, 41, 40, 37, 43, 32, 39, 46, 32, 39, 34, 36, 32, 38, 34, 31)
f <- factor(rep(c("试验组","对照组"), each=8)) #定义分组因子
data<- data.frame(x,f) #生成数据框
boxplot(x~f,data)

#散点图
#setwd("F:/worksp/R")
# Get the input values.
input <- mtcars[,c('wt','mpg')]

# Give the chart file a name.
png(file = "scatterplot.png")

# Plot the chart for cars with weight between 2.5 to 5 and mileage between 15 and 30.
plot(x = input$wt,y = input$mpg,
   xlab = "重量",
   ylab = "里程",
   xlim = c(2.5,5),
   ylim = c(15,30),
   main = "重量 VS 里程"
)

# Save the file.
dev.off()

#R画图
x <- c(1,2,3,4)
y <- x*x
jpeg(file = "plot.jpg")#保存图像
plt <- plot(x,y) #画散点图
dev.off()
getwd()











