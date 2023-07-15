# after reading the code. it's just a substitution cipher man :(
# so go to ->  https://planetcalc.com/8047/  holding a portion of study-guide to perform frequency analysis attack and retrieve the key (I took 300 lines)
# and voila I got the key

shuffled_keys = "XUNMRYDFWHGLSTIBJCAVOPEZQK".lower()
mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
flag_enc = "brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm"
flag = ""
for i in flag_enc:
    if i in shuffled_keys:
        flag += mapping[shuffled_keys.find(i)]
    else:
        flag += i

print(flag)
