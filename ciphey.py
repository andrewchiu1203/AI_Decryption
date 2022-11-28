import os
import subprocess

os.environ["PYTHONUTF8"] = "1"
text = input("Please give a text to decrypt: \n")
# text = "aGVsbG8gbXkgbmFtZSBpcyBiZWU="
# text = "Aopz pz Hukyld zwlhrpun. P sprl abyaslz."

try:
    proc = subprocess.Popen("ciphey -t \"" + text + "\" -q", stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = str(out)
    out = out[2:len(out)-5]
    print("\nThe encryption is done\n")
except:
    print("Something goes wrong during decryption")

print("The most possible original text: \n" + out + "\n")