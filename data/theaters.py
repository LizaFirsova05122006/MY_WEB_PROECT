import sqlalchemy
from sqlalchemy.util.preloaded import orm

from .db_session import SqlAlchemyBase


class Theater(SqlAlchemyBase):
    __tablename__ = 'theaters'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_city = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("cities.id"))
    adress = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    y_foundation = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    director_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("directors.id"))
    id_region = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("regions.id"))

    region_Th = orm.relationship('Region')
    director = orm.relationship('Director')
    city = orm.relationship('City')