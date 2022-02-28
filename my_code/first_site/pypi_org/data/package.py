from platform import release
import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime
from data.modelbase import SqlAlchemyBase
from data.releases import Release
import typing

class Package(SqlAlchemyBase):
  __tablename__ = 'packages'

  id = sa.Column(sa.String, primary_key=True,)
  created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
  summary = sa.Column(sa.String, nullable=False)
  description = sa.Column(sa.String, nullable=True)

  home_page = sa.Column(sa.String)
  docs_url = sa.Column(sa.String)
  package_url = sa.Column(sa.String)

  author_name = sa.Column(sa.String)
  author_email = sa.Column(sa.String, index=True)

  license = sa.Column(sa.String, index=True) 

  # releases relationship
  releases: List[Release] = orm.relation("Release",order_by=[
    Release.major_ver.desc(),
    Release.minor_ver.desc(),
    Release.build_ver.desc()]
    ,back_populates='package')

  def __repr__(self) -> str:
    return '<Package {}>'.format(self.id)