import PyPDF2
import fitz
from pdf2image import convert_from_path
from PIL import Image
import os
def merge_pdfs(input_pdfs, output_pdf):
    merger = PyPDF2.PdfMerger()
    for pdf in input_pdfs:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()

def split_pdf(input_pdf, output_directory):
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(reader.getNumPages()):
            writer = PyPDF2.PdfWriter()
            writer.addPage(reader.getPage(page_num))
            output_path = f"{output_directory}/page_{page_num + 1}.pdf"
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

def crop_pdf(input_pdf, output_pdf, left, top, right, bottom):
    pdf_document = fitz.open(input_pdf)
    pdf_page = pdf_document[0]
    pdf_page.set_cropbox((left, top, right, bottom))
    pdf_page.save(output_pdf)
    pdf_document.close()

def rotate_pdf(input_pdf, output_pdf, angle):
    pdf_document = fitz.open(input_pdf)
    pdf_page = pdf_document[0]
    pdf_page.setRotation(angle)
    pdf_page.save(output_pdf)
    pdf_document.close()

def convert_pdf_to_jpeg(input_pdf, output_directory):
    images = convert_from_path(input_pdf)
    for i, image in enumerate(images):
        image.save(f"{output_directory}/page_{i + 1}.jpeg", 'JPEG')

def convert_jpeg_to_pdf(input_directory, output_pdf):
    image_paths = [f"{input_directory}/{filename}" for filename in sorted(os.listdir(input_directory))]
    image_objects = [Image.open(image_path) for image_path in image_paths]
    image_objects[0].save(output_pdf, save_all=True, append_images=image_objects[1:])

if __name__ == "__main__":
    merge_pdfs(["D:\\Naga\\python_tasks\\day_6\\Freshres plan.pdf", "D:\\Naga\\python_tasks\\day_6\\LETTER.pdf"], "merged.pdf")
    split_pdf("input.pdf", "output_pages")
    crop_pdf("input.pdf", "cropped.pdf", 50, 50, 400, 400)
    rotate_pdf("input.pdf", "rotated.pdf", 90)
    convert_pdf_to_jpeg("input.pdf", "output_jpeg")
    convert_jpeg_to_pdf("output_jpeg", "converted.pdf")
