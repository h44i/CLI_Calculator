import subprocess
import sys

def test_calc():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2 + 2 * 2"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "6.0"

def test_error():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "1 / 0"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert result.stderr != ""