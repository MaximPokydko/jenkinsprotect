from fastapi import FastAPI
import time
import os

app = FastAPI()

START_TIME = time.time()

@app.get("/")
def root():
    return {
        "service": "mini-ci-app",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "uptime_sec": int(time.time() - START_TIME)
    }

@app.get("/env")
def env():
    return {
        "python_version": os.sys.version,
        "message": "CI/CD test app running"
    }
