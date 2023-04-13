import sqlalchemy
from sqlalchemy.util.preloaded import orm

from .db_session import SqlAlchemyBase


class Movie(SqlAlchemyBase):
    __tablename__ = 'movie'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_city = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("cities.id"))
    adress = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id_region = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("regions.id"))

    city_M = orm.relationship('City')
    region_Mv = orm.relationship('Region')