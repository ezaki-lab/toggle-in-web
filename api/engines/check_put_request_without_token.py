from engines.check_post_request_without_token import check_post_request_without_token
from engines.check_post_request_without_token import check_post_request_without_token
from models.Property import Property
from flask import Request
from typing import Any, List, Tuple, Union


# トークンなしでPUTされたものが適切であるかチェック
# 基本的にPOSTの関数と同様
def check_put_request_without_token(res: Request, req: List[Property] = None) -> Tuple[int, Union[Any, None]]:
    return check_post_request_without_token(res, req)
