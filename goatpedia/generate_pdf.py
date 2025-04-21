import pdfkit
import markdown2

input_file = "./entries/generated_entries.md"
output_file = "./entries/GOATPEDIA.pdf"

def convert_markdown_to_pdf():
    with open(input_file, "r", encoding="utf-8") as f:
        html = markdown2.markdown(f.read())

    # Convert to PDF
    pdfkit.from_string(html, output_file)
    print(f"PDF generated at {output_file}")

if __name__ == "__main__":
    convert_markdown_to_pdf()