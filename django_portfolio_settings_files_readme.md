# Split settings files

- `config/settings/__init__.py` -> import from `base`
- `config/settings/base.py` -> main shared settings
- `config/settings/dev.py` -> development overrides
- `config/settings/prod.py` -> production overrides
- `config/asgi.py` -> ASGI entrypoint
- `config/wsgi.py` -> WSGI entrypoint
