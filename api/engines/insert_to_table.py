from engines.db_info import DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
import sqlalchemy as sa
from pandas import DataFrame


def insert_to_table(table: str, df: DataFrame, if_exists: str = "append"):
    # データベースに接続するURL
    url = "{}://{}:{}@{}:{}/{}?charset=utf8".format(
        DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )
    engine = sa.create_engine(url, echo=False)

    # DataFrameをデータベースに挿入
    df.to_sql(
        table,
        con=engine,
        if_exists=if_exists,
        index=False
    )
