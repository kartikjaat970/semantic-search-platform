def _snap_back_to_whitespace(text, start, end, min_len):
    """Move `end` back to just after the last whitespace, if one is found
    at least `min_len` characters into the chunk. Avoids cutting words."""
    for i in range(end, start + min_len, -1):
        if text[i - 1].isspace():
            return i
    return end


def split_text(text, size=500, overlap=50):
    """Split text into chunks of at most `size` characters.

    Chunks break at whitespace where possible and consecutive chunks share
    roughly `overlap` characters, so a sentence cut at a boundary still
    appears whole in one of the two chunks.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    if not 0 <= overlap < size:
        raise ValueError("overlap must be between 0 and size - 1")

    text = text.strip()
    n = len(text)
    chunks = []
    start = 0

    while start < n:
        end = min(start + size, n)
        if end < n:
            end = _snap_back_to_whitespace(text, start, end, size // 2)

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end >= n:
            break

        # Step back by `overlap`, then forward to the next word boundary so
        # the next chunk does not begin mid-word. Always make progress.
        next_start = end - overlap
        while next_start < end and not text[next_start - 1].isspace():
            next_start += 1
        start = max(next_start, start + 1)

    return chunks
