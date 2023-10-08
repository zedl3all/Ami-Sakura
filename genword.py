"""generate word"""
import json
from bardapi import BardCookies
import viewlog


@viewlog.log_return_value
def opentoken():
    """GetToken"""
    with open("Token.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        PSID = data["__Secure-1PSID"]
        PSIDTS = data["__Secure-1PSIDTS"]
        PSIDCC = data["__Secure-1PSIDCC"]
    return PSID,PSIDTS,PSIDCC

@viewlog.log_return_value
def generate():
    """generate"""
    cookie_dict = {
    "__Secure-1PSID": opentoken()[0],
    "__Secure-1PSIDTS": opentoken()[1],
    "__Secure-1PSIDCC": opentoken()[2],
    # Any cookie values you want to pass session object.
    }
    bard = BardCookies(cookie_dict=cookie_dict)
    output = bard.get_answer("สุ่มประโยค 1 ประโยคสำหรับคุยกับเพื่อนเป็นภาษาไทย")
    outputcontent = output["content"]
    if '"' in outputcontent:
        extracted_word = outputcontent.split('"')[1]
        print(extracted_word)
        return extracted_word
    else:
        return "ขอเวลาแปป :heart_hands:"

#generate()
