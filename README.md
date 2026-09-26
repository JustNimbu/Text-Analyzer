# Text Editor (CLI)

A small, menu-driven text editor that runs in the terminal. You can type or open a text file, run quick edits and statistics on it (word counts, find/replace, case conversion, and so on), and save it back to disk. It is written in pure Python and needs **no third-party packages**.

This README assumes no prior knowledge of the project. Follow the steps in order and you will have the app running in a few minutes.

---

## Table of Contents

1. [Project structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Setup (step by step)](#setup-step-by-step)
4. [Configuration](#configuration)
5. [Running the app](#running-the-app)
6. [Example session](#example-session)
7. [Verifying the installation](#verifying-the-installation)
8. [Features](#features)
9. [How it works](#how-it-works)
10. [Troubleshooting](#troubleshooting)
11. [Known limitations](#known-limitations)

---

## Project structure

```
your-project-folder/
├── text_app.py     # Interactive app: menus, prompts, main loop (entry point)
├── text_ops.py     # Helper functions: file I/O, text operations, logging
└── README.md
```

| File | Purpose |
|------|---------|
| `text_app.py` | **Entry point.** Shows the menus, reads user input, and keeps track of the current text and file. |
| `text_ops.py` | Reusable functions that do the real work. Contains no menus, so it can be imported and tested on its own. |

Both files **must be in the same folder**, because `text_app.py` imports from `text_ops.py`.

---

## Prerequisites

- **Python 3.6 or newer** (the code uses f-strings). Python 3.8+ is recommended.
- A terminal (Command Prompt / PowerShell on Windows, Terminal on macOS or Linux).
- No internet connection, database, or API keys are needed.

### Check whether Python is installed

```bash
python --version
```

If that fails or shows Python 2.x, try:

```bash
python3 --version
```

If neither works, install Python from <https://www.python.org/downloads/>. On Windows, tick **"Add Python to PATH"** in the installer.

> On macOS/Linux the command is often `python3`. On Windows it is usually `python` (or `py`). Use whichever works on your machine in every command below.

---

## Setup (step by step)

### Step 1: Get the project files

Put `text_app.py` and `text_ops.py` together in one folder. If the project is in a Git repository, clone it instead:

```bash
git clone <repository-url>
cd <repository-folder>
```

If you only have the two files, create a folder and copy them in:

```bash
mkdir text-editor
cd text-editor
# copy text_app.py and text_ops.py into this folder
```

Confirm both files are present:

```bash
# macOS / Linux
ls

# Windows (Command Prompt)
dir
```

You should see `text_app.py` and `text_ops.py`.

### Step 2: (Optional but recommended) Create a virtual environment

A virtual environment keeps this project isolated from other Python projects. Because this project has no dependencies, you can skip this step and it will still run.

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt)**

```bat
python -m venv venv
venv\Scripts\activate.bat
```

**Windows (PowerShell)**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

When activated, your prompt starts with `(venv)`. To leave the environment later, run `deactivate`.

> If PowerShell blocks the activation script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

### Step 3: Install dependencies

**There are no dependencies to install.** The project uses only Python's standard library (`os` and built-in functions), so there is no `pip install` step and no `requirements.txt` is needed.

### Step 4: Check the configuration

The app works with default settings and needs no configuration files or environment variables. See [Configuration](#configuration) if you want to change the log file name or the recent-files limit.

---

## Configuration

There are no config files, environment variables, or command-line flags. The only settings are two constants in the code, both optional to change:

| Setting | Location | Default | Description |
|---------|----------|---------|-------------|
| `LOG_FILE` | `text_app.py` (near the top) | `"text_editor_activity.log"` | File where activity is logged. It is created automatically in the folder you run the app from. |
| `max_items` | `add_recent_file()` in `text_ops.py` | `5` | How many recent files are remembered and shown in the File menu. |

Example: to write logs to `logs/editor.log`, first create the `logs` folder, then change:

```python
LOG_FILE = "logs/editor.log"
```

Note that logging errors (such as a missing folder) are silently ignored and will not crash the app.

---

## Running the app

From the project folder (with the virtual environment activated, if you created one):

```bash
python text_app.py
```

(or `python3 text_app.py` / `py text_app.py`, depending on your system)

You should see:

```
===== TEXT EDITOR =====
1. File
2. Edit / Tools
3. Exit
Choose:
```

Type a number and press **Enter** to choose an option. To quit, choose **3** (Exit). You can also press `Ctrl+C` to force-quit, but doing so will not prompt you to save.

> **Run the command from the project folder.** If you run it from somewhere else (for example `python path/to/text_app.py`), the log file and any relative save paths will be created in your current directory, not the project folder.

---

## Example session

Below is a short walkthrough you can follow to confirm everything works. Lines starting with `>` are what you type.

```
===== TEXT EDITOR =====
1. File
2. Edit / Tools
3. Exit
Choose: > 1

--- File Menu ---
1. New text
2. Open file
3. Save
4. Save As
5. Back
Choose: > 1
Enter/Paste your text:
> hello world hello
New text set.

--- File Menu ---
Choose: > 4
Enter save path: > notes.txt
Saved as: notes.txt

--- File Menu ---
Choose: > 5

===== TEXT EDITOR =====
Current file: notes.txt
Choose: > 2

--- Edit / Tools Menu ---
Choose: > 7
Enter word to count: > hello
Occurrences: 2

Choose: > 12        (Back)
Choose: > 3         (Exit)
No unsaved changes. Exiting.
```

After this, a `notes.txt` file and a `text_editor_activity.log` file exist in your folder.

---

## Verifying the installation

**1. Check that the helper module imports and works** (no menus involved):

```bash
python -c "from text_ops import count_words; print(count_words('hello big world'))"
```

Expected output: `3`

**2. Check that the app starts:**

```bash
python text_app.py
```

Expected: the main menu appears. Choose `3` to exit.

**3. Check the log file:**

```bash
# macOS / Linux
cat text_editor_activity.log

# Windows
type text_editor_activity.log
```

Expected: lines such as `APP STARTED` and `APP CLOSED`.

---

## Features

### File menu
- **New text:** type or paste a single line of text to start with.
- **Open file:** open a UTF-8 text file by path, or pick one of the recent files by its number.
- **Save / Save As:** write the current text to a file (Save asks for a path if none is set yet).
- **Recent files:** the last 5 files opened or saved in this session are listed in the File menu.
- The app asks before discarding unsaved changes when creating new text, opening a file, or exiting.

### Edit / Tools menu
(available only after text has been created or loaded)

1. Show current text
2. Total characters
3. Total words
4. Total lines
5. Convert case (`upper`, `lower`, `title`)
6. Remove extra spaces
7. Word occurrence count
8. Find word positions (character offsets, optional case sensitivity)
9. Replace word (first or all, optional case sensitivity)
10. Insert text at the end
11. Insert text at a character position

Every edit shows a preview and asks **"Keep this change? (y/n)"** before it is applied.

### Activity log
Actions such as opening, saving, and editing are appended to the log file (default `text_editor_activity.log`). Logging failures are silently ignored so they never interrupt the editor.

---

## How it works

`text_app.py` holds the state (`current_text`, `current_file`, `text_loaded`, `unsaved_changes`, `recent_files`) and passes it through the menu handlers, which return the updated values. All actual work is delegated to `text_ops.py`:

| Function | Description |
|----------|-------------|
| `load_from_input()` | Read text typed by the user |
| `load_from_file(path)` / `save_to_file(path, text)` | Read and write UTF-8 files |
| `append_log(log_path, message)` | Append a line to the log file |
| `count_characters`, `count_words`, `count_lines` | Basic statistics |
| `report_characters`, `report_words`, `report_lines` | Format a single stat as a one-line report (or "No text loaded.") |
| `convert_case(text, case_type)` | Upper, lower, or title case |
| `remove_extra_spaces(text)` | Normalize whitespace |
| `word_occurrence(text, word)` | Count whole-word matches (case-insensitive) |
| `find_word_positions(text, word, case_sensitive)` | Return start indexes of whole-word matches |
| `replace_word(text, old, new, only_first, case_sensitive)` | Replace occurrences |
| `insert_at_end(text, new_text)` | Append text to the end |
| `insert_at_position(text, new_text, position)` | Insert text at a character index (position is clamped to the valid range) |
| `add_recent_file(recent_list, path, max_items=5)` | Maintain the recent-files list |
| `sanitize_path_for_display(path)` | Show only the file name, not the full path |

---

## Troubleshooting

| Problem | Cause / Fix |
|---------|-------------|
| `python: command not found` | Try `python3` (macOS/Linux) or `py` (Windows). If none work, install Python (see [Prerequisites](#prerequisites)). |
| `ModuleNotFoundError: No module named 'text_ops'` | `text_ops.py` is not in the same folder as `text_app.py`, or you are running from a different directory. `cd` into the project folder and retry. |
| `SyntaxError` near an `f"..."` string | Your Python is older than 3.6. Upgrade Python. |
| "Cannot open this as a text file." | The file is binary or not UTF-8 encoded. Only UTF-8 text files are supported. |
| "File not found." | The path is wrong. Use a full path, or a path relative to the folder you launched the app from. |
| "Could not save file: ..." | The folder does not exist or you lack write permission. Use a different path. |
| "No text loaded. Use File > New or File > Open first." | The Edit / Tools menu needs text first. Choose `1` (File), then New text or Open file. |
| No log file appears | The app can't write to the current directory. Log errors are ignored by design; run from a writable folder. |

---

## Known limitations

- **Single-line input:** "New text" and "Insert text" use `input()`, so they read one line at a time. To work with multi-line text, open a file.
- **Whitespace:** "Remove extra spaces" also collapses newlines, so multi-line text becomes one line.
- **Insert text:** only *trailing* whitespace is stripped from text you insert (via `rstrip()`); leading whitespace is preserved.
- **Word occurrence / find positions:** matching treats a match as a "whole word" if the characters immediately before and after it are not alphanumeric. This correctly skips "category" when searching for "cat", and correctly matches "cat," or "cat!" since punctuation counts as a boundary — but it is a simple ASCII-style check, not a full Unicode word-boundary implementation.
- **Recent files:** the list only exists for the current run (it is not saved to disk) and is **not** cleared when you choose "New text" — it persists until you restart the app.
- **Statistics:** menu options 2, 3, and 4 each print a single number (characters, words, or lines respectively) — there is no combined summary view.
- **Exit:** any answer other than `y` at the exit prompt — including `skip` — discards unsaved changes and exits; `skip` is not currently handled as a separate "cancel" option.
