from src.main import app

if __name__ == "__main__":
    import uvicorn
    from src.config import HOST, PORT

    uvicorn.run(app, host=HOST, port=PORT)
