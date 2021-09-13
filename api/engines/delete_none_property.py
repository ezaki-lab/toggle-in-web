# 辞書の中にNoneなプロパティがあれば削除
def delete_none_property(dic: dict) -> dict:
    for property in list(dic.keys()):
        if dic[property] == None:
            del dic[property]

        # 中にも辞書があれば再帰
        elif type(dic[property]) == dict:
            dic[property] = delete_none_property(dic[property])

        # 中が配列ならすべての要素を再帰
        elif type(dic[property]) == list:
            for index, _ in enumerate(dic[property]):
                if type(dic[property][index]) != dict:
                    continue
                dic[property][index] = delete_none_property(
                    dic[property][index]
                )

    return dic
