from src.models import Show
from fpdf import FPDF  # lightweight PDF library

def generate_exhibitor_report_text(show: Show) -> str:
    """Generate a text report for exhibitors to sign."""
    lines = []
    lines.append(f"Goat Show Report - Show {show.id}")
    lines.append(f"Date: {show.date} | Location: {show.location}")
    lines.append("=" * 40)
    lines.append("Participants:")
    for goat_id in show.participants:
        score = show.results.get(goat_id, "Pending")
        lines.append(f"Goat {goat_id} - Score: {score}")
    lines.append("=" * 40)
    lines.append("Exhibitor Signature: _____________________")
    return "\n".join(lines)

def generate_exhibitor_report_pdf(show: Show, filename: str) -> None:
    """Generate a PDF report for exhibitors to sign."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Goat Show Report - Show {show.id}", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Date: {show.date} | Location: {show.location}", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt="Participants:", ln=True)
    for goat_id in show.participants:
        score = show.results.get(goat_id, "Pending")
        pdf.cell(200, 10, txt=f"Goat {goat_id} - Score: {score}", ln=True)

    pdf.ln(20)
    pdf.cell(200, 10, txt="Exhibitor Signature: _____________________", ln=True)

    pdf.output(filename)
