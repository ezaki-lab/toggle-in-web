from engines.auth_api_token import auth_api_token
from engines.check_json_require import check_json_require
from models.Property import Property
from flask import Request
from typing import Any, List, Tuple, Union


# GETされたものが適切であるかチェック
def check_get_request(res: Request, req: Union[List[Property], None] = None) -> Union[Tuple[int, Union[Any, None]], int]:
    # API認証が成功するか
    if auth_api_token(res.headers.get("Authorization")):
        if req != None:
            json = res.args.to_dict()
            # 必須なものが含まれているか
            result, json = check_json_require(json, req)
            if result:
                return 200, json

            return 400, None

        return 200

    return 401
