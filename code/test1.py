from sklearn import tree #导入需要的机器学习库sklearn
from sklearn.datasets import load_wine#导入红酒数据集
from sklearn.model_selection import train_test_split#导入划分训练集和测试集的库train_test_split
import os#导入标准库os
wine=load_wine()#传入红酒数据集
Xtrain,Xtest,Ytrain,Ytest=train_test_split(wine.data,wine.target,test_size=0.3)#划分训练集和测试集，30%作为测试集，70%作为训练集
clf=tree.DecisionTreeClassifier(criterion="entropy")#实例化一个决策数模型
clf=clf.fit(Xtrain,Ytrain)#训练决策树模型
score=clf.score(Xtest,Ytest)#返回预测准确度score
print(score)#打印预测准确度score
#定义main函数
def main():
    # Loading input values
    print("::debug::Loading input values")
    development = os.environ.get("INPUT_DEVELOPMENT", default=None)#获取环境变量development
    mode = os.environ.get("INPUT_MODE", default=None)#获取环境变量mode
    print(development)#打印环境变量development，没有输入故为空
    print(mode)#打印环境变量mode，选择mode='development',故打印结果为development
#调用main函数   
if __name__ == "__main__":
    main()

