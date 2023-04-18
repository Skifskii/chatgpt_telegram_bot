from utils.db_api.db_gino import BaseModel
from sqlalchemy import Column, BigInteger, String, sql, Integer, VARCHAR


class User(BaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True, nullable=False)
    username = Column(String(64), default='')
    firstname = Column(String(64), default='')
    chat_story = Column(String, default='{"messages":[]}')
    status = Column(VARCHAR, default='user')
    limit = Column(Integer, default=3)
    max_limit = Column(Integer, default=3)
    # date_subscription_finish = Column(String, default='')
    total_images_generated = Column(Integer, default=0)
    total_messages_sent = Column(Integer, default=0)

    query: sql.select
