import psycopg2


class ProjectRepository:

    @staticmethod
    def get_connection():

        return psycopg2.connect(
            host="localhost",
            database="developer_portfolio",
            user="sakshiadarkar",
            password=""
        )
    
if __name__ == "__main__":

    connection = ProjectRepository.get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM projects;")

    projects = cursor.fetchall()

    print(projects)

    cursor.close()
    connection.close()