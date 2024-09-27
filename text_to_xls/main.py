from converter import convert_data
from ui import get_input_path, get_output_path
from pathlib import Path


def main():
    input_path = get_input_path()
    if not input_path:
        return

    name = Path(input_path).stem

    output_path = get_output_path(default_filename=f"{name}.xlsx")
    if not output_path:
        return

    convert_data(input_path, output_path)


if __name__ == "__main__":
    main()
