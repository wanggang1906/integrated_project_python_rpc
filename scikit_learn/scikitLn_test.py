# -*- coding: utf-8 -*-
from sklearn import neighbors,datasets,preprocessing
from sklearn.model_selection import train_test_split

# 网上的例子
# 来源 https://blog.csdn.net/qq_27150893/article/details/80169736
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#SVM模型实现汽车性能评测
car_data = pd.read_csv(r'..\DataSet\scilit_learn\car.csv')
car_data = car_data.dropna() #去掉缺失值
#提取特征和类别
X= car_data.ix[:, :'safety']
y= car_data.ix[:,'class']
#划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# 建立模型。 设置算法内核类型，有 'linear’, ‘poly’, ‘rbf’, ‘sigmoid’;惩罚参数为1，一般为10的幂次方
svc_model = svm.SVC(kernel='rbf', C= 1)
svc_model.fit(X_train, y_train)
predict_data = svc_model.predict(X_test)
accuracy = np.mean(predict_data==y_test)
print(accuracy)



def scTest():
    iris = datasets.load_iris()
    x, y = iris.data[:, :2], iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler.transform(X_test)
    knn = neighbors.KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    # accuracy_score(y_test,y_pred) # 准确性分析