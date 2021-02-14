"""
This script runs the api server with optionally supplied host and port.
"""
import argparse
import uvicorn

"""
In this section import the modules that define Actions.
These should be imported before importing whendo.api.main
"""
import alfalfa.action_imports

"""
import the main script that creates the FastAPI instance (main.app).
"""
from whendo.api import main

"""
parse command line arguments
"""
parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='127.0.0.1', dest='host')
parser.add_argument('--port', type=int, default=8000, dest='port')
args = parser.parse_args()

"""
uvicorn is the ASGI server that runs the api specified with FastAPI.
"""
uvicorn.run(main.app, host=args.host, port=args.port)
