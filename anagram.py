def anagram():
  word_one = input("‣ First word: ").lower()
  word_two = input("‣ Second word: ").lower()

  if word_one == word_two:
    print("⁉️ They're the same word, try again.")
    return

  is_anagram = sorted(word_one) == sorted(word_two)

  if is_anagram:
    print("✅ Both words are anagrams.")
  else:
    print("❌ Both words are not anagrams.")


anagram()