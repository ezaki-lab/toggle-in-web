from engines.delete_none_property import delete_none_property
from models.Property import Property
from typing import Any, List, Tuple


def check_json_require(json: Any, expected_req: List[Property]) -> Tuple[bool, Any]:
    # 要素内にNoneがある場合は、その要素をないものとする
    json = delete_none_property(json)

    # 想定される要素リストから辞書をつくる
    status = {}
    for index, element in enumerate(expected_req):
        # 必須なものはFalse、任意なものはTrue
        # 想定される要素リストのインデックスも記録
        status[element.element] = [
            False if element.is_require else True,
            index
        ]

    # JSONの全プロパティをチェックし、必須なものが存在すればTrue
    # 想定リストにないJSONの要素があれば、そこで脱落
    for property in list(json.keys()):
        if property in status:
            status[property][0] = True
            # 型が一致し、上限文字数以内ならTrueで値を更新
            # それ以外ならFalse
            result, altered = expected_req[status[property][1]].match(
                json[property])
            if result:
                json[property] = altered
            else:
                status[property][0] = False
        else:
            return False, json

    # 一つでも想定される要素リスト通りでなければ、そこで脱落
    for info in list(status.values()):
        if not info[0]:
            return False, json

    # おめでとう！君はすべて想定されている！
    return True, json
