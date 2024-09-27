import random


def generate_test_file(number_of_lines: int):
    with open("test.txt", "w") as file:
        for i in range(1, number_of_lines + 1):
            x, y, z = (random.uniform(0, 1_000_000) for _ in range(3))
            file.write(
                f"{i} {x} {y} {z}\n"
            )


if __name__ == "__main__":
    generate_test_file(number_of_lines=1000)
