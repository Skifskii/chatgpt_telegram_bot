from utils.db_api.db_gino import BaseModel
from sqlalchemy import Column, sql, Integer


class TelegramLogPermission(BaseModel):
    __tablename__ = 'tg_log_permissions'
    messages = Column(Integer, primary_key=True, default=0)
    new_users = Column(Integer, default=0)
    errors = Column(Integer, default=0)

    query: sql.select
