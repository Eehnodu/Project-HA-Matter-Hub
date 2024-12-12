"""Demo lock platform that implements locks."""

from __future__ import annotations

import asyncio
from typing import Any

from homeassistant.components.lock import LockEntity, LockEntityFeature, LockState
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

LOCK_UNLOCK_DELAY = 2  # Used to give a realistic lock/unlock experience in frontend


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the Demo config entry."""
    if discovery_info is None:
        return

    async_add_entities(
        [
            FakeLock("FrontDoor", "Front Door", LockState.LOCKED),
            FakeLock("BackDoor", "Back Door", LockState.UNLOCKED),
            FakeLock(
                "PoorlyInstalledDoor",
                "Poorly Installed Door",
                LockState.UNLOCKED,
                False,
                True,
            ),
            FakeLock("OpenableLock", "Openable Lock", LockState.LOCKED, True),
            FakeLock("FakeLock1", "Front Lock1", LockState.LOCKED),
            FakeLock("FakeLock2", "Front Lock2", LockState.LOCKED),
            FakeLock("FakeLock3", "Front Lock3", LockState.LOCKED),
            FakeLock("FakeLock4", "Back Lock1", LockState.LOCKED),
            FakeLock("FakeLock5", "Left Lock1", LockState.LOCKED),
            FakeLock("FakeLock6", "Left Lock2", LockState.LOCKED),
            FakeLock("FakeLock7", "Right Lock1", LockState.LOCKED),
            FakeLock("FakeLock8", "Right Lock2", LockState.LOCKED),
            FakeLock("FakeLock9", "In Gate1", LockState.LOCKED),
            FakeLock("FakeLock10", "In Gate2", LockState.LOCKED),
            FakeLock("FakeLock11", "Out Gate1", LockState.LOCKED),
            FakeLock("FakeLock12", "Out Gate2", LockState.LOCKED),
        ]
    )


class FakeLock(LockEntity):
    """Representation of a Fake lock."""

    _attr_should_poll = False

    def __init__(
        self,
        unique_id: str,
        name: str,
        state: str,
        openable: bool = False,
        jam_on_operation: bool = False,
    ) -> None:
        """Initialize the lock."""
        self._attr_unique_id = unique_id
        self._attr_name = name
        if openable:
            self._attr_supported_features = LockEntityFeature.OPEN
        self._state = state
        self._openable = openable
        self._jam_on_operation = jam_on_operation

    @property
    def is_locking(self) -> bool:
        """Return true if lock is locking."""
        return self._state == LockState.LOCKING

    @property
    def is_unlocking(self) -> bool:
        """Return true if lock is unlocking."""
        return self._state == LockState.UNLOCKING

    @property
    def is_jammed(self) -> bool:
        """Return true if lock is jammed."""
        return self._state == LockState.JAMMED

    @property
    def is_locked(self) -> bool:
        """Return true if lock is locked."""
        return self._state == LockState.LOCKED

    @property
    def is_open(self) -> bool:
        """Return true if lock is open."""
        return self._state == LockState.OPEN

    @property
    def is_opening(self) -> bool:
        """Return true if lock is opening."""
        return self._state == LockState.OPENING

    async def async_lock(self, **kwargs: Any) -> None:
        """Lock the device."""
        self._state = LockState.LOCKING
        self.async_write_ha_state()
        await asyncio.sleep(LOCK_UNLOCK_DELAY)
        if self._jam_on_operation:
            self._state = LockState.JAMMED
        else:
            self._state = LockState.LOCKED
        self.async_write_ha_state()

    async def async_unlock(self, **kwargs: Any) -> None:
        """Unlock the device."""
        self._state = LockState.UNLOCKING
        self.async_write_ha_state()
        await asyncio.sleep(LOCK_UNLOCK_DELAY)
        self._state = LockState.UNLOCKED
        self.async_write_ha_state()

    async def async_open(self, **kwargs: Any) -> None:
        """Open the door latch."""
        self._state = LockState.OPENING
        self.async_write_ha_state()
        await asyncio.sleep(LOCK_UNLOCK_DELAY)
        self._state = LockState.OPEN
        self.async_write_ha_state()
