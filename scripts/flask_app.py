from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def welcome():
    if request.method=='GET':
        return "Hello Worlds!"
    else:
         return jsonify({'name':'Isaac',
                    'address':'Addis Ababa, Ethiopia'})

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
