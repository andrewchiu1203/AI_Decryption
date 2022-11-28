from HE.HE import *

# Scheme's parameters
safe = False
# polynomial modulus degree
n = 2**4
# ciphertext modulus
q = 2**15
# plaintext modulus
t = 2**8
# polynomial modulus
poly_mod = np.array([1] + [0] * (n - 1) + [1])
# Keygen
pk, sk = keygen(n, q, poly_mod)

pt1 = input("Please enter a number for pt1 that will be encrypted: ")
pt2 = input("Please enter a number for pt2 that will be encrypted: ")
cst1 = input("Please enter a number for addition: ")
cst2 = input("Please enter a number for multiplication: ")

# Check if inputs are integer
if pt1.isdigit() and pt2.isdigit() and cst1.isdigit() and cst2.isdigit():
    safe = True
    pt1 = int(pt1)
    pt2 = int(pt2)
    cst1 = int(cst1)
    cst2 = int(cst2)

    # Encryption
    ct1 = encrypt(pk, n, q, t, poly_mod, pt1)
    ct2 = encrypt(pk, n, q, t, poly_mod, pt2)

    print("[+] Ciphertext({}):".format(pt1))
    print("")
    print("\t ct1_0:", ct1[0])
    print("\t ct1_1:", ct1[1])
    print("")
    print("[+] Ciphertext({}):".format(pt2))
    print("")
    print("\t ct1_0:", ct2[0])
    print("\t ct1_1:", ct2[1])
    print("")

    # Evaluation
    ct3 = add_plain(ct1, cst1, q, t, poly_mod)
    ct4 = mul_plain(ct2, cst2, q, t, poly_mod)

    # Decryption
    decrypted_ct3 = decrypt(sk, n, q, t, poly_mod, ct3)
    decrypted_ct4 = decrypt(sk, n, q, t, poly_mod, ct4)

    print("[+] Decrypted ct3(ct1 + {}): {}".format(cst1, decrypted_ct3))
    print("[+] Decrypted ct4(ct2 * {}): {}".format(cst2, decrypted_ct4))
else:
    print("One of the number you entered isn't an integer")