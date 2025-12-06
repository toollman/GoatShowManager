import csv
import json
from src.models import Show

def export_results_csv(show: Show, filename: str) -> None:
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Goat ID", "Score"])
        for goat_id, score in show.results.items():
            writer.writerow([goat_id, score])

def export_results_json(show: Show, filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(show.results, f, indent=4)
