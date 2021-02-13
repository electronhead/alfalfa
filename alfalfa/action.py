"""
A proof of concept regarding imports from whengo library.
"""
from whendo.core.actions.file_action import FileHeartbeat

class AlfalfaAction(FileHeartbeat):
    color:str
    
    def execute(self, tag:str=None, scheduler_info:dict=None):
        try:
            info = scheduler_info if scheduler_info else {}
            info['what?'] = 'Alfalfa rocks!'
            super().execute(tag=tag, scheduler_info=info)
        except Exception as exception:
            return exception