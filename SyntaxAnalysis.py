import re
# Grammar rules
# expression   -> term ( ( '+' | '-' ) term )*
# term         -> factor ( ( '' | '/' ) factor )
# factor       -> '(' expression ')' | NUMBER

def parse_expression(expression):
    tokens = re.findall(r'[-+*/()]|\d+', expression)
    idx = 0

    def parse_term():
        nonlocal idx
        left = parse_factor()

        while idx < len(tokens) and tokens[idx] in ('*', '/'):
            operator = tokens[idx]
            idx += 1
            right = parse_factor()

            if operator == '*':
                left *= right
            else:
                left /= right

        return left

    def parse_expression():
        nonlocal idx
        left = parse_term()

        while idx < len(tokens) and tokens[idx] in ('+', '-'):
            operator = tokens[idx]
            idx += 1
            right = parse_term()

            if operator == '+':
                left += right
            else:
                left -= right

        return left

    def parse_factor():
        nonlocal idx
        token = tokens[idx]
        idx += 1

        if token == '(':
            result = parse_expression()
            idx += 1  # Consume the closing parenthesis
            return result
        else:
            return int(token)

    return parse_expression()


# Example usage
expression = "2 * (3 + 4) - 5 / 2"
result = parse_expression(expression)
print(f"Result:{result}")
