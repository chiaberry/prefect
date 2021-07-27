import asyncio
import prefect.orion.utilities
import prefect.orion.schemas
import prefect.orion.models
import prefect.orion.api

from prefect.orion.utilities.settings import Settings
from prefect.orion.utilities import database as _database

# if the orion database engine is in-memory, populate it.
# this will match any of the following connection strings:
# - sqlite+aiosqlite:///:memory:
# - sqlite+aiosqlite://
if (
    _database.engine.url.get_backend_name() == "sqlite"
    and _database.engine.url.database in (":memory:", None)
):
    asyncio.run(_database.create_database_objects())
