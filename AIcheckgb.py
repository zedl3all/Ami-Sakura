""""check good or bad word"""
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import viewlog

@viewlog.log_return_value
def getdata():
    """GetToken"""
    with open('DataAnswer.json', "r", encoding="utf-8") as file:
        Data = json.load(file)
        train_x = Data["Text"]
        train_y = Data["Check"]
    return train_x, train_y

@viewlog.log_return_value
def check(word):
    """check word"""
    Train_X = getdata()[0]
    Train_Y = getdata()[1]
    vectorize = CountVectorizer(binary=True)
    Train_X_Vectors = vectorize.fit_transform(Train_X)

    clf_svm = svm.SVC(kernel='linear')
    clf_svm.fit(Train_X_Vectors, Train_Y)

    test_x = vectorize.transform([word])
    output = clf_svm.predict(test_x)
    print(output)
    score = 0
    if output == "Good":
        score = 1
    elif output == "Bad":
        score = -5
    return score
#check("สวัสดี")
