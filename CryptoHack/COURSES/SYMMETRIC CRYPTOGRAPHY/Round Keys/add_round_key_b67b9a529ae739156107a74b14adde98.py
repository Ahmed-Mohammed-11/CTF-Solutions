
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    # flatten the matrix to a list of a single dimension and then convert it to bytes
    return bytes(sum(matrix, [])).decode("utf-8")

def add_round_key(s, k):
    result = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = s[i][j] ^ k[i][j]
    return result



print(matrix2bytes(add_round_key(state, round_key)))


