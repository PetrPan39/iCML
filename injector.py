import hashlib
import shutil
from pathlib import Path

def inject_majak(file_path):
    src = Path(file_path)
    if not src.exists(): return None

    content = src.read_text()
    majak_line = "\n# MAJAK_FINGERPRINT: " + hashlib.md5(content.encode()).hexdigest()
    new_content = content + majak_line

    new_file = src.parent / ("majak_" + src.name)
    new_file.write_text(new_content)
    return str(new_file)
