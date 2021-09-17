from os import truncate
import gspread
from pprint import pprint
import math

client = gspread.service_account("creds.JSON")

sheet = client.open_by_key(
    "1kbRlOoLOxN7SjcmdpmXNVo9KiVPsGNNRXrFZ_gV28RE").sheet1


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

    return str(format(newTarget, '.2f'))


val = sheet.find("x")

name = sheet.cell(val.row, 1).value
best = float(sheet.cell(val.row, 2).value)
target = getTarget(best)
pb = sheet.cell(val.row, 3).value

pprint(name + " | " + target + " | " + pb)
