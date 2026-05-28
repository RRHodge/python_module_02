def garden_operations(operation_number: int) -> None:
    """Simulate different types of errors based on operation_number."""
    if operation_number == 0:
        int("abc")  # ValueError
    elif operation_number == 1:
        1 / 0  # ZeroDivisionError
    elif operation_number == 2:
        open("/non/existent/file")  # FileNotFoundError
    elif operation_number == 3:
        "string" + 1  # TypeError

def test_error_types() -> None:
    """Test each error type and demonstrate handling."""
    print("--- Testing Different Error Types ---")

    for i in range(5):
        print(f"\nTesting operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
