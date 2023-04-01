import os
import time
import click
from pypdf import PdfMerger, PdfReader
from pypdf.errors import PdfReadError


@click.command()
@click.option(
    "--files",
    "-f",
    multiple=True,
    type=str,
    help="Insert path to pdf file to merge (use parameter multiple times, once per file path)",
)
@click.option(
    "--output_path",
    "-o",
    type=str,
    help="Path where new file will be created (without file name)",
    default="",
)
@click.option(
    "--output_name",
    "-n",
    type=str,
    help="Name of new file (without .pdf extesion)",
)
def merge_pdf(files: tuple = None, output_path: str = "", output_name: str = None):
    merger = PdfMerger()
    for file in files:
        try:
            PdfReader(file)
            merger.append(file)
        except PdfReadError:
            print(f"Invalid PDF file: {file}")
            return
    if not output_name:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        output_name = f"result_pdf_{timestr}"
    output_file = os.path.join(output_path, f"{output_name}.pdf")
    merger.write(output_file)
    merger.close()


if __name__ == "__main__":
    merge_pdf()
