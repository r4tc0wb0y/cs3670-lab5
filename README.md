# Flag Finder CLI

A tiny Python CLI that finds CTF-style flags (`ctf{...}`) inside a directory.

## Quick start
```bash
python3 flag_finder.py .
# or
./flag_finder.py sample_data
```

You should see a result like:
```
ctf{sample_flag_for_testing}  ->  sample_data/demo.txt:1
```

## Run tests (optional)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install pytest
pytest -q
```

## Files
- `flag_finder.py` — CLI tool
- `tests/test_flag_finder.py` — minimal pytest
- `sample_data/` — includes a demo file with a test flag
- `.gitignore`, `LICENSE`

## License
MIT
