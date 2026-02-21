letter = '''Dear <|name|>,
 You are selected!
Congratulations!
              <|date|>'''

print(letter.replace("<|name|>", "Singh").replace("<|date|>", "22th January 2026"))