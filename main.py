import json
from Encoder import encode
from Decoder import decode
import browser

document = browser.document
alert = browser.alert

vocab = json.loads(open("vocab.json", "r").read())

y = encode("Why are you like this", vocab)

def visualize(____):
    alert(encode(document["t"].value, vocab))
def reset(___):
    document["t"].value = ""

print(y)
print(decode(y, vocab))
btn = document["send"]
resetbtn = document["reset"]
btn.bind("click", visualize)
resetbtn.bind("click", reset)
