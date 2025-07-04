#!/usr/bin/env python3
"""Simple run script"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app
import uvicorn

if __name__ == "__main__":
    print("Starting Simple Video Creation API...")
    print("API: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)