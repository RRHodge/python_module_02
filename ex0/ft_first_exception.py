def input_temperature(temp_str: str) -> int:
    """Convert a temperature string to an integer."""
    return int(temp_str)

def test_temperature() -> None:
    """Test the input_temperature function with valid and invalid inputs."""
    test_cases = ["25", "abc"]

    print("=== Garden Temperature ===")
    for temp_str in test_cases:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed = program didn't crash!")

if __name__ == "__main__":
    test_temperature()
