from flask import Flask
from flask import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    
    logging.info("Status endpoint was reached")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":1,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
   
    logging.info("mertics endpoint was reached")
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG , filemode='w', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    app.run(host='0.0.0.0')
