import sqlalchemy
from sqlalchemy.util.preloaded import orm
from .db_session import SqlAlchemyBase


class Director(SqlAlchemyBase):
    __tablename__ = 'directors'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    s_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    theater = orm.relationship("Theater", back_populates='director')