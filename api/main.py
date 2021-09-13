import logging

from flask import Flask
from flask_cors import CORS

import user


# デバッグのためのロギング
logging.basicConfig(
    filename="./logging.txt",
    level=logging.DEBUG,
    format="[%(levelname)s] %(asctime)s : %(filename)s:%(lineno)d >> %(message)s"
)

# サーバーアプリを作成
app = Flask(__name__)
# CORSを全面許可
CORS(app)

# すべてのアプリを統合
app.register_blueprint(user.app)


###################################
#  400 Bad Request
###################################
@app.errorhandler(400)
def bad_request(e):
    return "400 Bad Request", 400


###################################
#  401 Unauthorized
###################################
@app.errorhandler(401)
def unauthorized(e):
    return "401 Unauthorized", 401


###################################
#  404 Not Found
###################################
@app.errorhandler(404)
def not_found(e):
    return "404 Not Found", 404


###################################
#  405 Method Not Allowed
###################################
@app.errorhandler(405)
def not_found(e):
    return "405 Method Not Allowed", 405


###################################
#  409 Conflict
###################################
@app.errorhandler(409)
def conflict(e):
    return "409 Conflict", 409


###################################
#  500 Internal Server Error
###################################
@app.errorhandler(500)
def server_error(e):
    return "500 Internal Server Error", 500


if __name__ == "__main__":
    app.run(debug=False)
