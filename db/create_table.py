from database import Base


def create_table(engine):
    Base.metadata.create_all(engine)
