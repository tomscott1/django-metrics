.env file:

```
export DJANGO_SETTINGS_MODULE="records.settings.dev"
export SECRET_KEY=
export DB_NAME=
export DB_HOST=
export DB_USER=
export DB_PASSWORD=
export DB_PORT=
```

---
Installing Requirements:

- Activate virtual environment

`pip install -r requirements/dev.txt`

`npm install`

`python manage.py migrate`

---

---
Running on dev:

- In it's own terminal

`node server.js`

- In another terminal

`./start.sh`

___
