class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKGREEN}Hi Python!{bcolors.ENDC}")



import pytest


def test_dec_10111():
    assert int("10111", 2) == 23

def test_dec_11001010():
    assert int("11001010", 2) == 202

def test_bin_42():
    assert str(bin(42)) == "0b101010"

def test_bin_495():
    assert str(bin(495)) == "0b111101111"
