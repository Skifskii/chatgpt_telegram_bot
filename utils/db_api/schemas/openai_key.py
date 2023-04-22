from utils.db_api.db_gino import BaseModel
from sqlalchemy import Column, String, sql


class OpenaiKey(BaseModel):
    __tablename__ = 'openai_key'
    key = Column(String, primary_key=True, nullable=False, default='')
    status = Column(String, default='waiting')

    query: sql.select
