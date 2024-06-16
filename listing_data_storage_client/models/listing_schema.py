from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListingSchema")


@_attrs_define
class ListingSchema:
    """Listing schema.

    Attributes:
        listing_id (str): Unique identifier for the listing.
        section (str): Section where the seat is located.
        row (str): Row in which the seat is positioned.
        quantity (int): Max number of tickets available for that section/row combination.
        face_value (float): FaceValue for each ticket in listing.
        total_price (float): Total price with fees.
        seat_numbers (List[str]): Sequential numbers of the seats.
        description (str): Textual description of the listing.
        attributes (List[str]): Additional characteristics or features of the listing.
        split_type (str): Type of splitting allowed for the listing.
        custom_split (List[List[int]]): Custom optional splits available for purchase Example: [[0, 1], [1, 2]].
    """

    listing_id: str
    section: str
    row: str
    quantity: int
    face_value: float
    total_price: float
    seat_numbers: List[str]
    description: str
    attributes: List[str]
    split_type: str
    custom_split: List[List[int]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listing_id = self.listing_id

        section = self.section

        row = self.row

        quantity = self.quantity

        face_value = self.face_value

        total_price = self.total_price

        seat_numbers = self.seat_numbers

        description = self.description

        attributes = self.attributes

        split_type = self.split_type

        custom_split = []
        for custom_split_item_data in self.custom_split:
            custom_split_item = custom_split_item_data

            custom_split.append(custom_split_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listingId": listing_id,
                "section": section,
                "row": row,
                "quantity": quantity,
                "faceValue": face_value,
                "totalPrice": total_price,
                "seatNumbers": seat_numbers,
                "description": description,
                "attributes": attributes,
                "splitType": split_type,
                "customSplit": custom_split,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        listing_id = d.pop("listingId")

        section = d.pop("section")

        row = d.pop("row")

        quantity = d.pop("quantity")

        face_value = d.pop("faceValue")

        total_price = d.pop("totalPrice")

        seat_numbers = cast(List[str], d.pop("seatNumbers"))

        description = d.pop("description")

        attributes = cast(List[str], d.pop("attributes"))

        split_type = d.pop("splitType")

        custom_split = []
        _custom_split = d.pop("customSplit")
        for custom_split_item_data in _custom_split:
            custom_split_item = cast(List[int], custom_split_item_data)

            custom_split.append(custom_split_item)

        listing_schema = cls(
            listing_id=listing_id,
            section=section,
            row=row,
            quantity=quantity,
            face_value=face_value,
            total_price=total_price,
            seat_numbers=seat_numbers,
            description=description,
            attributes=attributes,
            split_type=split_type,
            custom_split=custom_split,
        )

        listing_schema.additional_properties = d
        return listing_schema

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
