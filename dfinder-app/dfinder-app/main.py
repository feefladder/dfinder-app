from fastapi import FastAPI
import dfinder


# this is horrible, and causes the container to break if too many consecutive
# calls are made, without any error (not even segfault)
dfinder.InitializeSquare()

app = FastAPI(
    title="dfinder",
    description="API for divisionfinder app",
    docs_url="/api/docs"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/calc-divisions/{divisions}")
def calc_divisions(divisions: int):
    if (divisions>0):
        return {"response" : dfinder.CalcDivisionsHTML(divisions)}