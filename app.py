from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/research")
def research(topic: str):
    try:
        result = subprocess.run(
            ["last30days", topic],
            capture_output=True,
            text=True,
            timeout=120
        )
        return {"output": result.stdout}
    except Exception as e:
        return {"error": str(e)}