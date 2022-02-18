def nested_parentheses(incoming):
  parentheses = ['()']
  while any(x in incoming for x in parentheses):
    for br in parentheses:
      incoming = incoming.replace(br, '')
  return not incoming


string = input()
print(string, "=>", "True"
if nested_parentheses(string) else "False")
