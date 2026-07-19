from src.models.project import create_project
from src.storage.json_storage import JSONStorage
from src.utils.helpers import get_valid_input, print_error, print_header, print_success
from src.utils.validators import (validate_name, validate_technology, validate_status)


class ProjectService:
    @staticmethod
    def add_project():

        #Project Name
        name = get_valid_input(
            "Enter project name: ",
            validate_name,
            "Invalid name. Please try again."
    )

        #Project Description
        description = input("Enter project description: ")

        #Project Technology
        technology = get_valid_input(
            "Enter project technology: ",
            validate_technology,
            "Invalid technology. Please try again."
        )

        #Project GitHub Link
        github = input("Enter project GitHub link: ")

        #Project Status
        #while True:
        print("\nSelect project status:")
        print("Planned")
        print("In Progress")
        print("Completed")

        status = get_valid_input(
            "Enter project status: ",
            validate_status,
            "Invalid status. Please try again."
        )
            

        # Create project dictionary
        project = create_project(name, description, technology, github, status)

        JSONStorage.save_project(project)

        
        print_success("Project added successfully!")
        



    @staticmethod
    def get_all_projects():
        return JSONStorage.load_projects()
    
    @staticmethod
    def search_project(name):
        projects = JSONStorage.load_projects()


        matching_projects = []

        search_text = name.strip().lower()

        for project in projects:

            #print("Checking:", project["name"])

            if search_text in project["name"].strip().lower():
                #print("Matched!")
                matching_projects.append(project)

        return matching_projects
    
    @staticmethod
    def update_project():
        projects = JSONStorage.load_projects()

        if not projects:
            print("No projects found.")
            return

        print("\nSelect a project to update:")
        for idx, project in enumerate(projects, start=1):
            print(f"{idx}. {project['name']}")

        while True:
            try:
                choice = int(input("Enter the project number: "))
                if 1 <= choice <= len(projects):
                    selected_project = projects[choice - 1]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Update project details
        print("\nEnter new details (leave blank to keep current value):")
        new_name = input(f"Name [{selected_project['name']}]: ") or selected_project['name']
        new_description = input(f"Description [{selected_project['description']}]: ") or selected_project['description']
        new_technology = input(f"Technology [{selected_project['technology']}]: ") or selected_project['technology']
        new_github = input(f"GitHub Link [{selected_project['github']}]: ") or selected_project['github']
        new_status = input(f"Status [{selected_project['status']}]: ") or selected_project['status']

        # Validate updated fields
        if not validate_name(new_name):
            print("Invalid name. Update aborted.")
            return
        if not validate_technology(new_technology):
            print("Invalid technology. Update aborted.")
            return
        if not validate_status(new_status):
            print("Invalid status. Update aborted.")
            return

        # Update the project
        updated_project = {
            "name": new_name,
            "description": new_description,
            "technology": new_technology,
            "github": new_github,
            "status": new_status
        }

        if ProjectService.update_project_data(choice - 1, updated_project):
            print_success("Project updated successfully!")
        else:
            print_error("Unable to update project")
    @staticmethod
    def delete_project(project_index):

        projects = JSONStorage.load_projects()

        if project_index < 0 or project_index >= len(projects):
            return False
        
        return JSONStorage.delete_project(project_index)
    
    @staticmethod
    def update_project_data(index, updated_project):

        projects = JSONStorage.load_projects()

        if index < 0 or index >= len(projects):
            return False
        
        projects[index] = updated_project

        return JSONStorage.save_all_projects(projects)