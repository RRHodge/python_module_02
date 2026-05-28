def input_temperature(temp_str: str) -> int:
    """Convert a temperature string to an integer and validate its range."""
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp

def test_temperature() -> None:
    """Test the input_temperature function with valid and invalid inputs."""
    test_cases = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")
    for temp_str in test_cases:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed = program didn't crash!")

if __name__ == "__main__":
    test_temperature()
