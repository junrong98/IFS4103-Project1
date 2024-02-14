from flask import Flask

app = Flask(__name__)

@app.route('/get_flag', methods=['GET'])
def get_flag():
    # Add logic to retrieve and return the flag
    return "FLAG{55RF_6NS_R3B1ND1NG}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
