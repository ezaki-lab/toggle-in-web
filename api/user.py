###################################
#  ユーザー情報API
###################################

from models.Property import Property
from engines.check_get_request import check_get_request
from engines.check_put_request import check_put_request
from engines.select_from_table import select_from_table
from engines.insert_to_table import insert_to_table
import logging
from pandas import concat, DataFrame
from flask import abort, Blueprint, request, jsonify

app = Blueprint("user", __name__)


@app.route("/user/<username>", methods=["GET", "PUT"])
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

        if request.method == "PUT":
            status, json = check_put_request(request, [
                Property("available", list, -1, True),
            ])

            if status == 200:
                # データベースから取ってきてDataFrameにし、リスト辞書に変換
                users = select_from_table("toggle_in_web_users")

                users = users[
                    users["id"] != username
                ]

                # 必須なものは挿入する
                user = {
                    "id": [username],
                    "available": [",".join(json["available"])],
                }

                # データベースに挿入
                insert_to_table(
                    "toggle_in_web_users",
                    concat([users, DataFrame.from_dict(user)]),
                    "replace"
                )

                logging.debug('debug')

                return jsonify({
                    "result": "OK",
                    "user": username,
                    "available": json["available"]
                }), 200

            elif status == 400:
                abort(400)
            elif status == 401:
                abort(401)

        else:
            abort(405)

    # 万が一エラーが起こったらログをとる
    except Exception as e:
        logging.debug(e)
        abort(e.code)
