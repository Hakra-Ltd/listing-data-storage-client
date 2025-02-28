# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from listing_data_storage_client.api.health_api import HealthApi
    from listing_data_storage_client.api.info_api import InfoApi
    from listing_data_storage_client.api.paciolan_api import PaciolanApi
    from listing_data_storage_client.api.primary_api import PrimaryApi
    from listing_data_storage_client.api.stubhub_api import StubhubApi
    from listing_data_storage_client.api.tickpick_api import TickpickApi
    from listing_data_storage_client.api.vividseats_api import VividseatsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from listing_data_storage_client.api.health_api import HealthApi
from listing_data_storage_client.api.info_api import InfoApi
from listing_data_storage_client.api.paciolan_api import PaciolanApi
from listing_data_storage_client.api.primary_api import PrimaryApi
from listing_data_storage_client.api.stubhub_api import StubhubApi
from listing_data_storage_client.api.tickpick_api import TickpickApi
from listing_data_storage_client.api.vividseats_api import VividseatsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
