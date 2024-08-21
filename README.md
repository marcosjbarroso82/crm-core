# CRM Core
This project is an excercise in creating a CRM system using Django. The project is a REST API for a CRM. The api is at `/api/v1/` and the documentation is at `/api/v1/docs/`. Swagger documentation can also be found at `/api/v1/schema/swagger-ui/`. Also a Postman collection can be found at `dev-resources/CRM.postman_collection`.


## Project setup for development

Run the following commands to setup the project for development:

```bash
mkdir -p local
cp crm_core/project/settings/templates/settings.dev.py ./local/settings.dev.py
cp crm_core/project/settings/templates/settings.unittests.py ./local/settings.unittests.py

```

To start the development server run the following command:
```bash
docker-compose -f docker-compose.dev.yml up
```


If you are using VSCode, you can simple execute the vscode command `Reopen in Dev Container` and build the project and leave you ready to work. Debugger is already configured.


### Running tests
From inside the container, run the following command to run the tests:
```bash
make test
```

### Running the project from inside the container
From inside the container, run the following command to run the project:
```bash
make migrate
make run-server
```

### CI/CD
The project is configured to run the tests and check linting before merging a PR. The CI/CD is configured using Github Actions.
To check if your code matches the requirements, run the following command:
```bash
make link
make test
```

## Commands
The project has a Makefile with some useful commands. To see all the commands available, run the following command:
```bash
make help
```


