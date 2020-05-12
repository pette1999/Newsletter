import gspread
import authentication

def getList():
    json_file_name = 'daily-newsletter-3f8ed4c4331e.json'
    credential = authentication.authenticate(json_file_name)
    gc = gspread.authorize(credential)
    wks = gc.open("Clients").sheet1

    values_list = wks.col_values(1)
    return values_list


def writeList(value_list, value):
    json_file_name = 'daily-newsletter-3f8ed4c4331e.json'
    credential = authentication.authenticate(json_file_name)
    gc = gspread.authorize(credential)
    wks = gc.open("Clients").sheet1

    wks.update_cell(len(value_list)+1, 1, value)

def emailInput():
    email = input("Please input your email here: ")
    writeList(getList(), email)
