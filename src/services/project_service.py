from src.models.project import create_project
from src.storage.json_storage import JSONStorage
from src.utils.validators import (validate_name, validate_technology, validate_status)


class ProjectService:
    @staticmethod
    def add_project():

        #Project Name
        while True:
            name = input("Enter project name: ")
            if validate_name(name):
                break
            else:
                print("Invalid name. Please try again.")

        #Project Description
        description = input("Enter project description: ")

        #Project Technology
        while True:
            technology = input("Enter project technology: ")
            if validate_technology(technology):
                break
            else:
                print("Invalid technology. Please try again.")

        #Project GitHub Link
        github = input("Enter project GitHub link: ")

        #Project Status
        while True:
            print("\nSelect project status:")
            print("Planned")
            print("In Progress")
            print("Completed")

            status = input("Enter project status: ")
            if validate_status(status):
                break
            print("Invalid status. Please try again.\n")

        # Create project dictionary
        project = create_project(name, description, technology, github, status)

        JSONStorage.save_project(project)

        print("\n====================================")
        print("Project added successfully!")
        print("====================================\n")



    @staticmethod
    def get_all_projects():
        return JSONStorage.load_projects()
    
    @staticmethod
    def search_project(name):
        projects = JSONStorage.load_projects()


        matching_projects = []

        search_text = name.strip().lower()

        for project in projects:

            print("Checking:", project["name"])

            if search_text in project["name"].strip().lower():
                print("Matched!")
                matching_projects.append(project)

        return matching_projects