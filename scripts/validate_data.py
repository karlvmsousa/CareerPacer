"""
Validates CareerPacer Markdown entries against their JSON Schemas.

Flow: extract YAML frontmatter -> validate against schema/*.json ->
check referential integrity (linked_actions, growth_areas against data/idp/)
-> report PASS/FAIL per file.

Exit codes:
    0: All files passed validation.
    1: One or more files failed data validation (schema or integrity error).
    2: Usage/argument error (e.g., target file does not exist).

Usage:
    pip install -r requirements.txt               # install dependencies
    python scripts/validate_data.py              # scan entire data/ directory
    python scripts/validate_data.py <file.md>     # validate a single file
"""

import argparse
import json
import sys
import re
from pathlib import Path
import yaml
from jsonschema import validate, ValidationError, FormatChecker

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SCHEMA_DIR = BASE_DIR / "schema"

SCHEMA_MAP = {
    "1on1": "1on1.schema.json",
    "idp": "idp-action.schema.json",
    "evaluation": "performance-eval.schema.json"
}

def load_frontmatter(filepath: Path) -> dict:
    """Extracts and parses the YAML frontmatter from a Markdown file."""
    try:
        content = filepath.read_text(encoding="utf-8")
        match = re.search(r'^-{3}\n(.*?)\n-{3}', content, re.MULTILINE | re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1))
        return {}
    except Exception as e:
        return {"_error": f"Failed to read or parse file: {str(e)}"}

def load_schema(schema_name: str) -> dict:
    """Loads a JSON schema file into a Python dictionary."""
    schema_path = SCHEMA_DIR / schema_name
    return json.loads(schema_path.read_text(encoding="utf-8"))

def build_valid_idp_set() -> set:
    """Builds a set of all valid IDP action IDs currently on disk."""
    valid_ids = set()
    idp_dir = DATA_DIR / "idp"
    if idp_dir.exists():
        for file in idp_dir.glob("*.md"):
            data = load_frontmatter(file)
            for action in data.get("actions", []):
                if "id" in action:
                    valid_ids.add(action["id"])
    return valid_ids

def validate_file(filepath: Path, valid_idps: set) -> list:
    """Validates a file's frontmatter against its schema and checks referential integrity."""
    errors = []
    parent_folder = filepath.parent.name
    
    if parent_folder not in SCHEMA_MAP:
        return [f"Unknown entity folder: {parent_folder}"]

    data = load_frontmatter(filepath)
    if "_error" in data:
        return [data["_error"]]
    
    if not data:
        return ["No YAML frontmatter found."]

    schema = load_schema(SCHEMA_MAP[parent_folder])
    normalized_data = json.loads(json.dumps(data, default=str))
    try:
        validate(instance=normalized_data, schema=schema, format_checker=FormatChecker())
    except ValidationError as e:
        errors.append(f"Schema Error: {e.message} (Path: {'/'.join(map(str, e.path))})")

    # Referential Integrity
    if parent_folder == "1on1":
        for action_id in data.get("linked_actions", []):
            if action_id not in valid_idps:
                errors.append(f"Integrity Error: linked_action '{action_id}' not found in any data/idp/ file.")
                
    elif parent_folder == "evaluation":
        for action_id in data.get("growth_areas", []):
            if action_id not in valid_idps:
                errors.append(f"Integrity Error: growth_area '{action_id}' not found in any data/idp/ file.")

    return errors

def main():
    """CLI entrypoint. Runs validation on a target file or the entire data directory."""
    parser = argparse.ArgumentParser(description="Validate CareerPacer data files.")
    parser.add_argument("file", nargs="?", help="Optional specific file to validate.")
    args = parser.parse_args()

    valid_idps = build_valid_idp_set()
    
    files_to_check = []
    if args.file:
        file_path = Path(args.file).resolve()
        if not file_path.exists():
            print(f"Error: File '{file_path}' does not exist.")
            sys.exit(2)
        files_to_check.append(file_path)
    else:
        for folder in SCHEMA_MAP.keys():
            folder_path = DATA_DIR / folder
            if folder_path.exists():
                files_to_check.extend(folder_path.glob("*.md"))

    has_errors = False

    for filepath in files_to_check:
        relative_path = filepath.relative_to(BASE_DIR)
        errors = validate_file(filepath, valid_idps)
        
        if errors:
            has_errors = True
            print(f"FAIL: {relative_path}")
            for err in errors:
                print(f"    - {err}")
        else:
            print(f"PASS: {relative_path}")

    if has_errors:
        sys.exit(1)
    else:
        print("\nAll checks passed successfully.")
        sys.exit(0)

if __name__ == "__main__":
    main()