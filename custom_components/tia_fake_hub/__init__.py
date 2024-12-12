"""Example Load Platform integration."""

from __future__ import annotations

from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "tia_fake_hub"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Your controller/hub specific code."""
    # Data that you want to share with your platforms
    hass.data[DOMAIN] = {"temperature": 23}

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(Platform.SENSOR, DOMAIN, {}, config)
    )

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(Platform.LOCK, DOMAIN, {}, config)
    )

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(Platform.FAN, DOMAIN, {}, config)
    )

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(Platform.SWITCH, DOMAIN, {}, config)
    )

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(Platform.LIGHT, DOMAIN, {}, config)
    )

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(
            Platform.ALARM_CONTROL_PANEL, DOMAIN, {}, config
        )
    )

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(
            Platform.AIR_QUALITY, DOMAIN, {}, config
        )
    )

    return True
