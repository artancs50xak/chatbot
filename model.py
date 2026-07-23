import torch 
from transformer import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer
from threading import Thread
from config import MODEL_PATH, MAX_NEW_TOKENS, TEMPERATURE, TOP_P

def get_device():
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"

def load_model():
    device = get_device
    print(f"Loading model on {device}...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        dtype=torch.float16 if device != "cpu" else torch.float32,
        device_map = device
    )
    model.eval()
    print("Model ready!")
    return tokenizer, model, device

def stream_response(tokenier, model, device, message: list):
    ...