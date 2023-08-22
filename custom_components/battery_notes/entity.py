"""BatteryTypesEntity class."""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME, VERSION
from .coordinator import BatteryTypesDataUpdateCoordinator


class BatteryTypesEntity(CoordinatorEntity):
    """BatteryTypesEntity class."""

    def __init__(self, coordinator: BatteryTypesDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self.unique_id)},
            name=NAME,
            model=VERSION,
            manufacturer=NAME,
        )