from fastapi import FastAPI, HTTPException
import subprocess
import sys
from pathlib import Path

app = FastAPI(title="last30days API")

@app.get("/")
def root():
    return {"status": "ok", "message": "last30days research API"}

@app.get("/research")
def research(topic: str, emit: str = "compact"):
    """Research a topic using last30days.
    
    Args:
        topic: The topic to research
        emit: Output format (compact, json, md, context, path)
    """
    if not topic or not topic.strip():
        raise HTTPException(status_code=400, detail="topic parameter is required")
    
    try:
        script_path = Path(__file__).parent / "scripts" / "last30days.py"
        result = subprocess.run(
            [sys.executable, str(script_path), topic, f"--emit={emit}"],
            capture_output=True,
            text=True,
            timeout=180
        )
        
        if result.returncode != 0:
            return {"error": result.stderr, "returncode": result.returncode}
        
        return {
            "topic": topic,
            "output": result.stdout,
            "success": True
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Research request timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Research failed: {str(e)}")