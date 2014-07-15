from flask import Flask, request

import datetime

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/payload', methods=['POST', ])
def handle_payload():
    # write to file payload data
    filename = "payload-{}.json".format(datetime.datetime.now())
    with open(filename, "w") as f:
        f.write(request.data)
    
    return "Processed payload", 200


if __name__ == "__main__":
    app.run()
