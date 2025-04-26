from src.core.my_file import my_function
from src.core.settings import settings


def main():
    if my_function():
        print("Function executed successfully.")
    else:
        print("Function execution failed.")
    
    print(f"My endpoint: {settings.MY_ENDPOINT}")


if __name__ == "__main__":
    main()
