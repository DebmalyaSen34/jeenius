import fitz  # PyMuPDF
import pdfplumber
from typing import List, Dict
import re

class PDFExtractor:
    """Extract text and equations from PDF for vector database storage."""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        
    def extract_with_structure(self) -> List[Dict[str, str]]:
        """Extract text with preserved structure and equations."""
        chunks = []
        
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                # Extract text with layout preserved
                text = page.extract_text(layout=True)
                
                if text:
                    # Split into meaningful chunks (paragraphs)
                    paragraphs = self._split_into_paragraphs(text)
                    
                    for para in paragraphs:
                        chunks.append({
                            'page': page_num,
                            'content': para.strip(),
                            'type': 'text'
                        })
        
        return chunks
    
    def extract_with_pymupdf(self) -> List[Dict[str, str]]:
        """Extract using PyMuPDF for better equation handling."""
        chunks = []
        doc = fitz.open(self.pdf_path)
        
        for page_num, page in enumerate(doc, 1):
            # Extract text blocks
            blocks = page.get_text("blocks")
            
            for block in blocks:
                text = block[4].strip()
                
                if text:
                    # Detect potential equations (heuristic)
                    is_equation = self._is_likely_equation(text)
                    
                    chunks.append({
                        'page': page_num,
                        'content': text,
                        'type': 'equation' if is_equation else 'text',
                        'bbox': block[:4]  # Bounding box for context
                    })
        
        doc.close()
        return chunks
    
    def _split_into_paragraphs(self, text: str) -> List[str]:
        """Split text into paragraphs."""
        # Split on double newlines or significant whitespace
        paragraphs = re.split(r'\n\s*\n', text)
        return [p for p in paragraphs if len(p.strip()) > 20]
    
    def _is_likely_equation(self, text: str) -> bool:
        """Heuristic to detect equations."""
        equation_markers = ['=', '∫', '∑', '∂', '≈', '≠', '≤', '≥', 
                           '∈', '∞', 'α', 'β', 'γ', 'θ', 'λ']
        
        # Check for mathematical symbols
        has_math_symbols = any(marker in text for marker in equation_markers)
        
        # Check for common equation patterns
        has_equation_pattern = bool(re.search(r'[a-zA-Z]\s*=\s*[^a-zA-Z\s]', text))
        
        return has_math_symbols or has_equation_pattern

# Usage example
def process_pdf_for_vdb(pdf_path: str) -> List[Dict[str, str]]:
    """Process PDF and return chunks ready for vector DB."""
    extractor = PDFExtractor(pdf_path)


    #NOTE A better way to extract text
    
    # Use PyMuPDF for better equation detection
    chunks = extractor.extract_with_pymupdf()
    
    # Filter out very short chunks
    filtered_chunks = [
        chunk for chunk in chunks 
        if len(chunk['content']) > 30
    ]
    
    return filtered_chunks

if __name__ == "__main__":
    pdf_file_path = "data/raw/books/hc_verma_kinematics_full.pdf"
    processed_chunks = process_pdf_for_vdb(pdf_file_path)

    import json

    with open("processed_chunks.json", "w") as f:
        json.dump(processed_chunks, f, indent=2)