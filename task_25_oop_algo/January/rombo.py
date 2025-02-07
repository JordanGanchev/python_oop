def get_rhombus(n):
    return [get_line(i, n) for i in range(n)] + \
            [get_line(i, n) for i in range(n - 2, -1, -1)]

def get_line(i, n, char='*'):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + (f'{char} ' * stars_count).strip()

def print_line(n):
    print(get_line(n, n))

def print_square(n):
    [print(get_line(n - 1, n - 1, '@')) for _ in range(n)]

def print_rhombus(n):
    [print(row) for row in get_rhombus(n)]

print_rhombus(3)
print_rhombus(4)
print_line(4)
print_square(5)


# def print_rhombus(n):
#     # for i in range(n):
#     #     print(get_line(i, n))
#     [print(get_line(i, n)) for i in range(n)]
#     # for i in range(n - 2, - 1, - 1):
#     #     print(get_line(i, n))
#     [print(get_line(i, n)) for i in range(n - 2, - 1, - 1)]

