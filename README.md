# luit-sept-2025-red-python

This repository is for the **Level Up In Tech – September 2025 Red Python Cohort**.  
It will hold practice Python scripts created during live calls and independent exercises.  

## Getting Started

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd luit-sept-2025-red-python
   ```

---

## Scripts

### `hello_world.py`
A very simple script that prints **"Hello World"** to the console.  
This is often the first program written when learning a new language.  

Run it with:
```bash
python hello_world.py
```

Expected output:
```
Hello World
```

---

### `using_imports.py`
A more advanced script that demonstrates:
- Using **common Python libraries** (`os`, `sys`, `random`)
- Plotting data with **matplotlib**
- Generating ASCII art with the obscure **pyfiglet** library
- Calling the `say_hello()` function from **hello_world.py**

Run it with:
```bash
python using_imports.py
```

Example output (truncated for readability):
```
Current working directory: /your/path
Python executable: /usr/bin/python3
Random numbers: [3, 7, 1, 9, 4, 0, 6, 2, 8, 5]

 _   _      _ _         __        __         _     _ 
| | | | ___| | | ___    \ \      / /__  _ __| | __| |
| |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` |
|  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |
|_| |_|\___|_|_|\___/      \_/\_/ \___/|_|  |_|\__,_|
```

Note: The matplotlib window will also pop up with a plot of the random numbers.

---

## Code Quality with Ruff

We use [Ruff](https://docs.astral.sh/ruff/) to enforce code quality and formatting.

### Install Ruff
```bash
pip install ruff
```

### Format Code
Automatically format your Python files:
```bash
ruff format
```

### Lint and Auto-Fix Issues
Check code for style, import sorting, and other issues, and fix them automatically:
```bash
ruff check --fix
```

Ruff is very fast and ensures the codebase stays clean and consistent.
