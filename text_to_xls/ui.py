from tkinter import filedialog


def get_input_path():
    return filedialog.askopenfilename(
        title="Select Input File",
        filetypes=(("Text files", "*.txt"),)
    )


def get_output_path(default_filename: str):
    return filedialog.asksaveasfilename(
        title="Save Output File",
        initialfile=default_filename,
        defaultextension=".xlsx",
        filetypes=(("XLS Files", "*.xlsx"),)
    )
