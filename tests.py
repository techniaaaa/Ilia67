import subprocess

# Valid inputs: four lines: sum, difference, product, integer quotient.
cases = [
    ("10 2", "12\n8\n20\n5"),
    ("-8 2", "-6\n-10\n-16\n-4"),
    ("7 2", "9\n5\n14\n3"),
    ("-7 2", "-5\n-9\n-14\n-3"),
    ("0 2", "2\n-2\n0\n0"),
]
for data, expected in cases:
    r = subprocess.run(["./app"], input=data, text=True,
                       capture_output=True, timeout=3)
    if r.returncode != 0 or r.stdout.strip() != expected:
        raise SystemExit(f"FAIL {data!r}: exit={r.returncode}, output={r.stdout!r}")
# Additional convention: zero divisor / invalid input => error, no numeric output.
for data in ["10 0", "hello"]:
    r = subprocess.run(["./app"], input=data, text=True,
                       capture_output=True, timeout=3)
    if r.returncode == 0 or r.stdout:
        raise SystemExit(f"FAIL invalid input {data!r}")
print(f"PASS: {len(cases) + 2} tests")
