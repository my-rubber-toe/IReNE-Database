#pulls specific image with specified mongodb version
docker pull mongo:4.2.3

#runs container with IReNEdb
docker run -d -p 20170:20170 --name IReNEdb mongo:4.2.3

#setting an enviornment to work inside the container
docker exec -it IReNEdb bash

#runs mongoshell
mongo

#exit -> getting out of the env
#docker stop IReNEdb -> close and save container