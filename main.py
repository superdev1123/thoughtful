def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def run_tests():
    tests = [
        # (width, height, length, mass, expected result)
        (100, 100, 100, 10, "SPECIAL"),      # Volume = 1,000,000 → bulky
        (200, 50, 50, 10, "SPECIAL"),        # Width = 200 → bulky
        (50, 50, 50, 25, "SPECIAL"),         # Mass = 25 → heavy
        (200, 200, 200, 25, "REJECTED"),     # Bulky + heavy
        (10, 10, 10, 1, "STANDARD"),         # Small and light
        (150, 10, 10, 10, "SPECIAL"),        # Dimension = 150 → bulky
        (100, 100, 100, 20, "SPECIAL"),      # Mass = 20 → heavy
        (10, 10, 10, 20, "SPECIAL"),         # Only heavy
        (160, 160, 160, 5, "SPECIAL"),       # Only bulky
        (160, 160, 160, 25, "REJECTED")      # Both
    ]

    for i, (w, h, l, m, expected) in enumerate(tests, 1):
        result = sort(w, h, l, m)
        print(f"Test {i}: sort({w}, {h}, {l}, {m}) = {result} — {'✅ Pass' if result == expected else f'❌ Fail (Expected {expected})'}")

if __name__ == "__main__":
    run_tests()
