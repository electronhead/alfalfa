import uvicorn
from whendo.api import main

import alfalfa.action

uvicorn.run(main.app, host='127.0.0.1', port=8000)