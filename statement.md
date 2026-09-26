# Project Statement: Text Editor (CLI)

## 1. Problem Statement

Working with plain text often means opening a full graphical editor or word processor, even for small jobs: counting the words in a passage, cleaning up stray spaces, finding where a term appears, or swapping one word for another. Those tools can be heavy for quick tasks, need a graphical environment, and are hard to use on remote machines or in a terminal-only session.

At the same time, people learning to program need small, self-contained projects that show how file handling, string manipulation, user input, and program structure fit together. Many such examples put everything in one file, which makes them hard to read, extend, and test.

This project addresses both needs. It provides a lightweight, menu-driven text editor that runs entirely in the terminal and handles the most common text-processing tasks: loading, editing, analyzing, and saving text. Its code is split into a user-interface layer (`text_app.py`) and a reusable logic layer (`text_ops.py`), so it also works as a clear example of separating interaction from functionality.

## 2. Scope of the Project

### In scope

- **Interface:** a text-based, menu-driven command-line application with a main menu, a File menu, and an Edit / Tools menu.
- **Text input:** typing or pasting a line of text, or opening an existing UTF-8 text file by path or from a recent-files list.
- **Saving:** Save and Save As to a UTF-8 text file, with prompts to prevent accidental loss of unsaved changes when creating new text, opening a file, or exiting.
- **Analysis:** character, word, and line counts; word occurrence counts; and locating the character positions of a word.
- **Editing:** case conversion (upper, lower, title), whitespace cleanup, find-and-replace (first or all matches, optional case sensitivity), and inserting text at the end or at a chosen position.
- **Safe editing workflow:** every edit is previewed and applied only after the user confirms it.
- **Session convenience:** a recent-files list (up to 5 files) for the current session.
- **Activity logging:** a plain-text log of actions such as opening, saving, editing, and starting or closing the app.
- **Environment:** Python 3.6 or newer using only the standard library, with no installation of external packages.

### Out of scope

- A graphical user interface or a web interface.
- Multi-line, cursor-based editing; text entry and insertion are one line at a time, and larger text is handled by opening a file.
- Rich-text or binary formats (Word, PDF, and so on); only UTF-8 plain text is supported.
- Undo/redo history, syntax highlighting, spell checking, or regular-expression search.
- Persistent settings, or a recent-files list that is kept between sessions.
- Multi-user, networked, or cloud-based editing.
- Automated tests and packaging for distribution (for example, publishing to PyPI).

## 3. Target Users

| User | How they benefit |
|------|------------------|
| **Students and beginners learning Python** | A readable, working example of file I/O, string methods, loops, functions, and modular design, with the interface and logic kept in separate modules. |
| **Instructors and evaluators** | A small, self-contained project that is easy to run, review, and assess, with no dependencies or setup beyond Python. |
| **Terminal and command-line users** | A quick way to inspect and clean up text without leaving the terminal or launching a heavier application. |
| **Users on minimal or remote systems** | Works over SSH or on machines with no graphical environment, since it needs only Python. |
| **Developers extending the project** | A cleanly separated logic layer (`text_ops.py`) that can be imported into other scripts or covered by unit tests. |

## 4. High-Level Features

1. **Menu-driven navigation.** A main menu leads to File and Edit / Tools menus, so the app can be used without memorizing commands.
2. **File management.** Create new text, open files by path or from the recent list, and save or save-as, with prompts before unsaved work is discarded.
3. **Text statistics.** Report character, word, and line counts for the current text.
4. **Search tools.** Count how often a word occurs (always case-insensitive) and list every character position where it appears, with an optional case-sensitive mode for the position search.
5. **Editing tools.** Convert case, remove extra whitespace, replace words (first or all occurrences, optional case sensitivity), and insert text at the end or at a chosen position.
6. **Preview and confirm.** Each change is shown first and applied only if the user confirms, so accidental edits can be avoided.
7. **Recent files.** Quick reopening of files from the current session, showing only file names for a cleaner display.
8. **Activity log.** A running record of actions in `text_editor_activity.log` that never interrupts the app if writing to it fails.
9. **Error handling.** Clear messages for missing files, non-text files, invalid positions, and save failures instead of crashes.
10. **Modular design.** Interface code and text-processing logic are in separate files, which makes the project easier to maintain, extend, and test.
