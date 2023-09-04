from ctransformers import AutoModelForCausalLM

llm_model = "../llm-models/llama2-7b-chat-ggml-q4km/llama-2-7b-chat.ggmlv3.q4_K_M.bin"
llm = None

def load_llm_model(thread_event=None):
  print("Loading Llama 2 Q4KM GGML model...")
  global llm_model, llm
  llm = AutoModelForCausalLM.from_pretrained(llm_model, model_type="llama")
  print("Model loaded.")

def infer(user_msg: str):
  global llm

  sys_prompt = "You are an AI bot."
  final_prompt = f"""<s>[INST] <<SYS>>\n{sys_prompt}\n<</SYS>>\n\n{user_msg} [/INST]"""

  print("Running inference...")
  llm_resp = ""
  print(f'Prompt: {final_prompt}')
  print("Response:")
  for text in llm(final_prompt, stream=True):
    print(text, end="", flush=True)
    llm_resp += text
  print("\n")
  print("Inference complete.")
  return llm_resp
