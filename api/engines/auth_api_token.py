from engines.tokens import GENERAL_TOKEN as TOKEN


# サービスを提供する上でのトークンと一致すれば
def auth_api_token(auth: str, option_token: str = None) -> bool:
    # 認証文字列がNoneなら脱落
    if auth == None:
        return False

    # 認証文字列が7文字以下なら脱落
    if len(auth) < 7:
        return False

    # Bearerトークンでなければ脱落
    if auth[:6] != "Bearer":
        return False

    # トークン部分
    token = auth[7:]

    if token == TOKEN:
        # 記録されているトークンと一致するなら
        return True
    elif token == option_token:
        # 正しいトークンが指定されているなら
        return True

    return False
