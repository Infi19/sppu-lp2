# AI Algorithms - Dependencies

This folder contains various AI and algorithm implementations. Here are the dependencies required for each file:

## General Requirements
- Python 3.6+

## File-Specific Dependencies

### astar.py
- Standard Python libraries only (no external dependencies)

### chatbot.py
- ChatterBot library
- SQLite (used by ChatterBot's SQLStorageAdapter)

### dfsbfs.py
- Standard Python libraries only
  - collections (deque) - included in Python standard library

### nqueen.py
- Standard Python libraries only (no external dependencies)

### greedyselection.py
- Standard Python libraries only (no external dependencies)

## Installation Instructions

To install the required dependencies, run:

```bash
pip install chatterbot==1.0.8
```

Note: ChatterBot may have additional dependencies that will be automatically installed. The latest version might be different, so adjust as needed.

## Compatibility Notes

- The chatbot.py file uses ChatterBot which has specific compatibility with Python versions. ChatterBot 1.0.8 works best with Python 3.6-3.8.
- All other scripts should work with any Python 3.6+ version. 