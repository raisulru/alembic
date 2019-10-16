# Alembic-Project

This is a test project of alembic with sqlalchemy ORM. 
This is tested with postgres database. 
The database models is written by sqlalchemy and generate migrations file using alembic migration tool.
This project not used any web application.

# Seutp
- First create the original database with some base models.
- Now Initialize the alembic project folder with some file using command `alembic init <name>`.
- Now change the `.ini` file for database uri.
- Configure the `env.py` file.
- If all is ok then test your project using `alembic current` command.

# Migration Steps
- Set your database current state by runing `alembic revision -m "initial comment"`.
- Now apply this into database by runing `alembic upgrade head`.
- Now if you want to create new column or want to make relation with new table then set the new column `nullable=True`.
- By the above procedure generate migrations by runing `alembic revision --autogenerate -m "New comment"` and apply it by same command.
- Now fillup the new db column with runing db script.
- At last set the column `nullable=False` and migrate again.
