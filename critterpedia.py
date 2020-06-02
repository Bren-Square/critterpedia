from bugs import Blist
from datetime import datetime
from fish import Flist
from flask import jsonify
from flask import request
from flask_restful import Resource, reqparse


def get_time():
    timestamp = datetime.now()
    mth = int(timestamp.month)
    hr = int(timestamp.hour)
    return mth, hr


def iterate(month, hour, critter):
    final_list = []
    for i in critter.entry:
        if month in i["Months"] and hour in i["Time"]:
            final_list.append(i)
    return final_list


class Health(Resource):
    def get(self):
        return 200


class Fish(Resource):
    def get(self):
        mth, hr = get_time()
        fish = Flist()
        final = iterate(mth, hr, fish)
        return jsonify(final)


class Bugs(Resource):
    def get(self):
        mth, hr = get_time()
        bugs = Blist()
        final = iterate(mth, hr, bugs)
        return jsonify(final)

