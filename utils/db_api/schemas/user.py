from ..db_gino import BaseModel, TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql


class User(TimedBaseModel):
	__tablename__ = "users"
	user_id = Column(BigInteger, primary_key=True)
	full_name = Column(String(200))
	username = Column(String(50))
	status = Column(String(30))

	query: sql.select