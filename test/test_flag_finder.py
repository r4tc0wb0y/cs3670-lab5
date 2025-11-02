from pathlib import Path
from flag_finder import scan_dir, DEFAULT_PATTERN

def test_finds_flag(tmp_path: Path):
    sample = tmp_path / "note.txt"
    sample.write_text("hello ctf{example_flag_123}\n")
    hits = scan_dir(tmp_path, DEFAULT_PATTERN)
    assert any("ctf{example_flag_123}" in hit[2] for hit in hits)
