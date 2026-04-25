from fastapi import FastAPI

app = FastAPI(title="DataGate API")


@app.get("/")
def root():
    return {"message": "DataGate is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}