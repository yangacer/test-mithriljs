from threading import Thread
from time import sleep
from datetime import datetime
from flask import Flask
from flask import jsonify

app = Flask(__name__)

data = []

stop_thd = False

def insert():
    while not stop_thd:
      data.append({ 'ts': str(datetime.now()) })
      sleep(2)
    pass

@app.route("/data/")
def last_10():
    return jsonify(list=data[-10:][::-1])


if __name__ == "__main__":
    thd = Thread(target=insert)
    thd.start()
    app.run(debug=True)
    stop_thd = True
