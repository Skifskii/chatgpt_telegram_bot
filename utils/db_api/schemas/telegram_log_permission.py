from utils.db_api.db_gino import BaseModel
from sqlalchemy import Column, sql, Integer


class TelegramLogPermission(BaseModel):
    __tablename__ = 'tg_log_permissions'
    admin_id = Column(Integer, primary_key=True)
    info = Column(Integer, default=1)
    warning = Column(Integer, default=1)
    error = Column(Integer, default=1)

    query: sql.select
