from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/Knn-Sequential", methods=['POST'])
def Sequential():
    content = request.json
    print(content['message'])
    return jsonify({"message":content['message']})

@app.route("/Knn-RTree", methods=['POST'])
def RTree():
    return "<p>Hello, World!</p>"

@app.route("/Knn-HighD", methods=['POST'])
def HighD():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
