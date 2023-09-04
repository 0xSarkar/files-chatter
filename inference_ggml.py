from ctransformers import AutoModelForCausalLM

llm_model = "../llm-models/llama2-7b-chat-ggml-q4km/llama-2-7b-chat.ggmlv3.q4_K_M.bin"
llm = None

def load_llm_model(thread_event=None):
  print("Loading Llama 2 Q4KM GGML model...")
  global llm_model, llm
  llm = AutoModelForCausalLM.from_pretrained(llm_model, model_type="llama")
  print("Model loaded.")

def infer(msg: str):
  global llm

  msg_prompt = f"[INST]<<SYS>>You're an helpful A.I. chatbot.<</SYS>>{msg}[/INST]"

  print("Running inference...")
  llm_resp = ""
  print(f'Prompt: {msg_prompt}')
  print("Response:")
  for text in llm(msg_prompt, stream=True):
    print(text, end="", flush=True)
    llm_resp += text
  print("\n")
  print("Inference complete.")
  return llm_resp
