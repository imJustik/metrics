from flask import Flask
from flask import request
import statsd
containerName = 'graphite'
port = 8125

app = Flask(__name__)
graphite = statsd.StatsClient(containerName, port)

@app.route('/test', methods=['POST'])
def updateCoverage():
    value = request.form['value']
    graphite.gauge("test", value)
    return "", 200

@app.route('/')
def mainPage():
    return "Hello world"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
