from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np
import uvicorn
from PIL import Image
import io

app = FastAPI()
model = YOLO("best.pt") 

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    results = model.predict(np.array(image), conf=0.25)[0]

    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = map(float, box.xyxy[0])
        detections.append({
            "label": label,
            "confidence": round(confidence, 2),
            "bbox": [x1, y1, x2 - x1, y2 - y1]
        })

    return JSONResponse(content={"detections": detections})
