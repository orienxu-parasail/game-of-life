#!/usr/bin/env python3
"""Prepare the local Python environment without running the exercise tests."""

import sys

if sys.version_info < (3, 9):
    print("SETUP FAILED: Python 3.9 or newer is required.", file=sys.stderr)
    sys.exit(2)

import argparse
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
ENV = ROOT / ".venv"
ENV_PYTHON = ENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
EDITOR_SETTINGS = ROOT / ".vscode" / "settings.json"
# Turns off AI inline completions (Copilot, Cursor Tab, ghost text) while this
# folder is open in VS Code or Cursor. Ordinary IntelliSense (identifiers,
# method names, parameter hints) stays on. Other folders are not affected.
NO_SUGGESTIONS = {
    "editor.inlineSuggest.enabled": False,
    "github.copilot.enable": {"*": False},
    "github.copilot.inlineSuggest.enable": False,
    "github.copilot.nextEditSuggestions.enabled": False,
    "cursor.cpp.disabledLanguages": ["python", "markdown", "plaintext", "json", "shellscript"],
}
CHECK = (
    "import sys; "
    "assert sys.version_info >= (3, 9), 'Python 3.9+ required'; "
    "import argparse, dataclasses, json, pathlib, typing, unittest; "
    "sys.path.insert(0, sys.argv[1]); import infection; "
    "print('Python ' + sys.version.split()[0] + ': required libraries verified')"
)


def disable_editor_suggestions():
    """Write (or update) .vscode/settings.json so the editor offers no AI completions."""
    settings = {}
    if EDITOR_SETTINGS.is_file():
        try:
            settings = json.loads(EDITOR_SETTINGS.read_text(encoding="utf-8"))
        except ValueError:
            print("Could not parse existing .vscode/settings.json; leaving it alone. "
                  "Turn off editor suggestions by hand.", flush=True)
            return
    if all(settings.get(key) == value for key, value in NO_SUGGESTIONS.items()):
        print("AI inline completions are already off for this folder.", flush=True)
        return
    settings.update(NO_SUGGESTIONS)
    EDITOR_SETTINGS.parent.mkdir(exist_ok=True)
    EDITOR_SETTINGS.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
    print("Wrote .vscode/settings.json: AI inline completions are off for this folder.",
          flush=True)


def fail(message):
    print("\nSETUP FAILED: " + message, file=sys.stderr)
    return 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print("[1/4] Checking Python: " + sys.version.split()[0], flush=True)
    print("[2/4] Preparing required libraries...", flush=True)
    print("This exercise uses only the Python standard library. No downloads are needed.",
          flush=True)

    if ENV.exists() or ENV.is_symlink():
        print("Reusing existing .venv (your exercise files are preserved).", flush=True)
        if not (ENV / "pyvenv.cfg").is_file() or not ENV_PYTHON.is_file():
            return fail("Existing .venv is incomplete or incompatible with this computer. "
                        "Rename .venv to keep it, then rerun setup. No files were replaced.")
    else:
        try:
            import venv
            # No third-party packages: pip and ensurepip are unnecessary.
            venv.EnvBuilder(with_pip=False).create(str(ENV))
        except ImportError:
            return fail("This Python installation is missing venv. Install the venv "
                        "component for this interpreter (often python3-venv on Linux), "
                        "or use a complete Python installation, then rerun setup.")
        except (OSError, subprocess.SubprocessError) as exc:
            return fail("Could not create .venv: %s. Check folder permissions and free "
                        "disk space. If .venv was partially created, rename it before "
                        "retrying. You can also extract the exercise to a writable folder."
                        % exc)

    print("[3/4] Verifying required libraries in .venv...", flush=True)
    try:
        checked = subprocess.run([str(ENV_PYTHON), "-I", "-c", CHECK, str(ROOT)],
                                 cwd=str(ROOT), capture_output=True, text=True)
    except OSError as exc:
        return fail("Cannot start .venv Python: %s. Rename .venv, then rerun setup "
                    "using a working Python 3.9+ installation." % exc)
    if checked.returncode:
        print(checked.stderr.strip(), file=sys.stderr)
        return fail("Required library or project import check failed. Standard-library "
                    "modules come with Python; they are not installed using pip. "
                    "For a missing Python module, repair/reinstall Python, rename .venv, "
                    "and rerun setup. If the error names an exercise file, correct that "
                    "file and retry. Setup has not changed your solution.")
    print(checked.stdout.strip())
    print("[4/4] Turning off AI inline completions for this folder...", flush=True)
    disable_editor_suggestions()
    print("\nSETUP SUCCESS — all required libraries are available.")
    print("Setup did not run the exercise tests.")
    print("Next, from the exercise folder (%s):" % ROOT)
    print(r"  .\.venv\Scripts\python.exe -m unittest tests.test_part1 -v" if os.name == "nt"
          else "  .venv/bin/python -m unittest tests.test_part1 -v")
    return 0


if __name__ == "__main__":
    sys.exit(main())
