from engines.db_info import DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
import sqlalchemy as sa
from sqlalchemy import text
from typing import Any


def update_table(table: str, target_column: str, target_value: Any, update_column: str, update_value: Any):
    # データベースに接続するURL
    url = "{}://{}:{}@{}:{}/{}?charset=utf8".format(
        DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )
    engine = sa.create_engine(url, echo=False)

    # 指定したカラムの値を変更
    with engine.connect() as conn:
        query = "UPDATE {0} SET {1} = :{1} WHERE {2} = :{2}".format(
            table, update_column, target_column)
        stmt = text(query)
        stmt = stmt.bindparams(**{
            update_column: update_value,
            target_column: target_value
        })
        conn.execute(stmt)
