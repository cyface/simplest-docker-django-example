# The Simplest Docker + Django Example

A very simple Docker + Django example to help folks learn how they can work together.

This repository is the companion to this article [The Simplest Docker + Django Example.](https://timlwhite.medium.com/the-simplest-django-docker-example-8ae479addf54)

### Commands

Build the Dockerfile into a runnable image:
- `docker build --tag docker-simple .`

Run the image you just built, exposing port 8000 and setting the `MAGIC_MESSAGE` environment variable:
- `docker run -p 8000:8000 -e MAGIC_MESSAGE="Docker command line" docker-simple`
- Ctrl-C to stop this ^^^

Use Docker Compose to do the same thing:
- `docker-compose up`
- Ctrl-C to stop this ^^^

Tag the image to upload to a container registry:
- `docker tag docker-demo <your docker id>/docker-simple:latest`
  (This only works if you already made a tag called docker-demo during the build step)

Upload the image to the container registry:
- `docker login`  (First time only)
- `docker push <your docker id>/docker-simple:latest`

Retrieve an image from the container registry:
- `docker pull <your docker id>/docker-simple:latest`

Run an image from the container registry:
- `docker run -p 8000:8000 -e MAGIC_MESSAGE="Docker command line" <your docker id>/docker-simple:latest`
- Try this from your machine!