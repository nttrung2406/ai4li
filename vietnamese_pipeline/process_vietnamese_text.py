from pyvi import ViPosTagger
from remove_tones import remove_tones

def process_vietnamese_text(text: str) -> dict:
    """
    A full pipeline that processes Vietnamese text.
    
    Args:
        text: The input Vietnamese string.
        
    Returns:
        A dictionary containing the results of each processing step:
        - original_text: The original input text
        - tokenized_string: Text with compound words joined by underscores
        - tokens_list: List of individual tokens
        - pos_tags: List of (word, POS tag) tuples
        - no_tones_text: Text with tone marks removed
    """

    words, tags = ViPosTagger.postagging(text)
    
    pos_tags = list(zip(words, tags))
    tokenized_string = " ".join(words)
    tokens_list = words 
    text_without_tones = remove_tones(text)
    
    results = {
        "original_text": text,
        "tokenized_string": tokenized_string,
        "tokens_list": tokens_list,
        "pos_tags": pos_tags,
        "no_tones_text": text_without_tones
    }
    
    return results