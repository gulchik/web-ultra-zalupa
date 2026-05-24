from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles  # если понадобятся картинки или CSS
import os

app = FastAPI(title="Clan Static Site")

# Если у вас есть папка со статикой (картинки, шрифты) - раскомментируйте
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Главная страница: отдаём index.html из папки templates
@app.get("/", response_class=HTMLResponse)
async def get_index():
    # Указываем полный путь до файла (работает из любой директории запуска)
    file_path = os.path.join("templates", "index.html")
    if not os.path.exists(file_path):
        return HTMLResponse(content="<h1>Файл templates/index.html не найден</h1>", status_code=404)
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# Альтернативный вариант (если не хотите читать файл вручную):
# from fastapi.responses import FileResponse
# @app.get("/")
# async def get_index():
#     return FileResponse("templates/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)