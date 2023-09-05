""""check good or bad word"""
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

def getdata():
    """GetToken"""
    with open('DataAnswer.json', "r", encoding="utf-8") as file:
        Data = json.load(file)
        train_x = Data["Text"]
        train_y = Data["Check"]
    return train_x, train_y

def check(word):
    """check word"""
    Train_X = getdata()[0]
    Train_Y = getdata()[1]
    vectorize = CountVectorizer(binary=True)
    Train_X_Vectors = vectorize.fit_transform(Train_X)

    clf_svm = svm.SVC(kernel='linear')
    clf_svm.fit(Train_X_Vectors, Train_Y)

    test_x = vectorize.transform([word])
    clf_svm.predict(test_x)
    print(clf_svm.predict(test_x))

check(input())
