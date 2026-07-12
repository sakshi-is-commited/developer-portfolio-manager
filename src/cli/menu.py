from src.services.project_service import ProjectService

def display_menu():
    print("\n==============================")
    print("Developer Portfolio Manager")
    print("==============================")
    print("1. Add Project")
    print("2. View Project")
    print("3. Search Project")
    print("4. Update Project")
    print("5. Delete Project")
    print("6. Exit")

    while True:

        choice = input("\nEnter your choice: ")

        if choice == "1":
            ProjectService.add_project()
        
        elif choice == "2":
            projects = ProjectService.get_all_projects()
            if not projects:
                print("====================================")
                print("\nNo projects found.")
                print("\nAdd all your projects")
                print("====================================")
            else:
                print("====================================")
                print("\nMY PORTFOLIO PROJECTS:")
                print("\n====================================")
                for idx, project in enumerate(projects, start=1):
                    print(f"\nProject {idx}:")
                    for key, value in project.items():
                        print(f"{key.capitalize()}: {value}")

        elif choice == "6":
            print("\nGoodbyee👋🏻")
            break

        else:
            print("\nFeature not implemented yet.")
    

    
            

    
