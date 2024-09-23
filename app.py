import io
import json
from fastapi import FastAPI, File, UploadFile
import pandas as pd
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import FileResponse, Response
from copa_tpclo_ml.utils.processing_text_data import ProcessingTextData
from copa_tpclo_ml.utils.cleanup_csv_data  import CleanupCSVData
import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np


app = FastAPI()
processingTextData=ProcessingTextData()
cleanupCSVData=CleanupCSVData()

@app.get("/", tags=["Health check"])
async def index():
    return {"message": "CPOA TPCLO MachineLearning API Running!"}

@app.get("/CleanupTextData", tags=["Cleanup text file data"])
def Test(filename:str):
    data=processingTextData.cleanup_textdata(filename)
    if data is  None:
        return {"message": "No data found in the file"}  
    else:
        return {"data": data}

@app.get("/MostFrequentWords", tags=["Generate most frequent words plot"])
def Test(filename:str):
    data=processingTextData.most_frequent_words(filename)
    return FileResponse(data)   

@app.get("/generate_ngrams", tags=["Generate ngrams plot"])
def Test(filename:str,ngrams:int):
    data=processingTextData.generate_ngrams(filename,ngrams)
    return FileResponse(data)   

@app.get("/analyze_sentiment", tags=["Get sentiment analyze"])
def Test(filename:str):
    data=processingTextData.analyze_sentiment(filename)
    return FileResponse(data)   

@app.get("/CleanupCSVData", tags=["Cleanup csv file data"])
def Test(filename:str,column:str):
    df=cleanupCSVData.CleanupCSVData(filename,column)
    if len(df)>0:
        json_data = df.to_json(orient="records")
        return {"data": json_data}  
    else:
        return {"message": "No data found in the file"}

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


