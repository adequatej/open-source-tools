# Script fo
import sys

def setOutput(name, value):
    print(f"::set-output name={name}::{value}")

def fail(message):
    print(f"::error::{message}")
    sys.exit(1)
