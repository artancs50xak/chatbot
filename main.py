from model import load_model
from chat import responed
from ui import build_ui

if __name__ == "__main__":
    tokenizer, model, device = load_model()
    respond_fn= responed(tokenizer, model, device)
    demo = build_ui(respond_fn)
    demo.launch()