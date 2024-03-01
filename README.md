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

