import ctranslate2
import transformers

llm_model = "../llm-models/fastchat-t5-3b-ct2"
translator = None
tokenizer = None

def load_llm_model(thread_event=None):

    print("Loading Fastchat CT2 model...")

    global llm_model, translator, tokenizer
    translator = ctranslate2.Translator(
      llm_model, 
      device="cpu", 
      compute_type="int8"
    )
    tokenizer = transformers.AutoTokenizer.from_pretrained(llm_model)

    print("Model loaded.")

def infer(msg: str):

  global llm_model, translator, tokenizer
  
  input_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(msg))

  print("Generating tokens of input text...")

  step_results = translator.generate_tokens(
    input_tokens,
    sampling_temperature=0.8,
    sampling_topk=20,
    max_decoding_length=512,
  )

  print("Running inference...")

  llm_resp = ""

  for step_result in step_results:
    #print(step_result)
    is_new_word = step_result.token.startswith("▁")
    word = tokenizer.decode(tokenizer.convert_tokens_to_ids(step_result.token))
    if is_new_word:
      print(f' {word}', end="", flush=True)
      llm_resp += f' {word}'
    elif (word == "</s>"):
      print("\n", end="", flush=True)
      llm_resp += "\n"
    else:
      print(word, end="", flush=True)
      llm_resp += word
  
  return llm_resp
