import os
import hashlib
import json

# === CONFIGURATION ===
MONITORED_DIR = "./monitor_folder"  # Change to your target directory
HASH_RECORD_FILE = "file_hashes.json"

def calculate_hash(filepath):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error hashing {filepath}: {e}")
        return None

def scan_directory(directory):
    """Scan directory and return dict of file paths and their hashes."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            hashval = calculate_hash(filepath)
            if hashval:
                file_hashes[filepath] = hashval
    return file_hashes

def load_hashes():
    """Load previous hashes from file."""
    if not os.path.exists(HASH_RECORD_FILE):
        return {}
    with open(HASH_RECORD_FILE, "r") as f:
        return json.load(f)

def save_hashes(hashes):
    """Save current hashes to file."""
    with open(HASH_RECORD_FILE, "w") as f:
        json.dump(hashes, f, indent=2)

def compare_hashes(old, new):
    """Compare old and new hashes; return lists of changed, added, deleted files."""
    changed = []
    added = []
    deleted = []

    for filepath in new:
        if filepath not in old:
            added.append(filepath)
        elif old[filepath] != new[filepath]:
            changed.append(filepath)
    for filepath in old:
        if filepath not in new:
            deleted.append(filepath)
    return changed, added, deleted

def main():
    print(f"Scanning directory: {MONITORED_DIR}")
    current_hashes = scan_directory(MONITORED_DIR)
    previous_hashes = load_hashes()

    changed, added, deleted = compare_hashes(previous_hashes, current_hashes)

    if not previous_hashes:
        print("No previous hash record found. Baseline created.")
    else:
        if changed:
            print("\n[!] Modified files:")
            for f in changed:
                print(f"  - {f}")
        if added:
            print("\n[+] Added files:")
            for f in added:
                print(f"  - {f}")
        if deleted:
            print("\n[-] Deleted files:")
            for f in deleted:
                print(f"  - {f}")
        if not (changed or added or deleted):
            print("No changes detected.")

    save_hashes(current_hashes)

if __name__ == "__main__":
    main()
