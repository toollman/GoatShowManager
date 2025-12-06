from src.models import Show

shows = {}

def create_show(date: str, location: str) -> Show:
    show_id = len(shows) + 1
    show = Show(id=show_id, date=date, location=location,
                participants=[], judges=[], results={})
    shows[show_id] = show
    return show
