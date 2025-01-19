from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class InputData(BaseModel):
    int_value: int = Field(..., ge=0, description="An integer that must not be negative.")
    string_value: str = Field(..., max_length=10, description="A string with a maximum length of 10 characters.")

@app.post("/submit")
async def submit(data: InputData):
    try:
        # Input data is automatically validated by Pydantic
        return {
            "message": "Data received successfully.",
            "int_value": data.int_value,
            "string_value": data.string_value
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
