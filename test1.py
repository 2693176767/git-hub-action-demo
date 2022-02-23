from sklearn import tree #导入需要的模块
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
wine=load_wine()
Xtrain,Xtest,Ytrain,Ytest=train_test_split(wine.data,wine.target,test_size=0.3)#30%作为测试集，70%作为训练集
clf=tree.DecisionTreeClassifier(criterion="entropy")
clf=clf.fit(Xtrain,Ytrain)
score=clf.score(Xtest,Ytest)#返回预测准确度accuracy
print(score)
print(enviorment)
