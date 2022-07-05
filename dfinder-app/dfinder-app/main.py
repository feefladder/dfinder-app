from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import dfinder


# this is horrible, and causes the container to break if too many consecutive
# calls are made, without any error (not even segfault)
dfinder.InitializeSquare()

app = FastAPI(
    title="dfinder",
    description="API for divisionfinder app",
)

class Instruction(BaseModel):
    description: str
    diagrams: List[str]
    verbal: List[str]

class Instructions(BaseModel):
    Instructions: List[Instruction]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/find-divs-svg/{divisions}")
def calc_divisions(divisions: int):
    if (divisions>0):
        r_divs =  dfinder.FindDivisionsSVG(divisions)
        return Instructions(Instructions=[Instruction(description=div.description, diagrams=div.diagrams, verbal=div.verbal) for div in r_divs ])
    else:
        raise HTTPException(status_code=403, detail="Please enter a number between 0 and 101 (otherwise you'll overload the server.")

@app.get("/fold-cycle-svg/")
def fold_cycle(total: int, start: int):
    if (total  > 0 and total < 101):
        start = start % total # so that 0 < start <  total
        cycle = dfinder.FoldCyclesSVG(total, start)
        return Instruction(description=cycle.description,diagrams=cycle.diagrams,verbal=cycle.verbal)
    else:
        raise HTTPException(status_code=403, detail="Please enter a number between 0 and 101 (otherwise you'll overload the server.")
