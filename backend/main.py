from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Shopping Backend - Version 7"}


@app.get("/health")
def health():
    raise HTTPException(
        status_code=500,
        detail="V7 intentional health check failure"
    )
