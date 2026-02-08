
import os

OUTPUT_FILE = "project_context.md"

# Directories/Files to Include
INCLUDE_DIRS = ["src", "docs", "tests", "scripts"]
INCLUDE_FILES = ["main.py", "requirements.txt", ".env.example"]

# Directories/Files to Exclude
EXCLUDE_DIRS = [".venv", "__pycache__", ".git", "pine_scripts", "data", "Lib", "Include", "Scripts"]
EXCLUDE_EXTENSIONS = [".pyc", ".pyd", ".log", ".jsonl"]

def get_file_content(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def main():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# Adaptive Trading Assistant - Project Context\n\n")
        
        # 1. Directory Structure
        out.write("## 1. Directory Structure\n```\n")
        for root, dirs, files in os.walk("."):
            # Filter excludes
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
            
            level = root.replace(".", "").count(os.sep)
            indent = " " * 4 * (level)
            out.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = " " * 4 * (level + 1)
            for f in files:
                if not any(f.endswith(ext) for ext in EXCLUDE_EXTENSIONS) and f != OUTPUT_FILE:
                    out.write(f"{subindent}{f}\n")
        out.write("```\n\n")

        # 2. File Contents
        out.write("## 2. File Contents\n\n")
        
        # Root Files
        for f in INCLUDE_FILES:
            if os.path.exists(f):
                content = get_file_content(f)
                out.write(f"### File: `{f}`\n\n```python\n{content}\n```\n\n")

        # Directory Walk
        for target_dir in INCLUDE_DIRS:
            for root, dirs, files in os.walk(target_dir):
                # Filter excludes
                dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
                
                for file in files:
                    if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                        continue
                        
                    filepath = os.path.join(root, file)
                    # Determine language for markdown fencing
                    ext = os.path.splitext(file)[1]
                    lang = "python" if ext == ".py" else "markdown" if ext == ".md" else "text"
                    
                    content = get_file_content(filepath)
                    out.write(f"### File: `{filepath.replace(os.sep, '/')}`\n\n```{lang}\n{content}\n```\n\n")

    print(f"Project exported to {os.path.abspath(OUTPUT_FILE)}")

if __name__ == "__main__":
    main()
