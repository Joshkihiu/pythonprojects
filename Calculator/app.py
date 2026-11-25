
# Flask is the framework that allows Python to communicate with a web browser.
# render_template allows us to display HTML pages.
# request allows us to receive information sent by the browser.
# jsonify converts Python data into JSON so JavaScript can understand it.
from flask import Flask, render_template, request, jsonify


# Create our Flask application.
# __name__ tells Flask where this Python file is located.
# Flask uses this information to find folders such as templates and static.
app = Flask(__name__)


# This is a route (URL path).
# When someone visits the homepage (http://127.0.0.1:5000/),
# Flask will execute the home() function below.
@app.route('/')
def home():

    # Look inside the templates folder and find index.html.
    # Flask will send that HTML page to the user's browser.
    return render_template('index.html')


# This route handles calculator requests.
# methods=['POST'] means this route accepts POST requests.
# A POST request is commonly used when sending data to a server.
@app.route('/calculate', methods=['POST'])
def calculate():

    # Get the JSON data sent by JavaScript.
    # For example, JavaScript might send:
    # {"num1": "10", "num2": "5", "operator": "+"}
    data = request.get_json()

    # Get num1 from the received JSON data.
    # float() converts the value into a decimal number.
    # For example, "10" becomes 10.0.
    num1 = float(data['num1'])

    # Get num2 and convert it into a decimal number too.
    num2 = float(data['num2'])

    # Get the operator (+, -, * or /) from the JSON data.
    # .get() retrieves a dictionary value using its key.
    operator = data.get('operator')

    # Check whether the user selected addition.
    if operator == '+':
        result = num1 + num2

    # If not addition, check whether the user selected subtraction.
    elif operator == '-':
        result = num1 - num2

    # If not subtraction, check whether the user selected multiplication.
    elif operator == '*':
        result = num1 * num2

    # If none of the above, check whether the user selected division.
    elif operator == '/':

        # Before dividing, check that the second number is not zero.
        # Division by zero is mathematically undefined.
        if num2 != 0:
            result = num1 / num2

        # If num2 is zero, send an error message to JavaScript.
        # 400 is an HTTP status code meaning the request was invalid.
        else:
            return jsonify({'error': 'Division by zero is not allowed.'}), 400

    # Convert our result into JSON and send it back to JavaScript.
    # For example: {"result": 15.0}
    return jsonify({'result': result})


# This condition checks whether we are running this file directly.
# If we run "python app.py", this condition becomes True.
# If another Python file imports this file, it does not run the server.
if __name__ == '__main__':

    # Start the Flask development server.
    # debug=True automatically reloads the server when we change our code
    # and displays helpful error messages during development.
    app.run(debug=True)
