"""generate word"""
import json
from bardapi import Bard
import viewlog

@viewlog.log_return_value
def opentoken():
    """GetToken"""
    with open("Token.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["tokenGenword"]

@viewlog.log_return_value
def generate():
    """generate"""
    opentoken()
    bard = Bard(token=opentoken())
    output = bard.get_answer("สุ่มประโยค 1 ประโยคสำหรับคุยกับเพื่อนเป็นภาษาไทย")
    outputcontent = output["content"]
    if '"' in outputcontent:
        extracted_word = outputcontent.split('"')[1]
        #print(extracted_word)
        return extracted_word
    else:
        return "กรุณาลองใหม่"

#generate()
