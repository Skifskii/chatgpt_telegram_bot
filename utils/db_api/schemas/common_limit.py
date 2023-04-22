from utils.db_api.db_gino import BaseModel
from sqlalchemy import Column, sql, Integer


class CommonLimit(BaseModel):
    __tablename__ = 'common_limit'
    value = Column(Integer, primary_key=True, nullable=False, default=2)

    query: sql.select
