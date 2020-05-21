from datetime import datetime
from flask import Flask, Response
import json
app = Flask(__name__)


@app.route('/getTime')
def index():
    now = datetime.now().today()
    _year = now.year
    _month = now.month
    _day = now.day
    _hour = now.hour
    _min = now.minute
    _sec = now.second

    time = {
        "hour": formatNum(_hour),
        "min": formatNum(_min),
        "sec": formatNum(_sec),
        "day": formatNum(_day),
        "month": formatNum(_month),
        "year": formatNum(_year),
    }
    print(time)
    return json.dumps(time)


def formatNum(num):
    if num < 10:
        return "0{}".format(num)
    else:
        return (num)
