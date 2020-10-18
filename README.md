# UB Form
### Dumpdata
```
python manage.py dumpdata contact --output=contact/fixtures/data.json --indent=4
python manage.py dumpdata auth.user --output=auth_user_data.json --indent=4
```

### Loaddata
```
python manage.py loaddata data.json
python manage.py loaddata auth_user_data.json
```

