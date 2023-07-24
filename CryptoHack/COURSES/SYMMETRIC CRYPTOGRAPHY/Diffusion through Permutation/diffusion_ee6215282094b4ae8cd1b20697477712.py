# Substitution on its own creates non-linearity, however it doesn't distribute it
# over the entire state. Without diffusion, the same byte in the same position
# would get the same transformations applied to it each round. This would allow
# cryptanalysts to attack each byte position in the state matrix separately. We need
# to alternate substitutions by scrambling the state (in an invertible way) so that
# substitutions applied on one byte influence all other bytes in the state.
# Each input into the next S-box then becomes a function of multiple bytes, meaning
# that with every round the algebraic complexity of the system increases enormously.

# ShiftRows is the most simple transformation in AES. It keeps the first row of the
# state matrix the same. The second row is shifted over one column to the left,
# wrapping around. The third row is shifted two columns, the fourth row by three.
# Wikipedia puts it nicely: "the importance of this step is to avoid the columns being
# encrypted independently, in which case AES degenerates into four independent block
# ciphers."


def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    s[1][1], s[2][1], s[3][1], s[0][1] = s[0][1], s[1][1], s[2][1], s[3][1]
    s[2][2], s[3][2], s[0][2], s[1][2] = s[0][2], s[1][2], s[2][2], s[3][2]
    s[3][3], s[0][3], s[1][3], s[2][3] = s[0][3], s[1][3], s[2][3], s[3][3]
    return s

# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)
    return s


state = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    # flatten the matrix to a list of a single dimension and then convert it to bytes
    return bytes(sum(matrix, [])).decode("utf-8")



print(matrix2bytes(inv_shift_rows(inv_mix_columns(state))))

