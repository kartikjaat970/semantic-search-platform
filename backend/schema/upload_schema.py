from pydantic import BaseModel


class Upload(BaseModel):
	text: str