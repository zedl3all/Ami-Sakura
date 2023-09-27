"""Linkdata"""
from datetime import datetime
import gspread
import viewlog

gsaccount = gspread.service_account("botdiscord-it-21-dcf1ea9eb41f.json")
sheet = gsaccount.open("Data_Bot")
worksheet = sheet.worksheet("Data")

@viewlog.log_return_value
def add_data(userid):
    """add_data"""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    new_data = [str(userid), 0, 0, current_time, False, False]
    last_row_number = len(worksheet.col_values(1)) + 1
    for i, value in enumerate(new_data):
        worksheet.update_cell(last_row_number, i + 1, value)
    #print(worksheet.get_all_values())

@viewlog.log_return_value
def check_data(userid):
    """checkdata"""
    if str(userid) in worksheet.col_values(1):
        return True
    else:
        return False
        #print("you have id")
    #print(worksheet.col_values(1))

@viewlog.log_return_value
def update_like_data(userid, likevalue):
    """update like data"""
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow + 1
        likedata = worksheet.row_values(userrow)[1]
        worksheet.update_cell(userrow, 2, str(int(likevalue)+int(likedata)))

#update_like_data(str(415728832574914562),1) #use for test add data

@viewlog.log_return_value
def get_time(userid):
    """get time"""
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow + 1
        latest_time = worksheet.row_values(userrow)[3]
        print(latest_time)
        return latest_time

#get_time(307804872408039424)#use for get time data

@viewlog.log_return_value
def get_active(userid):
    """get active"""
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow + 1
        active = worksheet.row_values(userrow)[4]
        print(active)
        return active

#get_active(307804872408039424)#use for get active data

@viewlog.log_return_value
def get_waiting_message(userid):
    """get active"""
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow + 1
        waiting = worksheet.row_values(userrow)[5]
        print(waiting)
        return waiting

#waiting_message(307804872408039424)#use for get waiting_message

@viewlog.log_return_value
def update_time(userid, value):
    """get time"""
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow + 1
        worksheet.update_cell(userrow, 4, value.strftime("%H:%M:%S"))

#update_time(307804872408039424, datetime.now())#use for update time data

@viewlog.log_return_value
def update_active(userid, value):
    """get active"""
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow + 1
        worksheet.update_cell(userrow, 5, bool(value))

#update_active(307804872408039424, True)#use for update active data

@viewlog.log_return_value
def update_waiting_message(userid, value):
    """get active"""
    if str(userid) in worksheet.col_values(1):
        userrow = worksheet.col_values(1).index(str(userid))
        userrow = userrow + 1
        worksheet.update_cell(userrow, 6, bool(value))

#update_waiting_message(307804872408039424, True)#use for update waiting_message
