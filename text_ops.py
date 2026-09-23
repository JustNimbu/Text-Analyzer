# text_ops.py

import os


def load_from_input():
    return input("Enter/Paste your text:\n")


def load_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_to_file(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def append_log(log_path, message):
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except Exception:
        pass


def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def count_lines(text):
    if text == "":
        return 0
    return len(text.splitlines())


def convert_case(text, case_type):
    case_type = case_type.strip().lower()
    if case_type == "upper":
        return text.upper()
    if case_type == "lower":
        return text.lower()
    if case_type == "title":
        return text.title()
    return text


def remove_extra_spaces(text):
    return " ".join(text.split())


def word_occurrence(text, word):
    if not word:
        return 0
    return text.lower().split().count(word.lower())


def find_word_positions(text, word, case_sensitive=False):
    if not word:
        return []
    search_text = text if case_sensitive else text.lower()
    search_word = word if case_sensitive else word.lower()
    positions = []
    start = 0
    while True:
        idx = search_text.find(search_word, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1
    return positions


def replace_word(text, old_word, new_word, only_first=False, case_sensitive=False):
    if not old_word:
        return text
    if case_sensitive:
        return _replace_case_sensitive(text, old_word, new_word, only_first)

    if only_first:
        idx = text.lower().find(old_word.lower())
        if idx == -1:
            return text
        return text[:idx] + new_word + text[idx + len(old_word):]

    return text.replace(old_word, new_word)


def _replace_case_sensitive(text, old_word, new_word, only_first):
    result = []
    start = 0
    count = 0
    while True:
        idx = text.find(old_word, start)
        if idx == -1:
            result.append(text[start:])
            break
        result.append(text[start:idx])
        result.append(new_word)
        start = idx + len(old_word)
        count += 1
        if only_first and count >= 1:
            result.append(text[start:])
            break
    return "".join(result)


def insert_at_end(text, new_text):
    return text + new_text


def insert_at_position(text, new_text, position):
    position = int(position)
    if position < 0:
        position = 0
    if position > len(text):
        position = len(text)
    return text[:position] + new_text + text[position:]


def show_current_text(text):
    if not text:
        return "(empty)"
    return text


def add_recent_file(recent_list, path, max_items=5):
    path = os.path.normpath(path)
    recent_list = [p for p in recent_list if os.path.normpath(p) != path]
    recent_list.insert(0, path)
    return recent_list[:max_items]


def report_stats(text):
    if not text:
        return "No text loaded."
    return (
        f"Characters: {count_characters(text)}\n"
        f"Words: {count_words(text)}\n"
        f"Lines: {count_lines(text)}"
    )


def sanitize_path_for_display(path):
    if not path:
        return None
    return os.path.basename(path)
