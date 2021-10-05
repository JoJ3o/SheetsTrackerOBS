from os import truncate
import gspread
from pprint import pprint
import math
import json

def getName(name):
        newName = name.split("] ")
        return newName[1]

def getBest(time: str):
    if ":" in time:
        split = time.split(":")
        time = int(split[0]) * 60 + float(split[1])
    return float(time)

def getTarget(best):
    target = round(best/0.95, 2)
    strippedTarget = math.floor(target * 10) / 10
    lastDecimal = round(target - strippedTarget, 2)
    if lastDecimal >= 0.06:
        newTarget = strippedTarget + 0.06
    elif lastDecimal >= 0.03:
        newTarget = strippedTarget + 0.03
    else:
        newTarget = strippedTarget + 0.00

    minutes = 0
    for _x in range(math.floor(newTarget/60)):
        newTarget = newTarget-60
        minutes += 1

    if minutes == 0:
        displayMin = ""
    elif minutes > 0:
        displayMin = str(minutes) + ":"
    return displayMin + str(format(newTarget, '.2f'))

def getPB(pb):
    if pb == None:
        pb = "??"
    return str(pb)

def main():
    client = gspread.service_account("creds.JSON")

    sheet = client.open_by_key(
        "1Xb0L8hFKLIjhku-ZycmoSZU-1UNu3Mi5y07IxVD5nU4").sheet1

    name = ""
    target = ""
    pb = ""

    val = sheet.find("x")
    if val:
        if val.col == 6 and sheet.cell(val.row, 2).value != None:
            name = getName(sheet.cell(val.row, 1).value)
            target = getTarget(getBest(sheet.cell(val.row, 2).value))
            pb = getPB(sheet.cell(val.row, 5).value)
    
    pprint(name + " | " + target + " | " + pb)
    data = {"name": name, "target": target, "pb": pb}
    return data


if __name__ == '__main__':
    main()
