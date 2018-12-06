# bookshop_graphql
Django+Graphene, GraphQL Demo

```bash
virtualenv --no-site-packages -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## Test
```bash
cd backend/bookshop/
pytest
```
