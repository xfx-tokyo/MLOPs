from transformers import CLIPTokenizer

def run(input_ids, skip_special_tokens=False, model="openai/clip-vit-large-patch14", local_cache_only=True):
    tokenizer = CLIPTokenizer.from_pretrained(model, subfolder="tokenizer", local_files_only=local_cache_only)
    string = tokenizer.decode(input_ids, skip_special_tokens)
    return string
