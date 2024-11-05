def count_str(lst):
    if not lst:
        return 0
    return (1 if isinstance(lst[0], str) else 0) + count_str(lst[1:])
