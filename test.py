import math
import sys
from os import rename

import requests

print("This is a test")
r = requests.get(
    "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjh2rWO5o3oAhUtxosKHdW6AigQPAgH"
)
print(r.ok)
print(r.status_code)
a = "asdas"
print("asda")
print("aSADASD")
