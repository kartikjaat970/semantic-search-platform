from fastapi import (
FastAPI
)

from fastapi.middleware.cors import (
CORSMiddleware
)

from upload import (
router as upload
)

from search import (
router as search
)

app = FastAPI()


app.add_middleware(

CORSMiddleware,

allow_origins=[

"http://localhost:3000"

],

allow_methods=["*"],

allow_headers=["*"],

allow_credentials=True

)


app.include_router(
upload
)

app.include_router(
search
)


@app.get("/")
def root():
    return {
        "status": "running"
    }