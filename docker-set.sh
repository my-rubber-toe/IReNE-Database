# Pull the latest image for mongo db
docker pull mongo

# Create docker volume to persist data
docker volume create IReNEdb_volume

# Create internal network for container communication
docker network create IReNEdb_network

# Create mongo container connected to the persistent volume and internal network
docker run -d --network IReNEdb_network -v IReNEdb_volume:/data/db --name IReNEdb mongo

# Create mongo-express container for UI management
docker run -d --network IReNEdb_network -e ME_CONFIG_MONGODB_SERVER=IReNEdb -p 8081:8081 --name mongo-express mongo-express


# IReNedb ip address for the schema_DB.py
docker inspect IReNEdb | grep IPAddress
