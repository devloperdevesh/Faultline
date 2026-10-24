from fastapi import FastAPI

app = FastAPI(
    title="Faultline",
    description="Security remediation and verification platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "Faultline",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {"status": "ok"}
