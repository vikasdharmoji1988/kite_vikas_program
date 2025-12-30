from datetime import datetime, timedelta

def get_older_date(from_date: str, days: int) -> str:
    """
    Returns a date string that is 'days' before the given from_date.

    Args:
        from_date (str): Date in "YYYY-MM-DD" format.
        days (int): Number of days to subtract.

    Returns:
        str: Older date in "YYYY-MM-DD" format.
    """
    base_date = datetime.strptime(from_date, "%Y-%m-%d").date()
    older_date = base_date - timedelta(days=days)
    return older_date.strftime("%Y-%m-%d")

# Example usage:
# from_date = "2025-09-01"
# print(get_older_date(from_date, 700))  # ➝ "2023-09-01"
