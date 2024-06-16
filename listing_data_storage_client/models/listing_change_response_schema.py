from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.listing_schema import ListingSchema


T = TypeVar("T", bound="ListingChangeResponseSchema")


@_attrs_define
class ListingChangeResponseSchema:
    """
    Attributes:
        added (List['ListingSchema']): List of added listings.
        removed (List['ListingSchema']): List of removed listing IDs.
    """

    added: List["ListingSchema"]
    removed: List["ListingSchema"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        added = []
        for added_item_data in self.added:
            added_item = added_item_data.to_dict()
            added.append(added_item)

        removed = []
        for removed_item_data in self.removed:
            removed_item = removed_item_data.to_dict()
            removed.append(removed_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_schema import ListingSchema

        d = src_dict.copy()
        added = []
        _added = d.pop("added")
        for added_item_data in _added:
            added_item = ListingSchema.from_dict(added_item_data)

            added.append(added_item)

        removed = []
        _removed = d.pop("removed")
        for removed_item_data in _removed:
            removed_item = ListingSchema.from_dict(removed_item_data)

            removed.append(removed_item)

        listing_change_response_schema = cls(
            added=added,
            removed=removed,
        )

        listing_change_response_schema.additional_properties = d
        return listing_change_response_schema

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
