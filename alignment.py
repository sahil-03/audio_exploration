from aeneas.executetask import ExecuteTask
from aeneas.task import Task

def align_transcript_with_audio() -> None:
    config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = "audio.mp3"
    task.text_file_path_absolute = ""
    task.sync_map_file_path_absolute = "aligned.json"

    ExecuteTask(task).execute()
    task.outpput_sync_map_file()