# File Integrity Monitor (FIM)

A Python tool for monitoring file changes in a directory using SHA-256 hashing. This project helps detect unauthorized modifications, additions, or deletions of files.

---

## Description

This File Integrity Monitor (FIM) scans a specified directory, calculates cryptographic hashes for each file, and stores them. On subsequent runs, it compares the current hashes to the stored ones and reports any changes, additions, or deletions. This helps identify tampering, malware, or accidental changes to critical files.

---

## Features

- Monitors a directory for file changes (modifications, additions, deletions)
- Uses secure SHA-256 hashing for integrity verification
- Stores file hashes in a JSON file for future comparison
- Prints alerts to the console when changes are detected
- Simple, cross-platform, and easy to use

---

## Installation

1. **Clone the repository or download the script:**
git clone https://github.com/yourusername/file_integrity_monitor.git
cd file_integrity_monitor


2. **Create the directory to monitor:**
- By default, the script monitors `./monitor_folder`. You can change this by editing the `MONITORED_DIR` variable in the script.

3. **(Optional) Add some files to the monitored folder for testing.**

---

## Usage

Run the script with Python 3:

python file_integrity_monitor.py


- **First run:** The script creates a baseline of file hashes.
- **Subsequent runs:** The script reports any files that have been modified, added, or deleted since the last run.

---

## Security Concepts Demonstrated

- **File Integrity Monitoring:** Detects unauthorized or accidental changes to files.
- **Cryptographic Hashing:** Uses SHA-256 to verify file integrity.
- **Change Detection:** Reports modifications, additions, and deletions.
- **Incident Response:** Provides alerts that can be used for further investigation.

---

## Improvement Ideas

- Add email or desktop notifications for real-time alerts.
- Monitor multiple directories.
- Integrate with a SIEM or logging platform.
- Add a GUI or web dashboard for easier monitoring.
- Schedule regular scans with cron (Linux) or Task Scheduler (Windows).

---

## What I Learned

- How to use Python for file operations and cryptographic hashing.
- The importance of monitoring critical files for security.
- Basics of change detection and alerting in cybersecurity.

---

## References

- [NIST Special Publication 800-53: Security and Privacy Controls for Information Systems](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
- [File Integrity Monitoring (Wikipedia)](https://en.wikipedia.org/wiki/File_integrity_monitoring)

---

**For educational use only. Always monitor files and systems with proper authorization.**
