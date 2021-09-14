from engines.auth_api_token import auth_api_token
from engines.check_json_require import check_json_require
from models.Property import Property
from flask import Request
from typing import Any, List, Tuple, Union


# POSTされたものが適切であるかチェック
def check_post_request(res: Request, req: List[Property] = None) -> Union[Tuple[int, Union[Any, None]], int]:
    # 形式はJSONであるか
    if res.headers.get("Content-Type") == "application/json":
        # API認証が成功するか
        if auth_api_token(res.headers.get("Authorization")):
            json = res.get_json()
            # 必須なものが含まれているか
            result, json = check_json_require(json, req)
            if result:
                return 200, json

            return 400, None

        return 401, None

    elif req == None:
        # API認証が成功するか
        if auth_api_token(res.headers.get("Authorization")):
            return 200

        return 401

    return 400, None
