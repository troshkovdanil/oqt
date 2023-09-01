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


def test_bin_10111_to_dec():
    assert int("10111", 2) == 23

def test_bin_11001010_to_dec():
    assert int("11001010", 2) == 202

def test_dec_42_to_bin():
    assert str(bin(42)) == "0b101010"

def test_dec_495_to_bin():
    assert str(bin(495)) == "0b111101111"

def test_hex_3B7C_to_dec():
    assert int("3B7C", 16) == 15228

def test_hex_FF_to_bin():
    assert str(bin(int("FF", 16))) == "0b11111111"

def test_hex_FA_to_dec():
    assert int("FA", 16) == 250

def test_hex_10_to_dec():
    assert int("10", 16) == 16

def test_hex_E4_to_dec():
    assert int("E4", 16) == 228



from bitstring import BitArray


def test_bin_000_to_dec():
    assert BitArray(bin="000").int == 0

def test_bin_001_to_dec():
    assert BitArray(bin="001").int == 1

def test_bin_010_to_dec():
    assert BitArray(bin="010").int == 2

def test_bin_011_to_dec():
    assert BitArray(bin="011").int == 3

def test_bin_100_to_dec():
    assert BitArray(bin="100").int == -4

def test_bin_101_to_dec():
    assert BitArray(bin="101").int == -3

def test_bin_110_to_dec():
    assert BitArray(bin="110").int == -2

def test_bin_111_to_dec():
    assert BitArray(bin="111").int == -1


def test_bin_1010001_to_char():
    assert BitArray(bin="1010001").uint == ord('Q')
    
def test_bits_to_ASCII():
    bits_list = [1010001, 1110101, 1100001, 1101110, 1110100, 1110101, 1101101]
    chars_list = "Quantum"
    assert len(bits_list) == len(chars_list)
    for i in range(len(bits_list)):
        assert BitArray(bin=str(bits_list[i])).uint == ord(chars_list[i])


def gate_NOT(A):
    assert A == 0 or A == 1
    return 1 if A == 0 else 0

def gate_OR(A, B):
    assert A == 0 or A == 1
    assert B == 0 or B == 1
    truth_table = [
        [[0, 0], 0],
        [[0, 1], 1],
        [[1, 0], 1],
        [[1, 1], 1]
    ]
    assert len(truth_table) == 2*2
    for i in range(len(truth_table)):
        if truth_table[i][0][0] == A and truth_table[i][0][1] == B:
            return truth_table[i][1]
    assert 0

def gate_AND(A, B):
    assert A == 0 or A == 1
    assert B == 0 or B == 1
    truth_table = [
        [[0, 0], 0],
        [[0, 1], 0],
        [[1, 0], 0],
        [[1, 1], 1]
    ]
    assert len(truth_table) == 2*2
    for i in range(len(truth_table)):
        if truth_table[i][0][0] == A and truth_table[i][0][1] == B:
            return truth_table[i][1]
    assert 0

def gate_NEG_OR(A, B):
    return gate_OR(gate_NOT(A), gate_NOT(B))

def gate_NAND(A, B):
    return gate_NOT(gate_AND(A, B))

def test_NEG_OR():
    truth_table = [
        [[0, 0], 1],
        [[0, 1], 1],
        [[1, 0], 1],
        [[1, 1], 0]
    ]
    assert len(truth_table) == 2*2
    for i in range(len(truth_table)):
        assert gate_NEG_OR(truth_table[i][0][0], truth_table[i][0][1]) == truth_table[i][1]
        assert   gate_NAND(truth_table[i][0][0], truth_table[i][0][1]) == truth_table[i][1]

def gate_NEG_AND(A, B):
    return gate_AND(gate_NOT(A), gate_NOT(B))

def gate_NOR(A, B):
    return gate_NOT(gate_OR(A, B))

def test_NEG_AND():
    truth_table = [
        [[0, 0], 1],
        [[0, 1], 0],
        [[1, 0], 0],
        [[1, 1], 0]
    ]
    assert len(truth_table) == 2*2
    for i in range(len(truth_table)):
        assert gate_NEG_AND(truth_table[i][0][0], truth_table[i][0][1]) == truth_table[i][1]
        assert     gate_NOR(truth_table[i][0][0], truth_table[i][0][1]) == truth_table[i][1]
