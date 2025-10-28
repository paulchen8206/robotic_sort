def sort(width, height, length, mass):
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("All input values must be non-negative.")

    # Check bulky condition
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Check heavy condition
    is_heavy = mass >= 20

    # Determine stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
