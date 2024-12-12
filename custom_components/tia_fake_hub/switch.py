from __future__ import annotations

import asyncio
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.const import STATE_ON, STATE_OFF
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the fake switch switch platform."""
    if discovery_info is None:
        return

    async_add_entities(
        [
            FakeSprinkler(
                "FakeSprinkler1", "Celling Sprinkler1", "mdi:sprinkler-fire", False
            ),
            FakeSprinkler(
                "FakeSprinkler2", "Celling Sprinkler2", "mdi:sprinkler-fire", False
            ),
            FakeSprinkler("FakeSprinkler3", "Side Sprinkler1", "mdi:sprinkler", False),
            FakeSprinkler("FakeSprinkler4", "Side Sprinkler2", "mdi:sprinkler", False),
            FakeSprinkler(
                "FakeSprinkler5", "Sprinkler1", "mdi:sprinkler-variant", False
            ),
            FakeSprinkler(
                "FakeSprinkler6", "Sprinkler2", "mdi:sprinkler-variant", False
            ),
            FakeSprinkler(
                "Fake_Line2_Sensor1",
                "Line2_Sensor1",
                "mdi:lightning-bolt-outline",
                False,
            ),
            FakeSprinkler(
                "Fake_Line2_Sensor2",
                "Line2_Sensor2",
                "mdi:lightning-bolt-outline",
                False,
            ),
            FakeSprinkler("Fake_Line2_Sensor3", "Line2_Sensor3", "mdi:remote", False),
            FakeSprinkler("Fake_Line2_Sensor4", "Line2_Sensor4", "mdi:remote", False),
            FakeSprinkler(
                "Fake_Line2_Sensor5", "Line2_Sensor5", "mdi:engine-outline", False
            ),
            FakeSprinkler(
                "Fake_Line2_Sensor6", "Line2_Sensor6", "mdi:engine-outline", False
            ),
            FakeSprinkler("Fake_in_sensor1", "in_sensor1", "mdi:switch", False),
            FakeSprinkler("Fake_in_sensor2", "in_sensor2", "mdi:switch", False),
            FakeSprinkler("Fake_in_sensor3", "in_sensor3", "mdi:boom-gate-up", False),
            FakeSprinkler("Fake_in_sensor4", "in_sensor4", "mdi:video", False),
            FakeSprinkler("Fake_out_sensor1", "out_sensor1", "mdi:switch", False),
            FakeSprinkler("Fake_out_sensor2", "out_sensor2", "mdi:switch", False),
            FakeSprinkler("Fake_out_sensor3", "out_sensor3", "mdi:boom-gate-up", False),
            FakeSprinkler("Fake_out_sensor4", "out_sensor4", "mdi:video", False),
        ]
    )


class FakeSprinkler(SwitchEntity):
    """Representation of a Fake switch."""

    _attr_should_poll = False

    def __init__(
        self, unique_id: str, name: str, icon: str, is_on: bool = False
    ) -> None:
        """Initialize the switch."""
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._icon = icon
        self._state = STATE_ON if is_on else STATE_OFF

    @property
    def is_on(self) -> bool:
        """Return true if the switch is on."""
        return self._state == STATE_ON

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn on the switch."""
        self._state = STATE_ON
        self.async_write_ha_state()
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off the switch."""
        self._state = STATE_OFF
        self.async_write_ha_state()
        self.async_write_ha_state()

    @property
    def state(self) -> str:
        """Return the state of the switch."""
        return self._state

    @property
    def icon(self) -> str:
        """Return the icon for the switch."""
        return self._icon
