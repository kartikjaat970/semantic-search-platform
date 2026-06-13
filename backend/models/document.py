from sqlalchemy import (

Column,

Integer,

Text

)

from pgvector.sqlalchemy import (
Vector
)

from database import (
Base
)


class Document(
Base
):
	__tablename__ = "documents"

	id = Column(Integer, primary_key=True)

	text = Column(Text)

	embedding = Column(Vector(384))