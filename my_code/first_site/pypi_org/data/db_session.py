import sqlalchemy as sa 
import sqlalchemy.orm as orm
from data.modelbase import SqlAlchemyBase

factory = None

def global_init(db_file: str):
  global factory

  if factory:
    return
  
  if not db_file or not db_file.strip():
    raise Exception("You must specify a db file.")


  conn_str = 'sqlite:///' + db_file.strip()

  print("Connecting to DB with {}".format(conn_str))

  engine = sa.create_engine(conn_str, echo=False)

  factory = orm.sessionmaker(bind=engine)

  #This import is very important because it shows it to the SqlAlchemy base.
  from data import __all_models
  SqlAlchemyBase.metadata.create_all(engine)