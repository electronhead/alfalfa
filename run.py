"""
This script runs the api server with optionally supplied host and port.
"""
import argparse
import uvicorn

"""
In this section import the modules that define Actions.
These should be imported before importing whendo.api.main
"""
import alfalfa.action

"""
import the main script involving the creation of a FastAPI instance.
"""
from whendo.api import main


"""
parse command line arguments
"""
parser = argparse.ArgumentParser()
parser.add_argument('-host', '--host', type=str, default='127.0.0.1', dest='host')
parser.add_argument('-port', '--port', type=int, default=8000, dest='port')
args = parser.parse_args()

uvicorn.run(main.app, host='127.0.0.1', port=8000)