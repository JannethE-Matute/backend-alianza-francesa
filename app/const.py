import os

# HASURA_JWT_SECRET = os.getenv("HASURA_GRAPHQL_JWT_SECRET",
#                               "tpoocLsdLnxXbIMeg.t63ceLu6DzLHuLIEH0J5MWFJNvH.-B0OwQEv3fP32L-mZ8")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv('POSTGRES_DB', 'socialdb')
password = os.getenv('POSTGRES_PW', 'micasa1997')