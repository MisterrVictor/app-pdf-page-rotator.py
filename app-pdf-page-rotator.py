import easygui as gui
from PyPDF2 import PdfReader, PdfWriter

# Ask user to select a PDF file
open_title = "Select a PDF to rotate..."
file_type = ["*.pdf"]
input_path = gui.fileopenbox(title=open_title, filetypes=file_type)

# If nothing was returned by gui.fileopenbox(), the user either
# hit cancel or closed the window so we should exit the program.
if input_path is None:
    exit()

# Ask the user by how many degrees each page should be rotated.
# If the user doesn't select anything, keep displaying the
# buttonbox() element until they do.
choices = ["90", "180", "270"]
message = "Rotate the PDF clockwise by how many degrees?"
degrees = None
while degrees is None:
    degrees = gui.buttonbox(message, "Choose rotation...", choices)

# Convert the chosen number of degrees to an integer
degrees = int(degrees)

# Ask the user what they would like to call the new PDF and where
# it should be saved.
save_title = "Save the rotated PDF as..."
output_path = gui.filesavebox(title=save_title, filetypes=file_type)

# If the user tries to overwrite the file they originally selected
# for rotation, warn them and ask them to select a new file path.
# Keep doing this until a valid file path is chosen.
warn_title = "Warning!"
warn_message = "Cannot overwrite original file!"
while input_path == output_path:
    gui.msgbox(warn_message, title=warn_title)
    output_path = gui.filesavebox(title=save_title, filetypes=file_type)

# If nothing was returned by gui.fileopenbox(), the user either hit
# cancel or closed the window so we should exit the program.
if output_path is None:
    exit()

# Открытие входного файла
input_file = PdfReader(open(input_path, "rb"))  # Здесь используется PdfReader вместо PdfFileReader
output_pdf = PdfWriter()

for page in input_file.pages:
    page = page.rotate(degrees)
    output_pdf.add_page(page)

# Запись выходного файла
with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)
