from engines.check_json_require import check_json_require
from models.Property import Property
from flask import Request
from typing import Any, List, Tuple, Union


# トークンなしでPOSTされたものが適切であるかチェック
def check_post_request_without_token(res: Request, req: List[Property] = None) -> Tuple[int, Union[Any, None]]:
    # 形式はJSONであるか
    if res.headers.get("Content-Type") == "application/json":
        json = res.get_json()
        # 必須なものが含まれているか
        result, json = check_json_require(json, req)
        if result:
            return 200, json

        return 400, None

    elif req == None:
        return 200

    return 400, None
