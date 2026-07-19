from src.services.project_service import ProjectService
from src.utils.helpers import (
    print_header,
    print_project,
    print_success,
    print_error,
    print_warning
)

def display_menu():
    
    print_header("Developer Portfolio Manager")

    print("1️⃣  Add Project")
    print("2️⃣  View Projects")
    print("3️⃣  Search Project")
    print("4️⃣  Update Project")
    print("5️⃣  Delete Project")
    print("6️⃣  Exit")

    print("=" * 40)
    while True:
        try:
            choice = input("\nEnter your choice: ")

            if choice == "1":
                ProjectService.add_project()
            
            elif choice == "2":
                projects = ProjectService.get_all_projects()
                if not projects:
                    print_warning("No projects found.")
                    print("Add all your projects")
                else:
                    print_header("DEVELOPER PORTFOLIO")

                    for idx, project in enumerate(projects, start=1):
                        print_project(project, idx)
            elif choice == "3":
                while True:
                    name = input("\nEnter project name to search: ").strip()
                    if name:
                        break
                    else:
                        print_error("Search text cannot be empty. Please try again.")
                
                projects = ProjectService.search_project(name)
                if projects:
                    print_header(
                        f"Found {len(projects)} project(s) matching '{name}'"
                    )   
                    for idx, project in enumerate(projects, start=1):
                        print_project(project, idx)
                else:
                    print_header(f"No projects found matching '{name}'")
                    

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
                        print_error("Invalid project number.")
                    except ValueError:
                        print_error("Invalid input. Please enter a valid project number.")

                selected_project = projects[project_number - 1]
                
                print_header("Project Selected")
                print_project(selected_project)

                while True:

                    confirmation = input(
                        "\nAre you sure you want to delete this project? (Y/N): "
                    ).strip().upper()

                    if confirmation == "N":
                        print_warning("Deletion cancelled.")
                        break

                    elif confirmation == "Y":
                        success = ProjectService.delete_project(project_number - 1)

                        if success:
                            print_success("Project deleted successfully!")
                            
                        else:
                            print_error("Failed to delete project.")
                        break

                    else:
                        print_error("Invalid input. Please enter Y or N.")

            elif choice == "6":
                print("\nGoodbyee👋🏻")
                break

            else:
                print("\nFeature not implemented yet.")
        
        except KeyboardInterrupt:
            print_warning("Application interrupted by user. Exiting... ")
            break 

        except Exception as e:
            print_error(f"An unexpected error occurred: {e}")
            break
    

    
            

    
