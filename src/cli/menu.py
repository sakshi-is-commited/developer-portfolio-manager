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
        elif choice == "3":
            while True:
                name = input("\nEnter project name to search: ").strip()
                if name:
                    break
                else:
                    print("Search text cannot be empty. Please try again.")
            
            projects = ProjectService.search_project(name)
            if projects:
                print("\n====================================")
                print(f"\nFound {len(projects)} project(s) matching '{name}':")
                print("\n====================================")
                for idx, project in enumerate(projects, start=1):
                    print(f"\nProject {idx}:")
                    for key, value in project.items():
                        print(f"{key.capitalize()}: {value}")
            else:
                print("\n====================================")
                print(f"\nNo projects found matching '{name}'.")
                print("\n====================================")

        elif choice == "4":
            ProjectService.update_project()

        elif choice == "5":
            projects = ProjectService.get_all_projects()

            if not projects:
                print("\nNo projects available to delete.\n")
                continue
            print("\nSelect a project to delete:\n")

            for index, project in enumerate(projects, start=1):
                print(f"{index}. {project['name']}")

            while True:
                try:
                    project_number = int(input("\nEnter project number: "))

                    if 1 <= project_number <= len(projects):
                        break
                    print("Invalid project number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid project number.")

            selected_project = projects[project_number - 1]
            print("\n====================================")
            print("Project Selected")
            print("====================================")

            print(f"Name       : {selected_project['name']}")
            print(f"Technology : {selected_project['technology']}")
            print(f"Status     : {selected_project['status']}")

            while True:

                confirmation = input(
                    "\nAre you sure you want to delete this project? (Y/N): "
                ).strip().upper()

                if confirmation == "N":
                    print("\nDeletion cancelled.\n")
                    break

                elif confirmation == "Y":
                    success = ProjectService.delete_project(project_number - 1)

                    if success:
                        print("\n====================================")
                        print("Project deleted successfully!")
                        print("====================================\n")
                    else:
                        print("\nFailed to delete project.\n")
                    break

                else:
                    print("Invalid input. Please enter Y or N.")

        elif choice == "6":
            print("\nGoodbyee👋🏻")
            break

        else:
            print("\nFeature not implemented yet.")
    

    
            

    
