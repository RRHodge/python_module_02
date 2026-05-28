from ft_custom_errors import PlantError

def water_plant(plant_name: str) -> None:
    """Water a plant if its name is capitalized."""
    if not plant_name.istitle():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")

def test_watering_system() -> None:
    """Test the watering system with valid and invalid plant names."""
    print("Opening watering system")
    try:
        # Test with valid plants
        print("\nTesting valid plants...")
        plants = ["Tomato", "Lettuce", "Carrots"]
        for plant in plants:
            water_plant(plant)

        # Test with invalid plants
        print("\nTesting invalid plants...")
        plants = ["Tomato", "lettuce"]
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

def main() -> None:
    """Run the watering system tests."""
    print("--= Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering_system()

    print("\nTesting invalid plants...")
    test_watering_system()

    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    main()
