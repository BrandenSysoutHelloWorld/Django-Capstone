# Eskak WebApplication

Welcome to the Django Project - Featuring Eskak Web Application with Generated Documentation by Sphinx.

## Table of Contents
1. [Overview](#overview)
2. [Getting Started](#getting-started)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Build the Docker Image](#step-2-build-the-docker-image)
    - [Step 3: Check the Docker Container](#step-3-check-the-docker-container)
    - [Step 4: Find the Port](#step-4-find-the-port)
    - [Step 5: Access the Application](#step-5-access-the-application)
3. [About the Application](#about-the-application)
4. [Contributing](#contributing)
5. [License](#license)

## Overview

The Django Capstone Project, featuring the Eskak Web Application, is a web application designed to track a user's power consumption by recording electricity units and generating reports and other useful data.

## Getting Started

Follow these steps to set up and run the Eskak Web Application on your local environment.

### Step 1: Clone the Repository

```bash
git clone https://github.com/BrandenSysoutHelloWorld/Django-Capstone.git
```

### Step 2: Build the Docker Image

```bash
cd Django-Capstone/myEskak
docker build -t eskak ./
```

### Step 3: Check the Docker Container

Run the following command to view a list of running containers:

```bash
docker ps
```

### Step 4: Find the Port

Copy the Container ID from the previous step and run the following command to find the port that the container is using:

```bash
docker port <container_id>
```

Make note of the port for the next step.

### Step 5: Access the Application

Open your web browser and enter the following URL, replacing `<docker_container_port>` with the port number obtained in Step 4:

```
http://localhost:<docker_container_port>
```

You should now be able to access the Eskak Web Application in your browser.

## About the Application

The Eskak Web Application is designed to help users track their power consumption by recording electricity units and generating valuable reports and insights.

## License
non

Thank you for using Eskak Web Application!

---

**Developed by Branden van Staden**
