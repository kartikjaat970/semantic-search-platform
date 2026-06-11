from sqlalchemy import (
create_engine,
Column,
Integer,
Text
)

from sqlalchemy.orm import (

sessionmaker,

declarative_base

)

DATABASE_URL=(
"postgresql://postgres:"
"admin@localhost:"
"5432/semanticdb"
)

engine=create_engine(
DATABASE_URL
)

SessionLocal=sessionmaker(

autocommit=False,

autoflush=False,

bind=engine

)

Base = declarative_base()


class Document(Base):
	__tablename__ = "documents"

	id = Column(
		Integer,
		primary_key=True
	)

	text = Column(
		Text
	)

	embedding = Column(
		Text
	)


Base.metadata.create_all(
bind=engine
)