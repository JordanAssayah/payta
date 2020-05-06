# Quickstart
First, set your app's secret key as an environment variable. For example,
add the following to `.bashrc` or `.bash_profile`.

```bash
export SRC_SECRET='something-really-secret'
```

Before running shell commands, set the `FLASK_APP` and `FLASK_DEBUG`
environment variables
```bash
export FLASK_APP=/path/to/server.py
export FLASK_DEBUG=1
```

Then run the following commands to bootstrap your environment
```bash
git clone https://github.com/gothinkster/flask-realworld-example-app.git
cd flask-realworld-example-app
```

Run the following commands to create your app's
database tables and perform the initial migration
```bash
flask db init
flask db migrate
flask db upgrade
```

To run the web application use
```bash
flask run --with-threads
```


# Deployment

In your production environment, make sure the `FLASK_DEBUG` environment
variable is unset or is set to `0`, so that `ProdConfig` is used, and
set `DATABASE_URL` which is your postgresql URI for example
`postgresql://localhost/example` (this is set by default in heroku).


# Shell

To open the interactive shell, run
```bash
flask shell
```

By default, you will have access to the flask `app` and models.


# Running Tests

To run all tests, run
```bash
flask test
```

# Migrations

Whenever a database migration needs to be made. Run the following commands ::
```bash
flask db migrate
```

This will generate a new migration script. Then run
```bash
flask db upgrade
```

To apply the migration.

For a full migration command reference, run `flask db --help`.
