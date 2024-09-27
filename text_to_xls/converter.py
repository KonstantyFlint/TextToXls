import decimal
from xlsxwriter import Workbook

from style import INDEX_STYLE, COORD_STYLE, INDEX_WIDTH, COORD_WIDTH


def convert_data(text_file_path: str, xls_file_path: str):

    workbook = Workbook(xls_file_path)
    index_style = workbook.add_format(properties=INDEX_STYLE)
    coord_style = workbook.add_format(properties=COORD_STYLE)

    text_file = open(text_file_path)

    with workbook, text_file:
        worksheet = workbook.add_worksheet()

        coord_dimensions = get_coord_dimensions(text_file)
        set_widths(worksheet, coord_dimensions)

        for row_number, line in enumerate(text_file.readlines()):
            row_components = line.split(" ")
            point_id = row_components[0]
            point_coords = tuple(decimal.Decimal(coord) for coord in row_components[1:])
            worksheet.write(row_number, 0, point_id, index_style)
            for column_number, coord in enumerate(point_coords):
                worksheet.write(row_number, column_number + 1, coord, coord_style)


def get_coord_dimensions(text_file):
    initial_position = text_file.tell()
    text_file.seek(0)
    first_line = text_file.readline()
    coord_dimensions = len(first_line.split(" ")) - 1
    text_file.seek(initial_position)
    return coord_dimensions


def set_widths(worksheet, coord_dimensions):
    worksheet.set_column("A:A", INDEX_WIDTH)
    if coord_dimensions == 2:
        worksheet.set_column("B:C", COORD_WIDTH)
    elif coord_dimensions == 3:
        worksheet.set_column("B:D", COORD_WIDTH)
    else:
        raise ValueError("Unexpected dimensions for a point.")
