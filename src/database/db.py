import psycopg2


def get_connection():

        return psycopg2.connect(
            host="localhost",
            database="developer_portfolio",
            user="sakshiadarkar",
            password="0297"
        )