"""TODO: describe what this module is for."""


def letter_grade(gpa):
    """This function show each gpa with its corresponding letter grape according to the grade system"""
    # TODO: your if/elif chain here
    if gpa>=4.5:
        return "A"
    elif gpa>=3.5:
        return "B"
    elif gpa>=2.5:
        return "C"
    elif gpa>=1.5:
        return "D"
    elif gpa<1.5:
        return "F"

