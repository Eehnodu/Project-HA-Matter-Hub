"""Demo fan platform that implements on/off functionality."""

from __future__ import annotations

import asyncio
from typing import Any

from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.const import STATE_ON, STATE_OFF
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

ON_OFF_DELAY = 2


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the Demo fan platform."""
    if discovery_info is None:
        return

    async_add_entities(
        [
            FakeFan("FaKeFan1", "Fan1", is_on=False),
            FakeFan("FaKeFan2", "Fan2", is_on=False),
            FakeFan("FaKeFan3", "Fan3", is_on=False),
            FakeFan("FaKeFan4", "Fan4", is_on=False),
            FakeFan("FaKeFan5", "Fan5", is_on=False),
            FakeFan("FaKeFan6", "Fan6", is_on=False),
            FakeFan("FaKeFan7", "Fan7", is_on=False),
            FakeFan("FaKeFan8", "Fan8", is_on=False),
        ]
    )


class FakeFan(FanEntity):
    """Representation of a Fake fan."""

    _attr_should_poll = False

    def __init__(self, unique_id: str, name: str, is_on: bool = False) -> None:
        """Initialize the fan."""
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._state = STATE_ON if is_on else STATE_OFF
        self._attr_supported_features = (
            FanEntityFeature.TURN_ON | FanEntityFeature.TURN_OFF
        )

    @property
    def is_on(self) -> bool:
        """Return true if the fan is on."""
        return self._state == STATE_ON

    async def async_turn_on(
        self,
        percentage: int | None = None,
        preset_mode: str | None = None,
        **kwargs: Any,
    ) -> None:
        """Turn on the fan."""
        self._state = STATE_ON
        self.async_write_ha_state()
        await asyncio.sleep(ON_OFF_DELAY)
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off the fan."""
        self._state = STATE_OFF
        self.async_write_ha_state()
        await asyncio.sleep(ON_OFF_DELAY)
        self.async_write_ha_state()

    @property
    def state(self) -> str:
        """Return the state of the fan."""
        return self._state
