import json
import os

class JSONStorage:
    FILE_PATH = "projects.json"

    @classmethod
    def save_project(cls, project):
        
        #Create file if it doesn't exist
        if not os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, 'w') as file:
                json.dump([], file)

        #Read existing data
        with open(cls.FILE_PATH, 'r') as file:

            try:
                projects = json.load(file)

            except json.JSONDecodeError:
                projects = []

        #Append new project
        projects.append(project)

        #Save updated list
        with open(cls.FILE_PATH, 'w') as file:
            json.dump(projects, file, indent=4)
    @classmethod
    def load_projects(cls):
        if not os.path.exists(cls.FILE_PATH):
            return []

        with open(cls.FILE_PATH, 'r') as file:
            try:
                projects = json.load(file)
                return projects
            except json.JSONDecodeError:
                return []