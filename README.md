# docker-courses


## les images:
trouver une image
`https://hub.docker.com/`

 Télécharger une image
```bash
docker pull <image>
```
voir les images téléchargées
```bash
docker images
```
Clean non used object
```bash
docker system prune
```
supprimer une image
```bash
docker rmi <image>
```
build une image:
```bash
docker build -t nom_de_votre_image:tag .
```

## les conteneurs:

run un conteneur a partir d'une image

```bash
docker run -d <image>
```

```bash
docker run -p 3000:3000 -d nom_de_votre_image:tag
```


supprimer un conteneur
```bash
docker rm <conteneur>
```

Voir les conteneurs actifs:
```bash
docker ps
```
Voir tous les conteneurs:
```bash
docker ps -a
```
relancer un conteneur
```bash
docker start <conteneur>
```

Stopper un conteneur:
```bash
docker stop <conteneur>
```

entrer dans un conteneur:
```bash
docker exec -it <conteneur> /bin/bash
```

vois les logs d'un conteneur:
```bash
docker logs <conteneur>
```

## les volumes:
- bind mount: relier au pc local
- volume: espace de stockage propre au conteneur

créer un volume:
```bash
docker volume create <nom_volume>
```
voir les volumes:
```bash
docker volume ls
```
