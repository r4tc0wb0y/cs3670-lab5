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

## Files
- `flag_finder.py` — CLI tool
- `.gitignore`, `LICENSE`

