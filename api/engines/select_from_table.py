from engines.db_info import DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
from pandas import DataFrame, read_sql
import sqlalchemy as sa


def select_from_table(table: str) -> DataFrame:
    # データベースに接続するURL
    url = "{}://{}:{}@{}:{}/{}?charset=utf8".format(
        DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )
    engine = sa.create_engine(url, echo=False)

    # journalテーブルから全てのデータを取り出す
    query = "SELECT * FROM " + table
    # 取り出したデータをDataFrameに格納
    return read_sql(query, con=engine)
