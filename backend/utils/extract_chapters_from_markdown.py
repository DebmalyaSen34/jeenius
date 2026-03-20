import re
import os
from pathlib import Path

def split_markdown_by_chapter(input_file: str, output_dir: str):
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    os.makedirs(output_dir, exist_ok=True)

    chapter_pattern = r'^##\s*Chapter\s*(\d+)\s*(.*)$'

    chapters = []
    current_chapter = None
    current_content = []

    for line in content.split('\n'):
        match = re.match(chapter_pattern, line)

        if match:
            if current_chapter:
                chapters.append({
                    'title': current_chapter,
                    'content': '\n'.join(current_content)
                })

            current_chapter = match.group(2).strip()
            current_content = [line]
        else:
            if current_chapter:
                current_content.append(line)

    if current_chapter:
        chapters.append({
            'title': current_chapter,
            'content': '\n'.join(current_content)
        })

    print(f"Found {len(chapters)} chapters")

    for i, chapter in enumerate(chapters):
        title = chapter['title']
        filename = f"chapter_{i+1}_{title.replace(' ', '_')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chapter['content'])

        print(f"Saved chapter '{title}' to {filepath}")
        
    return chapters


if __name__ == "__main__":
    chapters = split_markdown_by_chapter('data/processed/hc_verma_full_textbook.md', 'data/processed/chapters')