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


# 1.5 a
def test_bin_10111_to_dec():
    assert int("10111", 2) == 23

# 1.5 b
def test_bin_11001010_to_dec():
    assert int("11001010", 2) == 202

# 1.6 a
def test_dec_42_to_bin():
    assert str(bin(42)) == "0b101010"

# 1.6 b
def test_dec_495_to_bin():
    assert str(bin(495)) == "0b111101111"

# 1.7 a
def test_hex_3B7C_to_dec():
    assert int("3B7C", 16) == 15228

# 1.7 b
def test_hex_FF_to_bin():
    assert str(bin(int("FF", 16))) == "0b11111111"

# 1.7 c
def test_hex_FA_to_dec():
    assert int("FA", 16) == 250

# 1.7 c
def test_hex_10_to_dec():
    assert int("10", 16) == 16

# 1.7 c
def test_hex_E4_to_dec():
    assert int("E4", 16) == 228



from bitstring import BitArray


# 1.8
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

# 1.8
def test_bin_111_to_dec():
    assert BitArray(bin="111").int == -1


# 1.10
def test_bin_1010001_to_char():
    assert BitArray(bin="1010001").uint == ord('Q')
    
# 1.10
def test_bits_to_ASCII():
    bits_list = [1010001, 1110101, 1100001, 1101110, 1110100, 1110101, 1101101]
    chars_list = "Quantum"
    assert len(bits_list) == len(chars_list)
    for i in range(len(bits_list)):
        assert BitArray(bin=str(bits_list[i])).uint == ord(chars_list[i])


# 1.11
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
    assert len(truth_table) == 2**2
    for i in range(len(truth_table)):
        if truth_table[i][0][0] == A and truth_table[i][0][1] == B:
            return truth_table[i][1]
    assert 0

def gate_XOR(A, B):
    assert A == 0 or A == 1
    assert B == 0 or B == 1
    truth_table = [
        [[0, 0], 0],
        [[0, 1], 1],
        [[1, 0], 1],
        [[1, 1], 0]
    ]
    assert len(truth_table) == 2**2
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
    assert len(truth_table) == 2**2
    for i in range(len(truth_table)):
        if truth_table[i][0][0] == A and truth_table[i][0][1] == B:
            return truth_table[i][1]
    assert 0

def gate_NEG_OR(A, B):
    return gate_OR(gate_NOT(A), gate_NOT(B))

def gate_NAND(A, B):
    return gate_NOT(gate_AND(A, B))

# 1.11
def test_NEG_OR():
    truth_table = [
        [[0, 0], 1],
        [[0, 1], 1],
        [[1, 0], 1],
        [[1, 1], 0]
    ]
    assert len(truth_table) == 2**2
    for i in range(len(truth_table)):
        A = truth_table[i][0][0]
        B = truth_table[i][0][1]
        r = truth_table[i][1]
        assert gate_NEG_OR(A, B) == r
        assert gate_NAND(A, B) == r

# 1.12
def gate_NEG_AND(A, B):
    return gate_AND(gate_NOT(A), gate_NOT(B))

def gate_NOR(A, B):
    return gate_NOT(gate_OR(A, B))

# 1.12
def test_NEG_AND():
    truth_table = [
        [[0, 0], 1],
        [[0, 1], 0],
        [[1, 0], 0],
        [[1, 1], 0]
    ]
    assert len(truth_table) == 2**2
    for i in range(len(truth_table)):
        A = truth_table[i][0][0]
        B = truth_table[i][0][1]
        r = truth_table[i][1]
        assert gate_NEG_AND(A, B) == r
        assert gate_NOR(A, B) == r

# 1.18
def gate_XOR3(A, B, C):
    return gate_XOR(gate_XOR(A, B), C)

# 1.18
def test_XOR3():
    truth_table = [
        [[0, 0, 0], 0],
        [[0, 0, 1], 1],
        [[0, 1, 0], 1],
        [[0, 1, 1], 0],
        [[1, 0, 0], 1],
        [[1, 0, 1], 0],
        [[1, 1, 0], 0],
        [[1, 1, 1], 1]
    ]
    assert len(truth_table) == 2**3
    for i in range(len(truth_table)):
        A = truth_table[i][0][0]
        B = truth_table[i][0][1]
        C = truth_table[i][0][2]
        r = truth_table[i][1]
        assert gate_XOR3(A, B, C) == r
        assert r == 0 if (A + B + C) % 2 == 0 else r == 1

# 1.19
def gate_EX_1_19(A, B, C):
    return gate_NOT(gate_AND(gate_OR(A, B), gate_NAND(C, C)))

# 1.19
def test_EX_1_19():
    truth_table = [
        [[0, 0, 0], 1],
        [[0, 0, 1], 1],
        [[0, 1, 0], 0],
        [[0, 1, 1], 1],
        [[1, 0, 0], 0],
        [[1, 0, 1], 1],
        [[1, 1, 0], 0],
        [[1, 1, 1], 1]
    ]
    assert len(truth_table) == 2**3
    for i in range(len(truth_table)):
        A = truth_table[i][0][0]
        B = truth_table[i][0][1]
        C = truth_table[i][0][2]
        r = truth_table[i][1]
        assert gate_EX_1_19(A, B, C) == r

# 1.27
def gate_AND_by_NOT_and_OR(A, B):
    return gate_NOT(gate_OR(gate_NOT(A), gate_NOT(B)))

# 1.27
def test_AND_by_NOT_and_OR():
    input_table = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    assert len(input_table) == 2**2
    for i in range(len(input_table)):
        A = input_table[i][0]
        B = input_table[i][1]
        assert gate_AND_by_NOT_and_OR(A, B) == gate_AND(A, B)

# 1.28 a
def gate_NOT_by_NOR(A):
    return gate_NOR(A, A)

# 1.28 a
def test_NOT_by_NOR():
    input_table = [
        0,
        1
    ]
    assert len(input_table) == 2**1
    for i in range(len(input_table)):
        A = input_table[0]
        B = input_table[1]
        assert gate_NOT_by_NOR(A) == gate_NOT(A)

# 1.28 b
def gate_OR_by_NOR(A, B):
    t = gate_NOR(A, B)
    return gate_NOR(t, t)

# 1.28 b
def test_OR_by_NOR():
    input_table = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    assert len(input_table) == 2**2
    for i in range(len(input_table)):
        A = input_table[i][0]
        B = input_table[i][1]
        assert gate_OR_by_NOR(A, B) == gate_OR(A, B)


def gate_HalfAdd(A, B):
    S = gate_XOR(A, B)
    C = gate_AND(A, B)
    return [S, C]

def test_HalfAdd():
    io_table = [
        [[0, 0], [0, 0]],
        [[0, 1], [1, 0]],
        [[1, 0], [1, 0]],
        [[1, 1], [0, 1]]
    ]
    assert len(io_table) == 2**2
    for i in range(len(io_table)):
        A = io_table[i][0][0]
        B = io_table[i][0][1]
        S = io_table[i][1][0]
        C = io_table[i][1][1]
        [rS, rC] = gate_HalfAdd(A, B)
        assert rS == S
        assert rC == C

def gate_FullAdd(A, B, C):
    [rS, rCout] = gate_HalfAdd(A, B)
    [S, rCout2] = gate_HalfAdd(C, rS)
    Cout = gate_OR(rCout2, rCout)
    return [S, Cout]

def test_FullAdd():
    io_table = [
        [[0, 0, 0], [0, 0]],
        [[0, 0, 1], [1, 0]],
        [[0, 1, 0], [1, 0]],
        [[0, 1, 1], [0, 1]],
        [[1, 0, 0], [1, 0]],
        [[1, 0, 1], [0, 1]],
        [[1, 1, 0], [0, 1]],
        [[1, 1, 1], [1, 1]]
    ]
    assert len(io_table) == 2**3
    for i in range(len(io_table)):
        A = io_table[i][0][0]
        B = io_table[i][0][1]
        C = io_table[i][0][2]
        S = io_table[i][1][0]
        Cout = io_table[i][1][1]
        [rS, rCout] = gate_FullAdd(A, B, C)
        assert rS == S
        assert rCout == Cout
