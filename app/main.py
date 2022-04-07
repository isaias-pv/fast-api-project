from router.routes import *

@app.get('/')
async def index():
    return {"status": 400}