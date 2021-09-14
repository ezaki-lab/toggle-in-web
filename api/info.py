###################################
#  情報API
###################################

from engines.check_get_request import check_get_request
from engines.select_from_table import select_from_table
import logging
from flask import abort, Blueprint, request, jsonify

app = Blueprint("info", __name__)


@app.route("/info/<switch_id>", methods=["GET"])
def info(switch_id: str):
    # アクセス解析のためのロギング
    logging.info("|{}| {} |{}|".format(
        request.method, request.full_path, request.remote_addr
    ))

    try:
        if request.method == "GET":
            status = check_get_request(request)

            if status == 200:
                # データベースから取ってきてDataFrameにし、リスト辞書に変換
                switches = select_from_table("toggle_in_web_switches")
                switch = switches[switches["id"] == switch_id]

                if switch.shape[0] == 0:
                    return jsonify({
                        "result": "Not Found",
                        "switch": None,
                        "token": None,
                        "status": None,
                    }), 404

                # statusの型をboolに変換
                switch["status"] = switch["status"].astype(bool)

                return jsonify({
                    "result": "OK",
                    "switch": switch.iloc[0]["id"],
                    "token": switch.iloc[0]["token"],
                    "status": bool(switch.iloc[0]["status"]),
                }), 200

            elif status == 401:
                abort(401)

        else:
            abort(405)

    # 万が一エラーが起こったらログをとる
    except Exception as e:
        logging.debug(e)
        abort(e.code)
