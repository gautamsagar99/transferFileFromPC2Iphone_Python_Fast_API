import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.get("/files")
async def get_files():
    directory = "downloadablefiles"
    files = os.listdir(directory)
    return {"files": files}

@app.get("/file/{file_name}")
async def download_file(file_name: str):
    return FileResponse(f"downloadablefiles/{file_name}", filename=file_name)



# for iphones
# @app.get("/file/{file_name}")
# async def download_file(file_name: str):
#     file_path = f"downloadablefiles/{file_name}"
#     file_mime_type, _ = mimetypes.guess_type(file_path)
#     headers = {"Content-Disposition": f'attachment; filename="{file_name}"'}
#     return FileResponse(file_path, media_type=file_mime_type, headers=headers)