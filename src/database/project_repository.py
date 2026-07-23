from src.database.db import get_connection


class ProjectRepository:
    @staticmethod
    def add_project(project):

        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                INSERT INTO projects (name, description, technology, github, status)
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    project["name"],
                    project["description"],
                    project["technology"],
                    project["github"],
                    project["status"]
                )
            )

            connection.commit()

            return True
        except Exception as e:
            print(f"Database Error: {e}")

            if connection:
                connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    
if __name__ == "__main__":

    project = {
        "name": "Developer Portfolio Manager",
        "description": "CLI Project",
        "technology": "Python",
        "github": "https://github.com/example/project",
        "status": "In Progress"
    }

    success = ProjectRepository.add_project(project)

    if success:
        print("✅ Project inserted successfully!")
    else:
        print("❌ Failed to insert project.")
