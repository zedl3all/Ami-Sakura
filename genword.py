"""generate word"""
import json
import time
from bardapi import Bard

start = time.time()

def opentoken():
    """GetToken"""
    with open("Token.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["tokenGenword"]

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
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
