from src.models import Judge, Show

judges = {}

def assign_judge(show: Show, name: str, criteria: list[str]) -> Judge:
    judge_id = len(judges) + 1
    judge = Judge(id=judge_id, name=name, criteria=criteria)
    judges[judge_id] = judge
    show.judges.append(judge_id)
    return judge

def record_result(show: Show, goat_id: int, score: int) -> None:
    if goat_id not in show.participants:
        raise ValueError("Goat not registered in this show")
    show.results[goat_id] = score
