#pulls specific image with specified mongodb version
docker pull mongo:4.2.3

#runs container with IReNEdb
docker run -d -p 27017:27017 -v /Users/jaits/data:/data/db --name IReNE mongo

#setting an enviornment to work inside the container
docker exec -it IReNE bash

#runs mongoshell
mongo

#exit -> getting out of the env
#docker stop IReNEdb -> close and save container