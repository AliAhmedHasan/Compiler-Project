import re
TOKEN_INT = 'INT'
TOKEN_FLOAT = 'FLOAT'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_MULTIPLY = 'MULTIPLY'
TOKEN_DIVIDE = 'DIVIDE'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'
TOKEN_ASSIGN = 'ASSIGN'
TOKEN_SEMICOLON = 'SEMICOLON'


patterns = [
    (r'\d+', TOKEN_INT),                # Integer
    (r'\d+\.\d+', TOKEN_FLOAT),        # Float
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'\bwhile\b', 'WHILE'),
    (r'\b[a-zA-Z_]\w*\b', 'IDENTIFIER'),
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'\/', 'DIVIDE'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r';', 'SEMICOLON'),
    (r'=', TOKEN_ASSIGN),  # Assignment
(r'\s+', None),                      # Skip whitespace
]

# Sample code to be analyzed
source_code = """
#include <iostream>
using namespace std;

int main() {

  int i, n;
  bool is_prime = true;

  cout << "Enter a positive integer: ";
  cin >> n;

  // 0 and 1 are not prime numbers
  if (n == 0 || n == 1) {
    is_prime = false;
  }

  // loop to check if n is prime
  for (i = 2; i <= n/2; ++i) {
    if (n % i == 0) {
      is_prime = false;
      break;
    }
  }

  if (is_prime)
    cout << n << " is a prime number";
  else
    cout << n << " is not a prime number";

  return 0;
}
"""

# Perform lexical analysis
def tokenize(code):

    tokens = []
    for pattern, token_type in patterns:
        regex = re.compile(pattern)
        matches = regex.finditer(code)
        for match in matches:
            tokens.append((token_type, match.group()))
    return tokens

tokens = tokenize(source_code)

# Display the tokens
for token_type, token_value in tokens:
    print(f'{token_type}: {token_value}')
