#!/usr/bin/env python
import os
import json


def read_note(note):
    try:
        with open(note, 'r', encoding='utf-8') as n:
            note_content = n.read()
            return note_content
    except FileNotFoundError:
        return None


def get_unfinished_tasks(note_content):
    if note_content is None:
        return None
    lines = note_content.split('\n')
    unfinished_tasks = []

    for i, line in enumerate(lines):
        if line.startswith("- [ ]"):
            task_text = line.strip()[6:]

            start_index = i + 1
            task_description_lines = [lines[j].strip() for j in range(
                start_index, len(lines)) if lines[j].strip()]
            task_description = ' '.join(task_description_lines)

            unfinished_tasks.append(
                {"text": task_text, "tooltip": task_description})

    return unfinished_tasks


def main():
    note_path = os.path.expanduser("~/obsidian-vault/Obsidian Vault/todo.md")
    note_content = read_note(note_path)

    if note_content:
        unfinished_tasks = get_unfinished_tasks(note_content)

        if unfinished_tasks:
            json_data = {
                "text": unfinished_tasks[0]["text"],
                "tooltip": unfinished_tasks[0]["tooltip"],
                "class": "obsidian"
            }
            print(json.dumps(json_data))
        print('{"text": "", "class": "obsidian"}')
    print('{"text": "", "class": "obsidian"}')


if __name__ == "__main__":
    main()
