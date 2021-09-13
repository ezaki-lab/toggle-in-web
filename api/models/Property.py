from typing import Any, List, Tuple, Union
from datetime import datetime
import re


class Property:
    def __init__(self, element: str, element_type: type, max_len: int, is_require: bool, element_property: Union[List, None] = None):
        self.element = element
        self.element_type = element_type
        self.max_len = max_len
        self.is_require = is_require
        self.element_property = element_property

    def match(self, target: Any) -> Tuple[bool, Any]:
        # 要素内プロパティが指定されていないなら
        if self.element_property == None:
            # 時刻型が指定されているなら、文字列型が時刻型に変換できるかをチェック
            if self.element_type == datetime:
                # 時刻の正規表現で一つもマッチしなければ脱落
                if len(re.findall(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$", target)) == 0:
                    return False, None
            # 実数型が指定されていて、値の型が整数なら特別に通す
            elif self.element_type == float and type(target) == int:
                return True, float(target)
            # 型が異なれば脱落
            elif type(target) != self.element_type:
                return False, None

            # 上限文字数があれば、上限以内であるかをチェック
            # 上限を超えていれば脱落
            else:
                if self.max_len != -1:
                    if self.max_len < len(str(target)):
                        return False, None

        else:
            from api.engines.check_json_require import check_json_require
            # リストなら0番目の要素で判別する
            if self.element_type != list:
                return check_json_require(target, self.element_property)
            else:
                # リストならすべての要素をチェック
                # その中でFalseがあれば脱落
                for index, _ in enumerate(target):
                    result, target[index] = check_json_require(
                        target[index], self.element_property)
                    if not result:
                        return False, None

        return True, target
