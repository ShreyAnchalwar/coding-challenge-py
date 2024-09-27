from flask import Flask

app = Flask(__name__)

@app.route('/the-clumsy-programmer', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input_value = data.get("input")
    result = input_value * input_value
    logging.info("My result :{}".format(result))
    return json.dumps(result)


if __name__ == '__main__':
    app.run()
