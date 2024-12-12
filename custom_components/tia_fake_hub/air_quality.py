from __future__ import annotations

import asyncio
from typing import Any, final

from homeassistant.components.air_quality import AirQualityEntity
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType, StateType


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the Demo air quality platform."""
    if discovery_info is None:
        return

    async_add_entities(
        [
            FakeAirQuality(unique_id="FakeAirQuality", name="Air Quality1"),
            FakeAirQuality(unique_id="DemoAirquality", name="Air Quality2"),
        ]
    )


class FakeAirQuality(AirQualityEntity):
    """Representation of a Fake air_quality sensor."""

    _attr_should_poll = False

    def __init__(self, unique_id: str, name: str) -> None:
        """Initialize the fake air quality sensor."""
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._co2 = 400.0
        self._co = 0.5

    @property
    def carbon_dioxide(self) -> StateType:
        """Return the CO2 (carbon dioxide) level."""
        return self._co2

    @property
    def carbon_monoxide(self) -> StateType:
        """Return the CO (carbon monoxide) level."""
        return self._co

    @final
    @property
    def state_attributes(self) -> dict[str, str | int | float]:
        """Return the state attributes."""
        data: dict[str, str | int | float] = {}

        if (value := self.carbon_dioxide) is not None:
            data["carbon_dioxide"] = value

        if (value := self.carbon_monoxide) is not None:
            data["carbon_monoxide"] = value

        return data

    @property
    def state(self) -> StateType:
        """Return the current state (CO2 or CO)."""
        return self.carbon_dioxide

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
