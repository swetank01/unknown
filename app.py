from flask import Flask
from flask import jsonify 
app = Flask(__name__)

@app.route('/')
def front():
    return "Hi from Flask API"

@app.route('/examplejson')
def getjson():
    myjson={
        'key1':'value1',
        'key2':'value2'
    }
    return jsonify(myjson)

@app.route('/myfriends')
def myFriends():
    friendList={
        '0':'Swetank',
        '1':'Rishika',
        '2':'Sid',
        '3':'Akash',
        '4':'Bhalu',
        '5':'Deepu'
    }
    return jsonify(friendList)


if __name__=="__main__":
    app.run(debug=True)