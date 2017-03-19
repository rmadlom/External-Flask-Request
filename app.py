#handle a POST request
from flask import Flask, render_template, request, url_for, jsonify, redirect, make_response
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    print("Index page hit...")
    return render_template("index.html")

@app.route('/do_foo/<data>', methods=['POST','GET'])
def do_foo(data):
    print("do_foo page hit...")
    print("Data: " , data)
    return render_template('index.html', data = data )


@app.route('/tests/endpoint', methods=['POST'])
def my_test_endpoint():
    # force=True, below, is necessary if another developer
    # forgot to set the MIME type to 'application/json'
    input_json = request.get_json(force=True)

    # response to server with datetime.now()
    response = 'Data Received: ' + str(datetime.now())
    print("response:", response)
    dictToReturn = {'Server response': response}

    #grabbing 'puzzle' from dict only
    print('data from client:', input_json)
    alarm = input_json['alarm']
    # below line is just for testing
    alarm = 'piano'
    data = {'Alarmtype': alarm}
    print("This is the Alarm value:", data)
    #return jsonify(dictToReturn)
    response = make_response(render_template('index.html', data=data))
    #return redirect(('index.html',response))
    print("Response: ", response)
    return redirect(url_for('do_foo',data=data))
    #return render_template('index.html', puzzle = data )

if __name__ == '__main__':
    app.run(host='192.168.1.90',debug=True)
