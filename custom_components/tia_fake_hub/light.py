from homeassistant.components.light import (
    LightEntity,
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
import asyncio
from typing import Any


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    if discovery_info is None:
        return

    async_add_entities(
        [
            FakeLight("FakeLight1", "Light1", False, 128, (0, 255, 0)),
            FakeLight("FakeLight2", "Light2", False, 128, (0, 255, 0)),
            FakeLight("FakeLight3", "Light3", False, 128, (0, 255, 0)),
            FakeLight("FakeLight4", "Light4", False, 128, (255, 0, 0)),
            FakeLight("FakeLight5", "Light5", False, 128, (255, 0, 0)),
            FakeLight("FakeLight6", "Light6", False, 128, (255, 0, 0)),
            FakeLight("FakeLight7", "Light7", False, 128, (255, 0, 0)),
            FakeLight("FakeLight8", "Light8", False, 128, (255, 0, 0)),
        ]
    )


class FakeLight(LightEntity):
    _attr_should_poll = False

    def __init__(
        self,
        unique_id: str,
        name: str,
        state: bool,
        brightness: int = 255,
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._state = state
        self._brightness = brightness
        self._color = color
        # Set supported features based on the functionality
        self._attr_supported_features = SUPPORT_BRIGHTNESS | SUPPORT_COLOR

    @property
    def is_on(self) -> bool:
        return self._state

    @property
    def brightness(self) -> int:
        return self._brightness

    @property
    def rgb_color(self) -> tuple[int, int, int]:
        return self._color

    async def async_turn_on(self, **kwargs: Any) -> None:
        self._state = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        self._state = False
        self.async_write_ha_state()

    async def async_set_brightness(self, brightness: int, **kwargs: Any) -> None:
        self._brightness = brightness
        self.async_write_ha_state()

    async def async_set_color(self, color: tuple[int, int, int], **kwargs: Any) -> None:
        self._color = color
        self.async_write_ha_state()
