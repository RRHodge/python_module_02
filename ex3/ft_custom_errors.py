class GardenError(Exception):
    """Base class for garden-related errors."""
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    """Error related to plants."""
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    """Error related to watering."""
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)

def test_plant_error() -> None:
    """Raise and catch a PlantError."""
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

def test_water_error() -> None:
    """Raise and catch a WaterError."""
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

def test_garden_error() -> None:
    """Demonstrate catching all garden errors with GardenError."""
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")

def main() -> None:
    """Run all tests for custom errors."""
    print("--- Custom Garden Errors Demo ---")

    print("\nTesting PlantError...")
    test_plant_error()

    print("\nTesting WaterError...")
    test_water_error()

    print("\nTesting catching all garden errors...")
    test_garden_error()

    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    main()
