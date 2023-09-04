"""CheckWord"""
import json
from pythainlp import word_tokenize

def openjson():
    """OpenJson"""
    with open("Badword.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["Badword"], data["Goodword"]

def checkword(word, badword = openjson()[0], goodword = openjson()[1]):
    """Checkword"""
    score = 0
    spitword = set(word_tokenize(word))
    spitword = list(spitword)
    for i in spitword:
        print(i)
        if i in badword:
            score -= 5
        elif i in goodword:
            score += 1
    print(score)
    return score

checkword(word=str(input()))
