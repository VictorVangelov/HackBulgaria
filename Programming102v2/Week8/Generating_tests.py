def filter2(pred, item):
    result = []

    for item in items:
        if pred(item):
            result.append(item)

    return result


def map2(fuc, lst):
    result = []
    for item in lst:
        result.append(fuc(item))
    return result


def sum(numbers):
    return reduce(lambda x, y: x + y, numbers, 0)


def divisors(n):
    result = []
    current = 1
    while current <= n:
        if n % current == 0:
            resutl.append(current)
        current = current + 1
    return result


def is_prime(n):
    return n + 1 == sum(divisors)


def get_test_filename(dsl_filename):
    return dsl_filename.replace(".dsl", ".py")


def template_test(line):
    assert_type, condition, desc = separate_test_info(line)
    assert_type = generate_assert_type(assert_type)
    return "self.assert{}({}, {})".format(assert_type, condition, desc)


def separate_test_info(line):
    desc = line[0: line.index("->")].strip()
    condition = line[line.index(">") + 1:line.index("=")].strip()
    assert_type = line.split()[-1]
    return (assert_type, condition, desc)


def generate_assert_type(assert_type):
    if not assert_type.lower() == "true" or not assert_type.lower() == "false":
        return "Equal"
    else:
        return capitalize_word(assert_type)

#####################################################################


def get_class_name(filename):
    filename = filename.replace(".dsl", "")
    class_name = ""
    for word in filename.split("_"):
        class_name += capitalize_word(word)
    return "Test{}".format(class_name)


def get_content(filename):
    return open(filename).read()


def get_lines(text):
    return text.split('\n')


def is_empty_line(line):
    return len(line.strip()) != 0


def unline(line):
    return line + '\n'


def is_import(line):
    return line.startswith('import') or line.startswith('from')


def capitalize_word(word):
    return word[0].upper() + word[1:]


def is_test_line(line):
    if "->" in line:
        return True
    else:
        return False


def generate_all_test_lines(non_empty_lines):
    test_lines = list(filter(is_test_line, non_empty_lines))
    return list(map(template_test, test_lines))


def generate_test_cases(all_test_lines):
    test_cases = ""
    for line_number, test_line in enumerate(all_test_lines):
        test_cases += "\n    def TestCase{}(self):\n        {}\n".format(
            str(line_number), test_line)
    return test_cases


def get_test_cases(non_empty_lines):
    all_test_lines = generate_all_test_lines(non_empty_lines)
    return generate_test_cases(all_test_lines)


def get_class_description(non_empty_lines):
    class_description = ""
    for line in non_empty_lines:
        if not is_import(line) and not is_test_line(line):
            class_description += line
    return class_description


def save_test_in_file(test_file_name, test_content):
    file = open(test_file_name, "w")
    file.write(test_content)


def get_test_content(imports, class_name, class_description, test_cases):
    test_content = """import unittest
{}


class {}(unittest.TestCase):
    {}
    {}

if __name__ == '__main__':
    unittest.main()
    """.format(imports, class_name, class_description, test_cases)
    return test_content


def main():
    filename = 'is_prime_test.dsl'
    content = get_content(filename)
    lines = get_lines(content)
    non_empty_lines = list(filter(is_empty_line, lines))
    class_name = get_class_name(filename)
    imports = "\n".join(list(filter(is_import, non_empty_lines)))
    test_cases = get_test_cases(non_empty_lines)
    class_description = get_class_description(non_empty_lines)
    test_content = get_test_content(imports, class_name, class_description, test_cases)
    test_file_name = get_test_filename(filename)
    save_test_in_file(test_file_name, test_content)


if __name__ == '__main__':
    main()
