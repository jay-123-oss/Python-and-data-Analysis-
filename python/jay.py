import re
import re

t = "Hello World"
p = r"Hello"

result = re.match(p, t)
if result:
    print("Match found:", result.group())
else:
    print("No match")


text = "I have 2 apples and 35 bananas"
pattern = r"\d+"

new_text = re.sub(pattern, "x", text)
print(new_text)  # I have X apples and X bananas


parts = re.split(pattern, text)
print(parts)  # ['apple', 'banana', 'cherry', 'orange']



matches = re.findall(pattern, text)
print(matches)  # ['123', '456']



result = re.search(pattern, text)
print(result.group())   # World


