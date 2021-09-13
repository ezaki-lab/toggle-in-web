from engines.check_post_request import check_post_request
from models.Property import Property
from flask import Request
from typing import Any, List, Tuple, Union


# PUTされたものが適切であるかチェック
# 基本的にPOSTの関数と同様
def check_put_request(res: Request, req: List[Property]) -> Tuple[int, Union[Any, None]]:
    return check_post_request(res, req)
