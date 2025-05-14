from fastapi import APIRouter

entry_root = APIRouter()

#endpoint
@entry_root.get("/")

def api_running():
    res = {
        "status" : "ok",
        "message" : "Api is running"
    }
    return res