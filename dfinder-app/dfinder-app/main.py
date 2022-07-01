from fastapi import FastAPI, HTTPException
import dfinder


# this is horrible, and causes the container to break if too many consecutive
# calls are made, without any error (not even segfault)
dfinder.InitializeSquare()

app = FastAPI(
    title="dfinder",
    description="API for divisionfinder app",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/calc-divisions/{divisions}")
def calc_divisions(divisions: int):
    if (divisions>0 and divisions < 101):
        return {"response" : dfinder.CalcDivisionsHTML(divisions)}
    else:
        raise HTTPException(status_code=403, detail="Please enter a number between 0 and 101 (otherwise you'll overload the server.")