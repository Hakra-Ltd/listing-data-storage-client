import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.listing_change_response_schema import ListingChangeResponseSchema
from ...types import UNSET, Response


def _get_kwargs(
    *,
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v0/listing/getChanges",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ListingChangeResponseSchema]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListingChangeResponseSchema.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, ListingChangeResponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> Response[Union[HTTPValidationError, ListingChangeResponseSchema]]:
    """Listing Change

    Args:
        start_date (datetime.datetime):
        end_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListingChangeResponseSchema]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> Optional[Union[HTTPValidationError, ListingChangeResponseSchema]]:
    """Listing Change

    Args:
        start_date (datetime.datetime):
        end_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListingChangeResponseSchema]
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> Response[Union[HTTPValidationError, ListingChangeResponseSchema]]:
    """Listing Change

    Args:
        start_date (datetime.datetime):
        end_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListingChangeResponseSchema]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> Optional[Union[HTTPValidationError, ListingChangeResponseSchema]]:
    """Listing Change

    Args:
        start_date (datetime.datetime):
        end_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListingChangeResponseSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
