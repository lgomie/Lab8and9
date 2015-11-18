

commands = {'List all containers', 'List running containers', 'Inspect a container', 'Delete a container', 'Delete all containers', 'Create a container from an image', 'Restart a container', 'Stop a container' ,'Show logs from a container', 'List all images', 'Delete an image', 'Delete all images', 'TAG an image', 'create Docker images from local Dockerfile'};

no = 0
for i in commands:
    print no, "-", i
    no = no + 1
