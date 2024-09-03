import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="ah_datahub_szapi",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="ah_datahub_szapi_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from ah_datahub_szapi.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export ah_datahub_szapi_KEY=value
export ah_datahub_szapi_KEY="@int 42"
export ah_datahub_szapi_KEY="@jinja {{ this.db.uri }}"
export ah_datahub_szapi_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
ah_datahub_szapi_ENV=production ah_datahub_szapi run
```

Read more on https://dynaconf.com
"""
