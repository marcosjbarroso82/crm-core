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
make superuser
make run-server
```

### Using Examples in Postman Collection
A postman collection can be found in the folder `dev_tools` import that collection. In the environment variables, set `username` and `password` with the credentials of the superuser. You can use that user to create others and then change the credentials again.
Also, the collection can be found at [Postman Collection](https://universal-satellite-262876.postman.co/workspace/Monkey-CRM~bb32f883-6307-4118-b291-bec934cde3ec/collection/872186-e8f0e227-6613-4da6-9625-ae8e1ab9a59e?action=share&creator=872186&active-environment=872186-b479e34d-d399-454e-8e84-e7c1c2bb76f2)

### CI/CD
The project is configured to run the tests and check linting before merging a PR. The CI/CD is configured using Github Actions.
To check if your code matches the requirements, run the following command:
```bash
make lint
make test
```

## Commands
The project has a Makefile with some useful commands. To see all the commands available, run the following command:
```bash
make help
```


