from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.listing_schema import ListingSchema


T = TypeVar("T", bound="GetViewResponseSchema")


@_attrs_define
class GetViewResponseSchema:
    """
    Attributes:
        listings (List['ListingSchema']):
    """

    listings: List["ListingSchema"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listings = []
        for listings_item_data in self.listings:
            listings_item = listings_item_data.to_dict()
            listings.append(listings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listings": listings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_schema import ListingSchema

        d = src_dict.copy()
        listings = []
        _listings = d.pop("listings")
        for listings_item_data in _listings:
            listings_item = ListingSchema.from_dict(listings_item_data)

            listings.append(listings_item)

        get_view_response_schema = cls(
            listings=listings,
        )

        get_view_response_schema.additional_properties = d
        return get_view_response_schema

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
