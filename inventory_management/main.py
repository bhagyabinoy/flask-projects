from config.settings import engine
from config.settings import metadata
from config.settings import app
import uvicorn

from apps.post.views import post_route
from apps.products.views import product_route
app.include_router(post_route, prefix="/api/post", tags=["post"])
app.include_router(product_route, tags=["product"])


@app.get("/")
def home():
    return {"message": "Welcome to Inventory Management."}


if __name__ == '__main__':
    metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

