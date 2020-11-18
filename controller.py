from fastapi import FastAPI, Query
import extractor as ex
from repository import select_by_ids
from typing import List

app = FastAPI()


@app.post("/audio/extract")
def audio_extract(video_id: str, local_video_path: str):
    audio_id, local_audio_path = ex.extract(video_id, local_video_path)
    data = {'audio_id': audio_id, 'local_audio_path': local_audio_path}
    return {"success": True, "code": 0, "msg": "ok", "data": data}


@app.get("/audio/batch/query")
def batch_query(audio_ids: List[str] = Query(None)):
    data = select_by_ids(audio_ids)
    return {"success": True, "code": 0, "msg": "ok", "data": data}