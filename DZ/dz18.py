text = 'I am learning Python. hello, WORLD!'
start_pos = text.find('h')
end_pos = text.rfind('h')
substring = text[start_pos + 1:end_pos]
reversed_substring = ''.join(reversed(substring))
text = text.replace(substring, reversed_substring)
print(text)
