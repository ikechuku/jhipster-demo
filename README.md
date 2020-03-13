# Rest API for jhipster-tripetto demo

## Technolgies

* [Python 3.7](https://python.org) : Base development programming language


* [Django Framework](https://www.djangoproject.com/) : Host development framework built on top of python
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
<!-- * [CircleCI]() : Continous Integration and Deployment -->
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the appication and services orchestration
* [Yeoman](https://yeoman.io/) : Scaffolding tool for modern webapps
* [Tripetto](https://tripetto.com//) : Smart forms and surveys with visual form builder


## Getting Started

Few things you need to setup to get started, set up a virtual environment majorly for isolating installs, create a `.env` file from the example file and finally install all requirements in the `requirements.txt` files within the virtual environment.

Fortunately for us, we already have a convenient [script](https://github.com/decagonhq/bouncer-restapi/blob/master/bin/setup) for this, we are only left with understanding what it actually does as opposed to just using it.

Note that you do not need to bother about activating virtual environments when installing or uninstalling packages using the `bin/install` and `bin/uninstall` scripts, unless you are running them directly yourself with `pip`.

```bash

# Clone the repository

# Change directory into the cloned folder and run the setup script
$ cd bouncer-restapi
$ bin/setup

# Update .env file content as necessary. Not sure if values to set? ask the Leads

# Start the application containers and open it in browser
$ bin/start -d && bin/open

```

## License

The MIT License - Copyright (c) 2020 