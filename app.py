from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

@app.route('/')
def default_route():
    """Default route to return a simple message"""

    return jsonify('hello world')

@app.route('/message', methods=['GET'])
@app.route('/message/<new_message>', methods=['POST'])
def message_handler(new_message=None):
    """Handle the getting and setting of the message"""

    redis_client = redis.StrictRedis(host='redis')

    if request.method == 'GET':
        output = redis_client.get('message')
        # import pdb; pdb.set_trace()
        if output:
            return jsonify(dict(message=output.decode('utf-8')))

        return jsonify(dict(message='no output found for new_message'))

    redis_client.set('message', new_message)
    return jsonify(dict(message='set new_message'))

if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
