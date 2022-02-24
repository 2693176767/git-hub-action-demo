#pip install sklearn
#from sklearn import tree #导入需要的模块
#from sklearn.datasets import load_wine
#from sklearn.model_selection import train_test_split
#import pytest
import os
#wine=load_wine()
#Xtrain,Xtest,Ytrain,Ytest=train_test_split(wine.data,wine.target,test_size=0.3)#30%作为测试集，70%作为训练集
#clf=tree.DecisionTreeClassifier(criterion="entropy")
#clf=clf.fit(Xtrain,Ytrain)
#score=clf.score(Xtest,Ytest)#返回预测准确度accuracy
#print(score)
def main():
    # Loading input values
    print("::debug::Loading input values")
    development = os.environ.get("INPUT_DEVELOPMENT", default=None)
    mode = os.environ.get("INPUT_MODE", default=None)
    
    # Casting input values
    #print("::debug::Casting input values")
    #try:
        #model_version = int(model_version)
    #except TypeError as exception:
        #print(f"::debug::Could not cast model version to int: {exception}")
        #model_version = None
    #except ValueError as exception:
        #print(f"::debug::Could not cast model version to int: {exception}")
        #model_version = None
    
if __name__ == "__main__":
    main()

