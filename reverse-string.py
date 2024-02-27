# Create a function to reverse strings.


def reverse(text):
  length = len(text) + 1
  reverse_text = ''

  for idx in range(1, length):
    reverse_text += text[-idx]

  print(reverse_text)


reverse('Hola mundo')
reverse('Lorem ipsum')
reverse('Alucard')