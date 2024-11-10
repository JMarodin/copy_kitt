from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet
#uvicorn copykitt_api:app --reload
MAX_INPUT_LENGTH = 32

app = FastAPI()

@app.get("/generat_snippet")
async def generate_snippet(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet}

def validate_input_length(prompt: str):
    if len(prompt) > MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input too long. Must be equal to or under {MAX_INPUT_LENGTH} characters.")
