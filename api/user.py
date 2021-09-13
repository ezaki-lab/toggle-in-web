###################################
#  ユーザー情報API
###################################

from mmap import ALLOCATIONGRANULARITY
from engines.check_get_request import check_get_request
from engines.select_from_table import select_from_table
import logging
from flask import abort, Blueprint, request, jsonify

app = Blueprint("user", __name__)


@app.route("/user/<username>", methods=["GET"])
def user(username: str):
    # アクセス解析のためのロギング
    logging.info("|{}| {} |{}|".format(
        request.method, request.full_path, request.remote_addr
    ))

    try:
        if request.method == "GET":
            status = check_get_request(request)

            if status == 200:
                # データベースから取ってきてDataFrameにし、リスト辞書に変換
                users = select_from_table("toggle_in_web_users")
                user = users[users["id"] == username]

                if user.shape[0] == 0:
                    return jsonify({
                        "result": "Not Found",
                        "user": None,
                        "available": None
                    }), 404

                # 利用可能なトグルスイッチ一覧
                available = user.iloc[0]["available"]
                if available == None:
                    available = []
                else:
                    available = available.split(',')

                return jsonify({
                    "result": "OK",
                    "user": user.iloc[0]["id"],
                    "available": available
                }), 200

            elif status == 401:
                abort(401)

        else:
            abort(405)

    # 万が一エラーが起こったらログをとる
    except Exception as e:
        logging.debug(e)
        abort(e.code)
