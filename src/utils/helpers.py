def print_separator():
    print("=" * 40)


def print_header(title):
    print()
    print_separator()
    print(title)
    print_separator()


def pause():
    input("\nPress Enter to continue...")


def clear_screen():
    print("\n" * 40)


def get_valid_input(prompt, validator, error_message):
    while True:
        value = input(prompt).strip()

        if validator(value):
            return value

        print(error_message)

def print_success(message):
    print()
    print("=" * 40)
    print(f"✅ {message}")
    print("=" * 40)


def print_error(message):
    print()
    print("=" * 40)
    print(f"❌ {message}")
    print("=" * 40)


def print_warning(message):
    print()
    print("=" * 40)
    print(f"⚠️ {message}")
    print("=" * 40)

def print_project(project, number=None):

    if number is not None:
        print(f"\n📁 Project #{number}")
    else:
        print("\n📁 Project")

    print(f"Name        : {project['name']}")
    print(f"Description : {project['description']}")
    print(f"Technology  : {project['technology']}")
    print(f"Status      : {project['status']}")
    print(f"GitHub      : {project['github']}")

    print("-" * 42)