import tiktoken


def get_token_count(text: str, disallowed_special=[], chunk_size=1000) -> int:
    enc = tiktoken.get_encoding("cl100k_base")

    # Split the text into smaller chunks
    chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
    total_tokens = 0

    for chunk in chunks:
        tokens = enc.encode(chunk, disallowed_special=disallowed_special)
        total_tokens += len(tokens)

    return total_tokens
