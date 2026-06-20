
# uv command

Requirements to run this project:

1. Make sure you have Docker installed on your machine.
2. You have Git/Bash installed on your machine.

Get Started

### Step 1: Clone this project onto your local directory on your machine.
git clone https://github.com/heatkoemnak/trainiscord.git

### Step 2: Copy the environment from this project by using this command:
cp .env

### Step 3: Add your config pgadmin and posgtres database on this .env file
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DATABASE_URL=
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=

example:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456
POSTGRES_DB=example_db
DATABASE_URL=postgresql://postgres:123456@postgres:5432/example_db

PGADMIN_DEFAULT_EMAIL=admin@gmail.com
PGADMIN_DEFAULT_PASSWORD=admin

## Step 4: Build up project by running this following command:
docker compose up --build

## Step 5: Test api by open the browser and past this 
http://localhost/docs

## Step 6: Test pgAdmin
http://localhost:5050

then enter email and password from this value:
PGADMIN_DEFAULT_EMAIL=admin@gmail.com
PGADMIN_DEFAULT_PASSWORD=admin

## Step 7: Find PostgreSQL Container IP Address
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' example_db

## Step 8: Connect to PostgreSQL via pgAdmin
docker exec -it postgres psql -U postgres  
