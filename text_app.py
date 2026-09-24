# text_app.py

from text_ops import (
    load_from_input,
    load_from_file,
    save_to_file,
    append_log,
    count_characters,
    count_words,
    count_lines,
    convert_case,
    remove_extra_spaces,
    word_occurrence,
    find_word_positions,
    replace_word,
    insert_at_end,
    insert_at_position,
    show_current_text,
    add_recent_file,
    report_stats,
    sanitize_path_for_display,
)


LOG_FILE = "text_editor_activity.log"


def show_main_menu(current_file):
    print("\n===== TEXT EDITOR =====")
    display_name = sanitize_path_for_display(current_file)
    if display_name:
        print(f"Current file: {display_name}")
    print("1. File")
    print("2. Edit / Tools")
    print("3. Exit")
    return input("Choose: ").strip()


def show_file_menu(recent_files):
    print("\n--- File Menu ---")
    print("1. New text")
    print("2. Open file")
    if recent_files:
        print("   Recent files:")
        for i, rf in enumerate(recent_files, 1):
            print(f"   {i}. {sanitize_path_for_display(rf)}")
    print("3. Save")
    print("4. Save As")
    print("5. Back")
    return input("Choose: ").strip()


def show_tools_menu():
    print("\n--- Edit / Tools Menu ---")
    print("1. Show current text")
    print("2. Total characters")
    print("3. Total words")
    print("4. Total lines")
    print("5. Convert case (upper/lower/title)")
    print("6. Remove extra spaces")
    print("7. Word occurrence count")
    print("8. Find word positions")
    print("9. Replace word")
    print("10. Insert text at end")
    print("11. Insert text at position")
    print("12. Back")
    return input("Choose: ").strip()


def handle_file_menu(current_text, current_file, text_loaded, unsaved_changes, recent_files):
    while True:
        choice = show_file_menu(recent_files)

        if choice == "1":
            if unsaved_changes:
                answer = input("Unsaved changes exist. Save before new? (y/n): ").strip().lower()
                if answer == "y":
                    target = current_file if current_file else input("Enter save path: ")
                    try:
                        save_to_file(target, current_text)
                        current_file = target
                        unsaved_changes = False
                        recent_files = add_recent_file(recent_files, target)
                        append_log(LOG_FILE, f"SAVED: {target}")
                        print("Saved.")
                    except Exception as e:
                        print("Could not save:", e)
                else:
                    print("Discarded unsaved changes.")
            current_text = load_from_input()
            current_file = None
            text_loaded = True
            unsaved_changes = False
            recent_files = []
            append_log(LOG_FILE, "NEW: typed text")
            print("New text set.")

        elif choice == "2":
            if unsaved_changes:
                answer = input("Unsaved changes exist. Save before opening? (y/n): ").strip().lower()
                if answer == "y":
                    target = current_file if current_file else input("Enter save path: ").strip()
                    try:
                        save_to_file(target, current_text)
                        current_file = target
                        unsaved_changes = False
                        recent_files = add_recent_file(recent_files, target)
                        append_log(LOG_FILE, f"SAVED: {target}")
                        print("Saved.")
                    except Exception as e:
                        print("Could not save:", e)
                else:
                    print("Discarded unsaved changes.")

            sub = input("Enter path or recent number: ").strip()
            selected_path = None

            if sub.isdigit():
                idx = int(sub) - 1
                if 0 <= idx < len(recent_files):
                    selected_path = recent_files[idx]
                    print("Opening recent file:", sanitize_path_for_display(selected_path))
                else:
                    print("No such recent file.")
                    continue
            else:
                selected_path = sub

            if selected_path:
                try:
                    current_text = load_from_file(selected_path)
                    current_file = selected_path
                    text_loaded = True
                    unsaved_changes = False
                    recent_files = add_recent_file(recent_files, selected_path)
                    append_log(LOG_FILE, f"OPENED: {selected_path}")
                    print("File opened.")
                except UnicodeDecodeError:
                    print("Cannot open this as a text file.")
                    append_log(LOG_FILE, f"OPEN FAILED: {selected_path} - not a text file")
                except FileNotFoundError:
                    print("File not found.")
                    append_log(LOG_FILE, f"OPEN FAILED: {selected_path} - not found")
                except Exception as e:
                    print("Could not open file:", e)
                    append_log(LOG_FILE, f"OPEN FAILED: {selected_path} - {e}")

        elif choice == "3":
            if not text_loaded:
                print("Nothing to save.")
            else:
                target = current_file if current_file else input("Enter save path: ").strip()
                if not target:
                    print("No path provided.")
                    continue
                try:
                    save_to_file(target, current_text)
                    current_file = target
                    unsaved_changes = False
                    recent_files = add_recent_file(recent_files, target)
                    append_log(LOG_FILE, f"SAVED: {target}")
                    print("Saved.")
                except Exception as e:
                    print("Could not save file:", e)
                    append_log(LOG_FILE, f"SAVE FAILED: {target} - {e}")

        elif choice == "4":
            target = input("Enter save path: ").strip()
            if not target:
                print("No path provided.")
                continue
            try:
                save_to_file(target, current_text)
                current_file = target
                unsaved_changes = False
                recent_files = add_recent_file(recent_files, target)
                append_log(LOG_FILE, f"SAVED AS: {target}")
                print("Saved as:", target)
            except Exception as e:
                print("Could not save file:", e)
                append_log(LOG_FILE, f"SAVE AS FAILED: {target} - {e}")

        elif choice == "5":
            return current_text, current_file, text_loaded, unsaved_changes, recent_files

        else:
            print("Invalid choice.")

    return current_text, current_file, text_loaded, unsaved_changes, recent_files


def handle_tools_menu(current_text, current_file, text_loaded, unsaved_changes):
    while True:
        choice = show_tools_menu()

        if choice == "1":
            print("\n--- Current Text ---")
            print(show_current_text(current_text))
            print("---------------------\n")

        elif choice == "2":
            print("\n" + report_stats(current_text))

        elif choice == "3":
            print("\n" + report_stats(current_text))

        elif choice == "4":
            print("\n" + report_stats(current_text))

        elif choice == "5":
            fmt = input("Enter format (upper/lower/title): ").strip()
            result = convert_case(current_text, fmt)
            print("\nConverted text:\n", result)
            keep = input("Keep this change? (y/n): ").strip().lower()
            if keep == "y":
                current_text = result
                unsaved_changes = True
                append_log(LOG_FILE, f"EDIT: case converted to {fmt}")

        elif choice == "6":
            result = remove_extra_spaces(current_text)
            print("\nCleaned text:\n", result)
            keep = input("Keep this change? (y/n): ").strip().lower()
            if keep == "y":
                current_text = result
                unsaved_changes = True
                append_log(LOG_FILE, "EDIT: extra spaces removed")

        elif choice == "7":
            word = input("Enter word to count: ").strip()
            print("\nOccurrences:", word_occurrence(current_text, word))

        elif choice == "8":
            word = input("Enter word to find: ").strip()
            case_sensitive = input("Case sensitive? (y/n): ").strip().lower() == "y"
            positions = find_word_positions(current_text, word, case_sensitive)
            if not positions:
                print("\nWord not found.")
            else:
                print(f"\nFound {len(positions)} time(s) at position(s):")
                print(positions)

        elif choice == "9":
            old = input("Word to replace: ").strip()
            new = input("Replace with: ").strip()
            only_first = input("Replace only first? (y/n): ").strip().lower() == "y"
            case_sensitive = input("Case sensitive? (y/n): ").strip().lower() == "y"
            result = replace_word(current_text, old, new, only_first, case_sensitive)
            print("\nUpdated text:\n", result)
            keep = input("Keep this change? (y/n): ").strip().lower()
            if keep == "y":
                current_text = result
                unsaved_changes = True
                append_log(LOG_FILE, f"EDIT: replaced '{old}' with '{new}'")

        elif choice == "10":
            added = input("Text to insert at end: ").strip()
            result = insert_at_end(current_text, added)
            print("\nUpdated text:\n", result)
            keep = input("Keep this change? (y/n): ").strip().lower()
            if keep == "y":
                current_text = result
                unsaved_changes = True
                append_log(LOG_FILE, "EDIT: text inserted at end")

        elif choice == "11":
            pos = input("Insert at character position: ").strip()
            added = input("Text to insert: ").strip()
            try:
                result = insert_at_position(current_text, added, pos)
                print("\nUpdated text:\n", result)
                keep = input("Keep this change? (y/n): ").strip().lower()
                if keep == "y":
                    current_text = result
                    unsaved_changes = True
                    append_log(LOG_FILE, f"EDIT: text inserted at position {pos}")
            except Exception:
                print("Invalid position.")

        elif choice == "12":
            return current_text, current_file, text_loaded, unsaved_changes

        else:
            print("Invalid choice.")

    return current_text, current_file, text_loaded, unsaved_changes


def confirm_exit(current_text, current_file, text_loaded, unsaved_changes, recent_files):
    if not unsaved_changes:
        print("No unsaved changes. Exiting.")
        append_log(LOG_FILE, "EXIT: no unsaved changes")
        return current_text, current_file, text_loaded, True, recent_files

    response = input(
        "You have unsaved changes. Save before exiting? (y/n/skip): "
    ).strip().lower()

    if response == "y":
        if current_file:
            try:
                save_to_file(current_file, current_text)
                unsaved_changes = True
                append_log(LOG_FILE, f"SAVED ON EXIT: {current_file}")
                print("Saved.")
            except Exception as e:
                print("Could not save:", e)
                append_log(LOG_FILE, f"SAVE ON EXIT FAILED: {current_file} - {e}")
        else:
            path = input("Enter save path: ").strip()
            if path:
                try:
                    save_to_file(path, current_text)
                    unsaved_changes = False
                    append_log(LOG_FILE, f"SAVED ON EXIT: {path}")
                    print("Saved.")
                except Exception as e:
                    print("Could not save:", e)
                    append_log(LOG_FILE, f"SAVE ON EXIT FAILED: {path} - {e}")
        return current_text, current_file, text_loaded, False, recent_files

    print("Exiting without saving.")
    append_log(LOG_FILE, "EXIT: unsaved changes discarded")
    return "", None, False, False, recent_files


def main():
    current_text = ""
    current_file = None
    text_loaded = False
    unsaved_changes = False
    recent_files = []

    append_log(LOG_FILE, "APP STARTED")

    while True:
        main_choice = show_main_menu(current_file)

        if main_choice == "1":
            current_text, current_file, text_loaded, unsaved_changes, recent_files = (
                handle_file_menu(current_text, current_file, text_loaded, unsaved_changes, recent_files)
            )

        elif main_choice == "2":
            if not text_loaded:
                print("\nNo text loaded. Use File > New or File > Open first.")
                continue
            current_text, current_file, text_loaded, unsaved_changes = (
                handle_tools_menu(current_text, current_file, text_loaded, unsaved_changes)
            )

        elif main_choice == "3":
            current_text, current_file, text_loaded, unsaved_changes, recent_files = (
                confirm_exit(current_text, current_file, text_loaded, unsaved_changes, recent_files)
            )
            if not text_loaded:
                break

        else:
            print("Invalid choice.")

    append_log(LOG_FILE, "APP CLOSED")


if __name__ == "__main__":
    main()
