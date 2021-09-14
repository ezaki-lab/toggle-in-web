###################################
#  スイッチAPI
###################################

from engines.auth_api_token import auth_api_token
from engines.check_get_request_without_token import check_get_request_without_token
from engines.insert_to_table import insert_to_table
from engines.update_table import update_table
from engines.check_post_request import check_post_request
from engines.check_put_request_without_token import check_put_request_without_token
from engines.select_from_table import select_from_table
from engines.generate_token import generate_token
import logging
from pandas import DataFrame
from flask import abort, Blueprint, request, jsonify

app = Blueprint("switch", __name__)


@app.route("/switch/<switch_id>", methods=["GET", "POST", "PUT"])
def switch(switch_id: str):
    # アクセス解析のためのロギング
    logging.info("|{}| {} |{}|".format(
        request.method, request.full_path, request.remote_addr
    ))

    try:
        if request.method == "GET":
            status = check_get_request_without_token(request)

            if status == 200:
                # データベースから取ってきてDataFrameにし、リスト辞書に変換
                switches = select_from_table("toggle_in_web_switches")
                switch = switches[switches["id"] == switch_id]

                if switch.shape[0] == 0:
                    return jsonify({
                        "result": "Not Found",
                        "switch": None,
                        "status": None
                    }), 404

                # トークン認証に失敗したら
                if not auth_api_token(request.headers.get("Authorization"), switch.iloc[0]["token"]):
                    abort(401)

                # statusの型をboolに変換
                switch["status"] = switch["status"].astype(bool)

                return jsonify({
                    "result": "OK",
                    "switch": switch_id,
                    "status": bool(switch.iloc[0]["status"])
                }), 200

            elif status == 401:
                abort(401)

        if request.method == "POST":
            status = check_post_request(request)

            if status == 200:
                # データベースから取ってきてDataFrameにし、リスト辞書に変換
                switches = select_from_table("toggle_in_web_switches")
                switch = switches[switches["id"] == switch_id]

                if switch.shape[0] >= 1:
                    return jsonify({
                        "result": "Already Exist",
                        "switch": None
                    }), 409

                token = generate_token()

                insert_to_table(
                    "toggle_in_web_switches",
                    DataFrame.from_dict({
                        "id": [switch_id],
                        "token": [token],
                        "status": [False]
                    })
                )

                return jsonify({
                    "result": "OK",
                    "switch": switch_id,
                    "token": token
                })

            elif status == 400:
                abort(400)
            elif status == 401:
                abort(401)

        if request.method == "PUT":
            status = check_put_request_without_token(request)

            if status == 200:
                # データベースから取ってきてDataFrameにし、リスト辞書に変換
                switches = select_from_table("toggle_in_web_switches")
                switch = switches[switches["id"] == switch_id]

                if switch.shape[0] == 0:
                    return jsonify({
                        "result": "Not Found",
                        "switch": None,
                        "status": None
                    }), 404

                # statusの型をboolに変換
                switch["status"] = switch["status"].astype(bool)

                alter_status = None
                if request.args.get("status") != None:
                    perm = request.args.get("status")
                    if perm == "on":
                        alter_status = True
                    elif perm == "off":
                        alter_status = False
                    else:
                        abort(400)
                else:
                    alter_status = not switch.iloc[0]["status"]

                # トグルスイッチの状態を切り替える
                update_table(
                    "toggle_in_web_switches",
                    "id",
                    switch_id,
                    "status",
                    alter_status
                )

                return jsonify({
                    "result": "OK",
                    "switch": switch_id,
                    "status": alter_status
                }), 200

            elif status == 401:
                abort(401)

        else:
            abort(405)

    # 万が一エラーが起こったらログをとる
    except Exception as e:
        logging.debug(e)
        abort(e.code)
