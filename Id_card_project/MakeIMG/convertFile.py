# from PIL import Image
#
# image_1 = Image.open(r'user.png')
# im_1 = image_1.convert('RGB')
# im_1.save(r'user.pdf')



from fpdf import FPDF
# Create a class that inherits from FPDF
class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass
pdf = PDF()
pdf.set_auto_page_break(auto=True)
image_files = ["img1.png", "img2.png"]
x = 10
y = 10
w = 190
h = 270

for image_file in image_files:
    pdf.add_page()
    pdf.image(image_file, x=x, y=y, w=w, h=h)

pdf_filename = "output.pdf"
pdf.output(pdf_filename)
print(f"PDF generated as {pdf_filename}")

