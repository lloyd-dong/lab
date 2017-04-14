#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

# import sys
# print sys.argv[1:]

# from datetime import datetime
# import logging

# logging.basicConfig(filename="w.log",level=logging.INFO)

# log = logging.getLogger(__name__)

# log.info("{} first ".format(datetime.now()))


# with open("heathrow-cli.txt", "a") as f:
# 	f.write("{} : ".format(datetime.now()))
# 	f.write( '; '.join(sys.argv[1:]))
# 	f.write("\n")