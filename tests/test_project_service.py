import unittest
import os
import json

from src.services.project_service import ProjectService
from src.storage.json_storage import JSONStorage
from src.models.project import create_project

class TestProjectService(unittest.TestCase):
    def setUp(self):

        self.test_projects = []

        with open(JSONStorage.FILE_PATH, "w") as file:
            json.dump(self.test_projects, file)

    def tearDown(self):
        with open(JSONStorage.FILE_PATH, "w") as file:
            json.dump([], file)
    
    def test_add_project(self):

        project = create_project(
            "Portfolio Manager",
            "CLI App",
            "Python",
            "https://github.com/test",
            "Planned"
        )

        JSONStorage.save_project(project)

        projects = JSONStorage.load_projects()

        self.assertEqual(len(projects), 1)
    
    def test_search_existing_project(self):

        project = create_project(
            "Expense Tracker",
            "Finance APP",
            "Python",
            "github.com/test",
            "Completed"
        )

        JSONStorage.save_project(project)

        results = ProjectService.search_project("Expense")

        self.assertEqual(len(results), 1)
    
    def test_search_missing_project(self):

        results = ProjectService.search_project("Unknown")

        self.assertEqual(results, [])
    
    def test_update_project(self):

        project = create_project(
            "Portfolio",
            "CLI App",
            "Python",
            "",
            "Planned"
        )

        JSONStorage.save_project(project)

        updated_project = create_project(
            "Portfolio",
            "CLI App",
            "Flask",
            "",
            "Completed"
        )

        result = ProjectService.update_project_data(
            0,
            updated_project
        )

        self.assertTrue(result)

        projects = JSONStorage.load_projects()

        self.assertEqual(
            projects[0]['technology'],
            "Flask"
        )

        self.assertEqual(
            projects[0]['status'],
            "Completed"
        )

    def test_delete_project(self):

        project = create_project(
            "Portfolio",
            "CLI App",
            "Python",
            "",
            "Planned"
        )

        JSONStorage.save_project(project)

        ProjectService.delete_project(0)

        projects = JSONStorage.load_projects()

        self.assertEqual(len(projects), 0)