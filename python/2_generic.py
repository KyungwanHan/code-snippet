# sample1
def are_equal(a, b):
  return a == b

print(are_equal(10, 10.0))

# sample2
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal2(a: T, b: U) -> bool:
  return a == b

print(are_equal2(10, 10.0))