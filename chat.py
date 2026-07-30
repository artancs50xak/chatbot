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
    ...

def handle_edit(edi_data: gr.EditData):
    ...

def handel_clear():
    ...

def load_conversation():
    ...

def delete_sellected(selected_sid: str):
    ...

def refresh_sidebar():
    ...