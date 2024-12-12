from __future__ import annotations

import asyncio
from typing import Any

from homeassistant.components.alarm_control_panel import (
    AlarmControlPanelEntity,
    AlarmControlPanelState,
    AlarmControlPanelEntityFeature,
)
from homeassistant.exceptions import ServiceValidationError
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the alarm control panel platform."""
    async_add_entities(
        [
            CustomAlarmControlPanel("FakeAlarm1", "Alarm1", "1234"),
            CustomAlarmControlPanel("FakeAlarm2", "Alarm2", "1234"),
            CustomAlarmControlPanel("FakeAlarm3", "Alarm3", "1234"),
            CustomAlarmControlPanel("FakeAlarm4", "Alarm4", "1234"),
            CustomAlarmControlPanel("FakeAlarm5", "Alarm5", "1234"),
            CustomAlarmControlPanel("FakeAlarm6", "Alarm6", "1234"),
            CustomAlarmControlPanel("FakeAlarm7", "Alarm7", "1234"),
            CustomAlarmControlPanel("FakeAlarm8", "Alarm8", "1234"),
        ]
    )


class CustomAlarmControlPanel(AlarmControlPanelEntity):
    """A custom implementation of an alarm control panel."""

    _attr_should_poll = False
    _attr_code_arm_required = True  # Require a code for arming actions
    _attr_code_format = "NUMBER"  # Enable numeric keypad
    _attr_supported_features = (
        AlarmControlPanelEntityFeature.ARM_AWAY
        | AlarmControlPanelEntityFeature.ARM_HOME
    )

    def __init__(self, unique_id: str, name: str, default_code: str | None = None):
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._attr_alarm_state = AlarmControlPanelState.DISARMED
        self._default_code = default_code

    @callback
    def code_or_default_code(self, code: str | None) -> str | None:
        """Return the provided code or the default code."""
        if code:
            return code
        return self._default_code

    @callback
    def check_code_arm_required(self, code: str | None) -> str | None:
        """Verify if the code is required for arming."""
        _code = self.code_or_default_code(code)
        if not _code and self.code_arm_required:
            raise ServiceValidationError(
                translation_domain="homeassistant",
                translation_key="code_arm_required",
                translation_placeholders={"entity_id": self.entity_id},
            )
        return _code

    @property
    def alarm_state(self) -> AlarmControlPanelState:
        """Return the current alarm state."""
        return self._attr_alarm_state

    async def async_alarm_disarm(self, code: str | None = None) -> None:
        """Disarm the alarm."""
        if code != self._default_code:
            raise ServiceValidationError("Invalid disarm code")
        self._attr_alarm_state = AlarmControlPanelState.DISARMED
        self.async_write_ha_state()

    async def async_alarm_arm_away(self, code: str | None = None) -> None:
        """Arm the alarm in away mode."""
        self.check_code_arm_required(code)
        self._attr_alarm_state = AlarmControlPanelState.ARMED_AWAY
        self.async_write_ha_state()

    async def async_alarm_arm_home(self, code: str | None = None) -> None:
        """Arm the alarm in home mode."""
        self.check_code_arm_required(code)
        self._attr_alarm_state = AlarmControlPanelState.ARMED_HOME
        self.async_write_ha_state()
