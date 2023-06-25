import click
from ocr_converter import OCRConverter


@click.command()
@click.argument("folder_path")
def main(folder_path: str):
    ocr_converter = OCRConverter(folder_path)
    ocr_converter.convert_images()


if __name__ == "__main__":
    main()
