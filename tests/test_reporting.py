import os
from src.models import Show
from src.services import reporting

def test_generate_exhibitor_report_text():
    show = Show(id=1, date="2025-12-05", location="Jacksonville Fairgrounds",
                participants=[1, 2], judges=[], results={1: 87, 2: 92})
    report = reporting.generate_exhibitor_report_text(show)
    assert "Goat Show Report - Show 1" in report
    assert "Goat 1 - Score: 87" in report
    assert "Goat 2 - Score: 92" in report
    assert "Exhibitor Signature" in report

def test_generate_exhibitor_report_pdf(tmp_path):
    show = Show(id=1, date="2025-12-05", location="Jacksonville Fairgrounds",
                participants=[1], judges=[], results={1: 87})
    filename = tmp_path / "report.pdf"
    reporting.generate_exhibitor_report_pdf(show, str(filename))
    assert os.path.exists(filename)
    assert filename.stat().st_size > 0
