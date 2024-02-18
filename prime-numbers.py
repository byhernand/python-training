# Print the prime numbers from 0 to 100.

prime_numbers = [2,3,5,7]


def is_prime(x):
  if x == 1: return False # 1 is not a prime number

  for prime_num in prime_numbers:
    if x % prime_num == 0:
      return False

  return True


for number in range(1, 101):
  if is_prime(number):
    print(number)