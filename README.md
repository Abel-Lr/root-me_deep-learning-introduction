# [[Root-Me]](https://www.root-me.org/) Deep Learning - Introduction

## Summary

- [\[Root-Me\] Deep Learning - Introduction](#root-me-deep-learning---introduction)
  - [Summary](#summary)
  - [Context](#context)
  - [Running this project](#running-this-project)
    - [With Docker](#with-docker)
        - [Build](#build)
        - [Run](#run)
    - [Without Docker](#without-docker)
        - [Build](#build-1)
          - [Windows](#windows)
          - [Linux](#linux)
        - [Installing dependancies](#installing-dependancies)
        - [Run](#run-1)
  - [Result](#result)


## Context

In [this challenge](https://www.root-me.org/en/Challenges/Programming/Deep-Learning-Introduction), the goal is to classify each image in the "Flag" directory as either a cat (1) or a dog (0). Each prediction should correspond to a pixel in a flag, where a "cat" is represented by a black pixel and a "dog" by a white pixel.

To reconstruct the flag, you need to use the coordinates embedded in the image filenames. Each image file follows the format row_column.jpg, where:

- Row represents the row coordinate of the pixel.

- Column represents the column coordinate of the pixel.

For example:

The prediction for the image 78_6.jpg corresponds to the pixel at row 78 and column 6 in the flag.

## Running this project

Duration of the execution will depend on your hardware due to usage of Deep Learning model.

### With Docker

Make sure you have Docker and Docker Compose installed. Then start a shell with the root of the project as cwd.

##### Build

To build the Docker image, run the following command:

```bash
docker-compose build
```

##### Run

Once the image is built, you can start the container with the following command:

```bash
docker-compose up
```

This will start the container and the application inside it. If you don't want to see any logs or output run the following command instead:

```bash
docker-compose up -d
```

If you don't want to clone the project you can get it from

```bash
docker pull ghcr.io/abel-lr/root-me_deep-learning-introduction:latest
```

### Without Docker

Make sure you have [uv](https://github.com/astral-sh/uv) installed. Install with it Python 3.9.23 as specified in the `pyproject.toml` file.

##### Build

```bash
uv python install 3.9.23
```

Check if the installation succeeds

```bash
uv python list
```

The path next to `cpython-3.9.23-linux-x86_64-gnu` should be displayed.

This Python interpreter has to be used by default then executing the following command

```bash
uv python pin 3.9.23
```

Then start the virtual env using

###### Windows
```bash
uv venv
.venv\Script\activate
```

###### Linux
```bash
uv venv
source .venv/bin/activate
```
You can exit the venv with the command `deactivate`.

##### Installing dependancies

Install packages while **inside** the venv with the command 
```bash
uv add -r requirements.txt
```

##### Run

Finally, the Python script can be executed **inside** the venv by doing

```bash
uv run main.py
```

## Result

After a while depending on your hardware, the Flag image will be generated inside the `result` folder.