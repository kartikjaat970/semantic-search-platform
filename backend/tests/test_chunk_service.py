import pytest

from services.chunk_service import split_text


def test_empty_text_gives_no_chunks():
    assert split_text("") == []
    assert split_text("   \n ") == []


def test_short_text_is_one_chunk():
    assert split_text("hello world") == ["hello world"]


def test_chunks_respect_size_limit():
    text = " ".join(f"word{i}" for i in range(500))
    assert all(len(c) <= 100 for c in split_text(text, size=100, overlap=20))


def test_words_are_not_cut_in_half():
    words = [f"word{i}" for i in range(500)]
    text = " ".join(words)
    valid = set(words)
    for chunk in split_text(text, size=100, overlap=20):
        assert set(chunk.split()) <= valid


def test_no_text_is_lost():
    words = [f"word{i}" for i in range(500)]
    chunks = split_text(" ".join(words), size=100, overlap=20)
    seen = {w for c in chunks for w in c.split()}
    assert seen == set(words)


def test_consecutive_chunks_overlap():
    text = " ".join(f"word{i}" for i in range(500))
    chunks = split_text(text, size=100, overlap=30)
    assert len(chunks) > 2
    for a, b in zip(chunks, chunks[1:]):
        assert set(a.split()) & set(b.split())


def test_long_unbroken_string_still_terminates():
    chunks = split_text("x" * 2000, size=500, overlap=50)
    assert "".join(chunks).count("x") >= 2000
    assert all(len(c) <= 500 for c in chunks)


def test_invalid_arguments():
    with pytest.raises(ValueError):
        split_text("abc", size=0)
    with pytest.raises(ValueError):
        split_text("abc", size=10, overlap=10)
