from uuid import uuid4
from pathlib import Path
import gradio as gr

from model import stream_response
from history import (
    save_conversation, delete_conversation,
    get_sidebar_choices, get_messages
)

def build_messages(history: list, uset_text: str) -> list:
    ...

def responed(tokenizer, model, device):
    ...

def handle_retry(responed_fn):
    ...

def handle_like(data: gr.LikeData):
    print(f"[Like] {'👍' if data.liked else '👎'}")

def handle_edit(edi_data: gr.EditData):
        print(f"[Edir] index = {edi_data.index}, value = {edi_data.value}")

def handle_clear():
    new_uuid = str(uuid4())
    print(f"[Clear] new session: {new_uuid}")
    return new_uuid, gr.update(choices = get_sidebar_choices(), value = None)

def handle_undo(history, undo_data: gr.UndoData):
    print(f"[Undo] index={undo_data.index}")
    return history[:undo_data.index], undo_data.value

def load_conversation():
    ...

def delete_sellected(selected_sid: str):
    ...

def refresh_sidebar():
    return gr.update(choices = get_sidebar_choices())