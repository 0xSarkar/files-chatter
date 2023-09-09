from ctransformers import AutoModelForCausalLM
import tkinter as tk
import threading

llm_model = "../llm-models/llama2-7b-chat-ggml-q4km/llama-2-7b-chat.ggmlv3.q4_K_M.bin"
llm = None

def load_llm_model(thread_event=None):
  print("Loading Llama 2 Q4KM GGML model...")
  global llm_model, llm
  llm = AutoModelForCausalLM.from_pretrained(llm_model, model_type="llama")
  print("Model loaded.")

def infer(user_msg: str, txt_conv):
  global llm

  sys_prompt = "You are an AI bot. Don't greet or apologize to user. Give straight-forward response to what the user says."
  final_prompt = f"""<s>[INST] <<SYS>>\n{sys_prompt}\n<</SYS>>\n\n{user_msg} [/INST]"""

  print("Running inference...")
  llm_resp = ""
  print(f'Prompt: {final_prompt}')
  print("Response:")
  
  def run_inference():
    nonlocal llm_resp
    nonlocal txt_conv

    txt_conv.config(state=tk.NORMAL)
    txt_conv.tag_configure("bold", font=("Helvetica", 12, "bold"))
    txt_conv.insert(tk.END, "\nBot:\n", "bold")
    txt_conv.config(state=tk.DISABLED)

    for idx, text in enumerate(llm(final_prompt, stream=True)):
      print(text, end="", flush=True)

      if(idx == 1): # strip the empty space at the beginning of the first token
        text = text.strip()

      if (idx > 0): # skip the first empty space token
        txt_conv.config(state=tk.NORMAL)
        txt_conv.insert(tk.END, text)
        txt_conv.config(state=tk.DISABLED)

        llm_resp += text
      
    print("\n")
    print("Inference complete.")

  # Create a new thread and start it
  inference_thread = threading.Thread(target=run_inference)
  inference_thread.start()

  return llm_resp
