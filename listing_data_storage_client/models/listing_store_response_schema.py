from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingStoreResponseSchema")


@_attrs_define
class ListingStoreResponseSchema:
    """
    Attributes:
        code (Union[Unset, int]): Response code. Default: 200.
        status (Union[Unset, str]): Response message. Default: 'OK'.
    """

    code: Union[Unset, int] = 200
    status: Union[Unset, str] = "OK"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        status = d.pop("status", UNSET)

        listing_store_response_schema = cls(
            code=code,
            status=status,
        )

        listing_store_response_schema.additional_properties = d
        return listing_store_response_schema

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
