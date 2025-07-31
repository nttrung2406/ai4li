import unicodedata

def remove_tones(text: str) -> str:
    """
    Removes Vietnamese tone marks from a string.
    This is useful for search normalization or creating URL slugs.
    
    It uses Unicode normalization (NFD) to separate base characters 
    from their diacritical marks, then removes the marks.
    
    Example: 'tiếng Việt' -> 'tieng Viet'
    
    Args:
        text: The input Vietnamese string.
        
    Returns:
        str: The text with tone marks removed.
    """
    normalized_text = unicodedata.normalize('NFD', text)
    
    return "".join(c for c in normalized_text if unicodedata.category(c) != 'Mn')
