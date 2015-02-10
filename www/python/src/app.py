#!/usr/bin/env python2.7

# Thanks to Kunal Mehta for assistance, including the fab library.
from flask import Flask, request, Response
from flask.ext.jsonpify import jsonify

import logging, phabricator, json

with open('config.json') as f:
    conf = json.load(f)

phab = phabricator.Phabricator(conf['PHAB_HOST'], conf['PHAB_USER'], conf['PHAB_CERT'])

app = Flask(__name__)

"""
Returns status information for the given task IDs, supporting JSONP
"""
@app.route("/queryTasks")
def queryTasks():
    return jsonify(phab.request('maniphest.query', {
        'ids': json.loads(request.args.get('ids'))
    }))

if __name__ == '__main__':
    app.run()
