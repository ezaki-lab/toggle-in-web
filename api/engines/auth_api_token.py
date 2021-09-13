from engines.select_from_table import select_from_table
from engines.update_table import update_table
from datetime import datetime, timedelta, timezone
import hashlib


def auth_api_token(auth: str) -> bool:
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

    # データベースのトークン情報
    tokens = select_from_table("api_tokens")
    hashed_token = hashlib.sha3_256(token.encode("utf-8")).hexdigest()

    # データベースにそのIDが存在するなら
    if tokens[tokens["token"] == hashed_token].shape[0]:
        # 最終使用時間を更新
        update_table(
            "api_tokens",
            "token",
            hashed_token,
            "last",
            datetime.now(timezone(timedelta(hours=+9), 'JST'))
        )

        return True

    return False
