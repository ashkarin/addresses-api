import sqlalchemy as sa
from myapp.app import database
from myapp.model.address import Address


def get_dist_builings_by_zip(zip_code=None):
    dist = None
    if zip_code is not None:
        dist = database.session.query(Address.plz, sa.func.count(Address.object_id))\
                      .filter(Address.plz == zip_code)\
                      .group_by(Address.plz).all()
    else:
        dist = database.session.query(Address.plz, sa.func.count(Address.object_id))\
                         .group_by(Address.plz).all()

    return sorted(dist, key=lambda x: int(x[0]))


def get_dist_builings_by_years(zip_code=None):
    dist = None
    if zip_code is not None:
        dist = database.session.query(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date)),
                             sa.func.count(Address.object_id))\
                      .filter(Address.plz == zip_code)\
                      .group_by(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date))).all()
    else:
        dist = database.session.query(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date)),
                             sa.func.count(Address.object_id))\
                      .group_by(sa.func.extract('year', sa.cast(Address.str_datum, sa.Date))).all()

    return sorted(dist, key=lambda x: int(x[0]))
