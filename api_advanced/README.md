# API Advanced

## 0. How many subs?

### Module Documentation
`0-subs.py` includes:
- A module docstring.
- A function docstring for `number_of_subscribers(subreddit)`.

### Importing in Alphabetical Order
Imports in `0-subs.py` are sorted alphabetically:
- `requests`

### Output: existing Subreddit
Example:
```bash
$ python3 0-main.py programming
756024
```
Note: The exact number changes over time.

### Output: nonexisting subreddit
Example:
```bash
$ python3 0-main.py this_is_a_fake_subreddit
0
```

### PEP8 validation
Run:
```bash
$ pycodestyle 0-subs.py
```
Expected output: no output (PEP8 compliant).
