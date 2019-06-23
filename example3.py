from automatabpp import *


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    import binascii
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def dynamically_create_function(name):
    def created(**_):
        print(created.__name__, end="")
    created.__name__ = name
    return EXECUTION.state(created)


BEHAVIOUR.load_behaviour_from_graph("base64/encode.graphml", "Base64 encode machine")

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/":
    dynamically_create_function(char)

# ...............................................................................
# ---------- DEFINITIONS COMPLETE - RUNNING THE PROGRAM -------------------------
# ...............................................................................
OPERATION.start()

example = "Man is distinguished, not only by his reason, but by this singular passion from other animals, " \
        "which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable " \
        "generation of knowledge, exceeds the short vehemence of any carnal pleasure."

for i, char in enumerate(text_to_bits(example)):
    OPERATION.run(char)
    if i > 0 and i % (8*57) == 0:
        print()
