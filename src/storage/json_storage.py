import json
import os

from src.utils.helpers import print_warning, print_error

class JSONStorage:
    FILE_PATH = "projects.json"

    @classmethod
    def save_project(cls, project):

        try:

            # Create file if it doesn't exist
            if not os.path.exists(cls.FILE_PATH):
                with open(cls.FILE_PATH, "w") as file:
                    json.dump([], file)

            # Read existing projects
            with open(cls.FILE_PATH, "r") as file:
                try:
                    projects = json.load(file)
                except json.JSONDecodeError:
                    print_warning(
                        "Projects file is corrupted.\nStarting with an empty portfolio..."
                    )
                    projects = []

            # Add the new project
            projects.append(project)

            # Save updated projects
            with open(cls.FILE_PATH, "w") as file:
                json.dump(projects, file, indent=4)

            return True
        except PermissionError:
            print_error(
                "Permission denied.\nUnable to save project."
            )
            return False

        except Exception as e:
            print_error(
                f"Unexpected error:\n{e}"
            )
            return False

    @classmethod
    def load_projects(cls):
        if not os.path.exists(cls.FILE_PATH):
            print_warning("Unable to load projects.\nStarting with an empty portfolio...")
            with open(cls.FILE_PATH, 'w') as file:
                json.dump([], file)
            return []

        try:

            with open(cls.FILE_PATH, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print_warning(
            "Projects file is corrupted.\nStarting with an empty portfolio..."
            )
            return []

        except PermissionError:
            print_error(
                "Permission denied while reading projects."
            )
            return []

        except Exception as e:
            print_error(
                f"Unexpected error:\n{e}"
            )
            return []
    
    @classmethod
    def save_all_projects(cls, projects):

        try:
            with open(cls.FILE_PATH, "w") as file:
                json.dump(projects, file, indent=4)

            return True

        except PermissionError:
            print_error(
                "Permission denied.\nUnable to save projects."
            )
            return False

        except Exception as e:
            print_error(
                f"Unexpected error:\n{e}"
            )
            return False
    @classmethod
    def delete_project(cls, index):
        """
        Delete a project at the specified index.

        Returns:
            True -> Project deleted successfully.
            False -> Invalid index or deletion failed.
        """

        projects = cls.load_projects()

        if index < 0 or index >= len(projects):
            return False
        
        try:

            projects.pop(index)

            with open(cls.FILE_PATH, "w") as file:
                json.dump(projects, file, indent=4)

            return True

        except PermissionError:

            print_error(
                "Permission denied.\nUnable to delete project."
            )

            return False

        except Exception as e:

            print_error(
                f"Unexpected error:\n{e}"
            )

            return False