# Text Editor (CLI)

A small menu-driven text editor for the terminal. You can type or open text, run some quick edits and statistics on it, and save it back to a file. It uses only the Python standard library.

## Files

| File | Purpose |
|------|---------|
| `text_app.py` | The interactive app: menus, user prompts, and the main loop. |
| `text_ops.py` | Helper functions for file I/O, text operations, logging, and formatting. Contains no menus, so it is easy to test on its own. |

## Requirements

- Python 3.6+ (uses f-strings)
- No third-party packages

## Running

Keep both files in the same folder, then run:

```bash
python text_app.py
```

## Features

### File menu
- **New text**: type or paste a single line of text to start with.
- **Open file**: open a UTF-8 text file by path, or pick one of the recent files by number.
- **Save / Save As**: write the current text to a file.
- **Recent files**: the last 5 files opened or saved in this session are listed in the File menu.
- If you have unsaved changes, the app asks before creating new text, opening a file, or exiting.

### Edit / Tools menu
- Show current text
- Character, word, and line counts
- Convert case (`upper`, `lower`, `title`)
- Remove extra spaces (collapses all whitespace into single spaces)
- Word occurrence count
- Find word positions (character offsets, optional case sensitivity)
- Replace word (replace first or all, optional case sensitivity)
- Insert text at the end or at a character position

Every edit shows a preview and asks **"Keep this change? (y/n)"** before it is applied.

### Activity log
Actions such as opening, saving, and editing are appended to `text_editor_activity.log` in the current working directory. Logging failures are silently ignored so they never interrupt the editor.

## How it works

`text_app.py` holds the state (`current_text`, `current_file`, `text_loaded`, `unsaved_changes`, `recent_files`) and passes it through the menu handlers, which return the updated values. All actual work is delegated to `text_ops.py`:

| Function | Description |
|----------|-------------|
| `load_from_input()` | Read text typed by the user |
| `load_from_file(path)` / `save_to_file(path, text)` | Read and write UTF-8 files |
| `append_log(log_path, message)` | Append a line to the log file |
| `count_characters`, `count_words`, `count_lines` | Basic statistics |
| `convert_case(text, case_type)` | Upper, lower, or title case |
| `remove_extra_spaces(text)` | Normalize whitespace |
| `word_occurrence(text, word)` | Count whole-word matches (case-insensitive) |
| `find_word_positions(text, word, case_sensitive)` | Return start indexes of matches |
| `replace_word(text, old, new, only_first, case_sensitive)` | Replace occurrences |
| `insert_at_end`, `insert_at_position` | Insert text (position is clamped to valid range) |
| `add_recent_file(recent_list, path, max_items=5)` | Maintain the recent-files list |
| `report_stats(text)` | Format the character/word/line summary |
| `sanitize_path_for_display(path)` | Show only the file name, not the full path |

## Notes and limitations

- **Single-line input:** "New text" and "Insert text" use `input()`, so they read one line at a time. To work with multi-line text, open a file.
- **Whitespace:** "Remove extra spaces" also collapses newlines, so multi-line text becomes one line.
- **Word count/occurrence** split on whitespace, so a word followed by punctuation (e.g. `hello,`) won't match `hello`.
- **Find positions** does substring matching, so it also finds a word inside longer words.
- **Replace (case-insensitive, replace all):** currently uses a plain `str.replace`, which is case-sensitive. Replace-first and the case-sensitive path behave as expected.
- **Recent files** are kept in memory only and are reset when you choose "New text" or restart the app.
- **Statistics:** menu options 2, 3, and 4 all display the same combined summary.
- **Exit:** any answer other than `y` at the exit prompt discards unsaved changes.
