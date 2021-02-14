"""
A proof of concept regarding imports from whengo library.
"""
from typing import Optional
from whendo.core.action import ActionPayload, Action
from whendo.core.actions.file_action import FileHeartbeat
from whendo.core.util import PP
import logging

logger = logging.getLogger(__name__)

class AlfalfaAction(FileHeartbeat):
    color:str
    
    def execute(self, tag:str=None, scheduler_info:dict=None):
        info = scheduler_info if scheduler_info else {}
        info['what?'] = 'Alfalfa rocks!'
        super().execute(tag=tag, scheduler_info=info)
