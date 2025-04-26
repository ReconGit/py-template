from src.deps.my_deps import my_dep


def my_function():
    dep = my_dep()
    if dep == "my_dep":
        return True
    else:
        return False


# Protoyping
if __name__ == "__main__":
    if my_function():
        print("Function executed successfully.")

