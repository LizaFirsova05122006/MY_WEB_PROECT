import sqlalchemy
from sqlalchemy.util.preloaded import orm

from .db_session import SqlAlchemyBase


class City(SqlAlchemyBase):
    __tablename__ = 'cities'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_region = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("regions.id"))
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    region = orm.relationship('Region')
    city = orm.relationship("Theater", back_populates='city')
    city_M = orm.relationship("Movie", back_populates='city_M')