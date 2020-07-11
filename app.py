from flask import Flask
from flask import jsonify 
app = Flask(__name__)

@app.route('/')
def front():
    # Creating a multiline string
    multiline_str = "Hi from Flask API\n" \
    "- /examplejson\n" \
    "- /myfriends"
    return multiline_str
    

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

## My COMPLEX FUNCTION
@app.route('/aboutme')
def aboutme():
    about={
        'about':[{
        'name': 'swetank',
        'role': 'devops',
        'salary': '4 CTC',
        'skills': {
            'language': 'python',
            'CI': 'Jenkins',
            'CD': 'Ansible',
            'Frontend': 'React',
            'Backend': 'flask'
        }}],
        'gadgets': [
            {
               'type': 'laptop',
               'model':'mac book air'
            },
            {
               'type': 'phone',
               'model': 'iphone 11'
            }
        ]
    }
    return jsonify(about)

if __name__=="__main__":
    app.run(debug=True)