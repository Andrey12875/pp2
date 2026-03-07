import re

text = "This string was created march 2026 to give examples on python regular expression." \
       " Contact: Wasd@gmail.com score=22 price=12.5 code=1234 (unique strings) [in brackets]" \
       " <img src   = link> ID_42 #tag C++ zip-050000 end."

print(re.search(r"march", text).group())
print(re.search(r"\w+@\w+\.\w+", text).group())
print(re.search(r"\d+\.\d+", text).group())
print(re.search(r"<img\s+src\s*=\s*\w+>", text).group())

print(re.findall(r"in", text))
print(re.findall(r"[aeiou]", text))
print(re.findall(r"\d", text))
print(re.findall(r"\d{4}", text))
print(re.findall(r"\w+@\w+\.\w+", text))
print(re.findall(r"\(.*?\)", text))
print(re.findall(r"\[.*?\]", text))
print(re.findall(r"#\w+", text))
print(re.findall(r"\b[A-Z]{2}_\d+\b", text))
print(re.findall(r"\bzip-\d{6}\b", text))
print(re.findall(r"C\+\+", text))

print(re.split(r"\s+", text))
print(re.split(r"\d+", text))
print(re.split(r"[<>\[\]\(\)]", text))
print(re.split(r"[@.=]", "Wasd@gmail.com score=22 price=12.5"))

print(re.sub(r"\s+", "_", text))
print(re.sub(r"\d", "X", text))
print(re.sub(r"\w+@\w+\.\w+", "email_here", text))
print(re.sub(r"<.*?>", "[TAG]", text))