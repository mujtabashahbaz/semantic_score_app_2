import pypandoc
import os
from docx import Document

def convert_rtf_to_docx(rtf_path, docx_path=None):
    """
    Convert an RTF file to DOCX format.
    
    Args:
        rtf_path (str): Path to the input RTF file
        docx_path (str, optional): Path to save the output DOCX file. 
                                 If None, uses same directory as input with .docx extension.
    
    Returns:
        str: Path to the created DOCX file
    """
    if docx_path is None:
        docx_path = os.path.splitext(rtf_path)[0] + '.docx'
    
    # Convert RTF to DOCX using pandoc
    output = pypandoc.convert_file(
        rtf_path,
        'docx',
        outputfile=docx_path,
        format='rtf'
    )
    
    return docx_path

# Example usage
if __name__ == "__main__":
    input_file = "hindi_content.rtf"  # Replace with your RTF file path
    output_file = "output.docx"  # Replace with desired output path
    
    try:
        converted_file = convert_rtf_to_docx(input_file, output_file)
        print(f"Successfully converted {input_file} to {converted_file}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")