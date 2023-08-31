import ctranslate2
import transformers

print("Loading Fastchat CT2 model...")

llm_model = "../llm-models/fastchat-t5-3b-ct2"
translator = ctranslate2.Translator(
  llm_model, 
  device="cpu", 
  compute_type="int8"
)
tokenizer = transformers.AutoTokenizer.from_pretrained(llm_model)

input_text = """
Text:
Large Language Models (LLMs) are trained on massive amounts of text data. As a result, they can generate coherent and fluent text. LLMs perform well on various natural languages processing tasks, such as language translation, text summarization, and conversational agents. LLMs perform so well because they are pre-trained on a large corpus of text data and can be fine-tuned for specific tasks. GPT is an example of a Large Language Model. These models are called 'large' because they have billions of parameters that shape their responses. For instance, GPT-3, the largest version of GPT, has 175 billion parameters and was trained on a massive corpus of text data.

Query: What are the key points of this text in 30 words?
"""

#input_text = "The purpose of life is "
input_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(input_text))

print("Generating tokens...")

step_results = translator.generate_tokens(
  input_tokens,
  sampling_temperature=0.8,
  sampling_topk=20,
  max_decoding_length=512,
)

print("Running inference...")

for step_result in step_results:
  #print(step_result)
  is_new_word = step_result.token.startswith("▁")
  word = tokenizer.decode(tokenizer.convert_tokens_to_ids(step_result.token))
  if is_new_word:
    print(f' {word}', end="", flush=True)
  elif (word == "</s>"):
    print("\n\n", end="", flush=True)
  else:
    print(word, end="", flush=True)

'''
output_ids = []
for step_result in step_results:
  is_new_word = step_result.token.startswith("▁")

  if is_new_word and output_ids:
    word = tokenizer.decode(tokenizer.convert_tokens_to_ids(step_result.token))
    print(word, end=" ", flush=True)
    output_ids = []

  output_ids.append(step_result.token)

if output_ids:
  word = tokenizer.decode(tokenizer.convert_tokens_to_ids(output_ids))
  print(word)'''