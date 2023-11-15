from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for testing POST request
sample_data = {
    "name": "John Doe",
    "age": 25,
    "city": "New York"
}

# GET API
@app.route('/', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET request."})

# POST API
@app.route('/api/post', methods=['POST'])
def post_data():
    # Get JSON data from the request
    data = request.get_json()

    # Process the data (you can do more complex operations here)
    result = {"message": "This is a POST request.", "data_received": data}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
