from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

f = FactorDB(n)
f.connect()
p = f.get_factor_list()[0]
q = f.get_factor_list()[1]

phi = (p-1) * (q-1)

d = pow(e, -1, phi)

pt = pow(ct, d , n)
print(long_to_bytes(pt))
