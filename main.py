from src.cli.menu import display_menu

def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "6":
            print("\nGoodbyee👋🏻")

        else:
            print("\nFeature not implemented yet.")

if __name__ == "__main__":
    main()