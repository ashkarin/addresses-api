import sqlalchemy as sa
from myapp.app import database
from myapp.model.address import Address


def get_dist_builings_by_zip(zip_code=None):
    if zip_code is not None:
        return database.session.query(Address.plz, sa.func.count(Address.object_id))\
                      .filter(Address.plz == zip_code)\
                      .group_by(Address.plz).all()
    else:
        return database.session.query(Address.plz, sa.func.count(Address.object_id))\
                         .group_by(Address.plz).all()


def get_dist_builings_by_years(zip_code=None):
    if zip_code is not None:
        return database.session.query(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date)), 
                             sa.func.count(Address.object_id))\
                      .filter(Address.plz == zip_code)\
                      .group_by(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date))).all()
    else:
        return database.session.query(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date)), 
                             sa.func.count(Address.object_id))\
                      .group_by(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date))).all() 
