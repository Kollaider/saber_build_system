# Saber Build System

The Saber Build System (SBS) is a build system designed to streamline and automate the game development process. 
It provides a set of tools and functionality that help game developers accelerate the build and delivery of their 
game projects.

SBS processes the build and task data and returns a list of tasks sorted according to their dependencies.
It uses a topological sorting algorithm to determine the order in which tasks are to be executed, given their dependencies.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Kollaider/saber_build_system.git
$ cd saber_build_system
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd saber_build_system
(env)$ python manage.py runserver
```
And navigate to browsable API to `http://127.0.0.1:8000/api/get_tasks/`.

## Walkthrough

Now you can only send POST requests with json body, for example:
```sh
{
	"build": "forward_interest"
}
```
as a response, you will receive a list of consecutive tasks sorted according to dependencies, as well as errors, if any.


## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```
