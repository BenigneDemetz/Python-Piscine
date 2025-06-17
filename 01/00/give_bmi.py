
def check_bmi_types(height: list[int | float], weight: list[int | float]) -> int:
    """
    Check if the types of height and weight lists are valid.

    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: 0 if types are valid, raises TypeError otherwise.
    """
    
    if not isinstance(height, list) or not isinstance(weight, list):
        return True
    for h in height:
        if not isinstance(h, (int, float)):
            print("Height must be a list of numbers.")
            return True
        if h <= 0:
            print("Height must be greater than zero.")
            return True
    for w in weight:
        if not isinstance(w, (int, float)):
            print("Weight must be a list of numbers.")
            return True
        if w < 0:
            print("Weight must be positive.")
            return True
    return False

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for each pair of height and weight.

    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: List of BMI values.
    """
    if len(height) != len(weight):
        print("Height and weight lists must be of the same length.")
        return None
    if check_bmi_types(height, weight):
        return None
    return [w/(h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int | float) -> list[bool]:
    """
    Check if each BMI value is below a specified limit.

    :param bmi: List of BMI values.
    :param limit: The limit to compare against.
    :return: List of booleans indicating if each BMI is below the limit.
    """
    
    if not isinstance(limit, (int, float)):
        print("Limit must be a number.")
        return None
    return [b > limit for b in bmi]



# BMI = 	
# mass (kg) /
# height2 (m)
#  = 	
# 72.57 /
# 1.7782
#  = 23.0
