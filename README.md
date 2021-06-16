# Mayaa
Mayaa is a discord bot for the server Hova.finance

## Requirements
 - Python 3.7+
 - Docker
 - docker-compose

**Note:** Docker and docker-compose are required if a local postgres database is required.

## Installing dependencies
 - Open a terminal at the root of the project and run the following command.
```bash
pip install -r requirements.txt
```

## Running a database instance locally (Optional)
 **Note:** In case an existing Postgres database is used, the connection details must be specified in the .env file

 - Run the following command at the root of the project directory
```bash
docker-compose up -d
```

## Running the bot
 - Run this command in the *src* folder of the project 
```bash
python launcher.py
```

## Help
 - For more details about the commands use the *help* command.