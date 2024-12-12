"""Base entity for IronOS integration."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH, DeviceInfo
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import MANUFACTURER, MODEL
from .coordinator import IronOSBaseCoordinator


class IronOSBaseEntity(CoordinatorEntity[IronOSBaseCoordinator]):
    """Base IronOS entity."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: IronOSBaseCoordinator,
        entity_description: EntityDescription,
        context: Any | None = None,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, context=context)

        self.entity_description = entity_description
        self._attr_unique_id = (
            f"{coordinator.config_entry.unique_id}_{entity_description.key}"
        )
        if TYPE_CHECKING:
            assert coordinator.config_entry.unique_id
        self.device_info = DeviceInfo(
            connections={(CONNECTION_BLUETOOTH, coordinator.config_entry.unique_id)},
            manufacturer=MANUFACTURER,
            model=MODEL,
            name="Pinecil",
            sw_version=coordinator.device_info.build,
            serial_number=f"{coordinator.device_info.device_sn} (ID:{coordinator.device_info.device_id})",
        )