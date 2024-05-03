from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from src.textSummarizer.pipeline.stage_6_prediction import PredictionPipeline
import uvicorn

app = FastAPI()

# Configure Jinja2Templates to load HTML templates from the "templates" directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict_route(request: Request):
    try:
        data = await request.json()
        text = data.get("text")
        if text is None:
            return JSONResponse(status_code=400, content={"error": "Missing 'text' in request body"})
        
        prediction_obj = PredictionPipeline()
        predicted_text = prediction_obj.predict(text)
        return {"text": predicted_text}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Internal Server Error"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)