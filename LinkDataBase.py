"""Linkdata"""
from datetime import datetime
import gspread
import viewlog

@viewlog.log_return_value
def add_data(userid):
    """add_data"""
    gsaccount = gspread.service_account("botdiscord-it-21-dcf1ea9eb41f.json")
    sheet = gsaccount.open("Data_Bot")
    worksheet = sheet.worksheet("Data")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    new_data = [str(userid), 0, 0, current_time, False]
    last_row_number = len(worksheet.col_values(1)) + 1
    for i, value in enumerate(new_data):
        worksheet.update_cell(last_row_number, i + 1, value)
    #print(worksheet.get_all_values())

@viewlog.log_return_value
def check_data(userid):
    """checkdata"""
    gsaccount = gspread.service_account("botdiscord-it-21-dcf1ea9eb41f.json")
    sheet = gsaccount.open("Data_Bot")
    worksheet = sheet.worksheet("Data")
    if str(userid) in worksheet.col_values(1):
        return True
    else:
        return False
        #print("you have id")
    #print(worksheet.col_values(1))

@viewlog.log_return_value
def update_like_data(userid, likevalue):
    """update like data"""
    gsaccount = gspread.service_account("botdiscord-it-21-dcf1ea9eb41f.json")
    sheet = gsaccount.open("Data_Bot")
    worksheet = sheet.worksheet("Data")
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow+1
        likedata = worksheet.row_values(userrow)[1]
        worksheet.update_cell(userrow, 2, str(int(likevalue)+int(likedata)))

#update_like_data(str(415728832574914562),1)
