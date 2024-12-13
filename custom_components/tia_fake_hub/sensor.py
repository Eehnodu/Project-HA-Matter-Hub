"""Platform for sensor integration."""

from __future__ import annotations

from random import randint, uniform
from datetime import datetime, timedelta
from typing import cast

from homeassistant.components.sensor import (
    DOMAIN as SENSOR_DOMAIN,
    RestoreSensor,
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import (
    ATTR_BATTERY_LEVEL,
    CONCENTRATION_PARTS_PER_MILLION,
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfIrradiance,
    UnitOfVolume,
    UnitOfPower,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfFrequency,
)


from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.event import async_track_time_interval

from . import DOMAIN


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return

    temperature_sensors = [
        FakeSensor(
            f"temperature{i+1}",
            "Outside Temperature",
            round(uniform(10, 30), 1),
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            UnitOfTemperature.CELSIUS,
            round(randint(10, 100), 0),
        )
        for i in range(4)
    ]

    line1_sensors = [
        FakeSensor(
            f"Line1_CO_{i+1}",
            "carbon_monoxide",
            round(uniform(10, 30), 0),
            SensorDeviceClass.CO,
            SensorStateClass.MEASUREMENT,
            CONCENTRATION_PARTS_PER_MILLION,
            round(randint(10, 100), 0),
        )
        for i in range(12)
    ] + [
        FakeSensor(
            f"Line1_CO2_{i+1}",
            "carbon_dioxide",
            round(uniform(300, 800), 0),
            SensorDeviceClass.CO2,
            SensorStateClass.MEASUREMENT,
            CONCENTRATION_PARTS_PER_MILLION,
            round(randint(10, 100), 0),
        )
        for i in range(12)
    ]

    line2_sensors = [
        FakeSensor(
            f"Line2_CO_{i+1}",
            "carbon_monoxide",
            round(uniform(10, 30), 0),
            SensorDeviceClass.CO,
            SensorStateClass.MEASUREMENT,
            CONCENTRATION_PARTS_PER_MILLION,
            round(randint(10, 100), 0),
        )
        for i in range(7)
    ] + [
        FakeSensor(
            f"Line2_CO2_{i+1}",
            "carbon_dioxide",
            round(uniform(300, 800), 0),
            SensorDeviceClass.CO2,
            SensorStateClass.MEASUREMENT,
            CONCENTRATION_PARTS_PER_MILLION,
            round(randint(10, 100), 0),
        )
        for i in range(7)
    ]

    fake_solar_sensors = [
        # solar
        FakeSensor(
            "fake_solar_power_sensor1",
            "fake solar power energy1",
            18.03,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_solar_power_sensor2",
            "fake solar power energy2",
            24.16,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_solar_power_sensor3",
            "fake solar power energy3",
            29.8,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_solar_power_sensor4",
            "fake solar power energy4",
            17.96,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_solar_voltage_sensor1",
            "fake solar voltage energy1",
            48,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            None,
        ),
        FakeSensor(
            "fake_solar_voltage_sensor2",
            "fake solar voltage energy2",
            48,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            None,
        ),
        FakeSensor(
            "fake_solar_voltage_sensor3",
            "fake solar voltage energy3",
            48,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            None,
        ),
        FakeSensor(
            "fake_solar_voltage_sensor4",
            "fake solar voltage energy4",
            48,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            None,
        ),
        FakeSensor(
            "fake_solar_ampere_sensor1",
            "fake solar ampere energy1",
            375.63,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            None,
        ),
        FakeSensor(
            "fake_solar_ampere_sensor2",
            "fake solar ampere energy2",
            503.33,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            None,
        ),
        FakeSensor(
            "fake_solar_ampere_sensor3",
            "fake solar ampere energy3",
            620.83,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            None,
        ),
        FakeSensor(
            "fake_solar_ampere_sensor4",
            "fake solar ampere energy4",
            374.58,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            None,
        ),
    ]

    fake_battery_sensors = [
        FakeSensor(
            "fake_battery_power_sensor",
            "fake_battery_power",
            74.6,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfEnergy.KILO_WATT_HOUR,
            None,
        ),
        FakeSensor(
            "fake_battery_ampere_sensor",
            "fake_battery_ampere",
            1558.33,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            None,
        ),
        FakeSensor(
            "fake_battery_voltage_sensor",
            "fake_battery_voltage",
            48,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            None,
        ),
        FakeSensor(
            "fake_battery_battery_temperature",
            "fake_battery_voltage",
            18.3,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfTemperature.CELSIUS,
            None,
        ),
    ]

    fake_temp_sensors = [
        FakeSensor(
            "fake_radiator_temperature_sensor",
            "fake_radiator_temperature_sensor",
            21.3,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfTemperature.CELSIUS,
            None,
        ),
        FakeSensor(
            "fake_dc_transformer_temperature_sensor",
            "fake_dc_transformer_temperature_sensor",
            19.2,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfTemperature.CELSIUS,
            None,
        ),
    ]

    fake_aux_sensors = [
        FakeSensor(
            "fake_aux_1",
            "Fake Aux 1",
            31.84,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_aux_2",
            "Fake Aux 2",
            23.61,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_aux_1_extra",
            "Fake Aux 1 Extra",
            13.58,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_aux_2_extra",
            "Fake Aux 2 Extra",
            6.31,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_sunsynk_aux_power",
            "Fake Aux Power",
            74.92,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
    ]

    fake_load_sensors = [
        FakeSensor(
            "fake_load1_power",
            "Fake Load1 Pover",
            52.71,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSensor(
            "fake_load2_power",
            "Fake Load2 Pover",
            25.83,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
    ]

    fake_energy_sensor = [
        FakeSumSensor(
            "fake_total_solar_sensor1",
            "fake total solar energy ",
            100,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfEnergy.KILO_WATT_HOUR,
            None,
        ),
        FakeSumSensor(
            "fake_total_solar_sensor2",
            "fake total solar energy 2",
            0.00025,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfEnergy.MEGA_WATT_HOUR,
            None,
        ),
        FakeSumSensor(
            "fake_total_gas_sensor1",
            "Fake Total gas 1",
            0.025,  # 0.30 m³/h (10.6 ft³ / h)
            SensorDeviceClass.GAS,
            SensorStateClass.TOTAL,
            UnitOfVolume.CUBIC_METERS,
            None,
        ),
        FakeSumSensor(
            "fake_total_gas_sensor2",
            "Fake Total gas 2",
            1.0,  # 12 ft³/h (0.34 m³ / h)
            SensorDeviceClass.GAS,
            SensorStateClass.TOTAL,
            UnitOfVolume.CUBIC_FEET,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_day_load_energy",
            "Fake Day Load Energy",
            10.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_grid_ct_power",
            "Fake Grid Ct Power",
            20.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSumSensor(
            "fake_tibber_energy_cost_buy",
            "Fake Tibber Energy Cost Buy",
            1420.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfPower.WATT,
            None,
        ),
        FakeSumSensor(
            "fake_nonessential1_power",
            "Fake Nonessential1 Power",
            5.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSumSensor(
            "fake_nonessential2_power",
            "Fake Nonessential2 Power",
            7.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_inverter_power",
            "Fake Inverter Power",
            7000.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfPower.WATT,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_inverter_current",
            "Fake Inverter Current",
            300.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfElectricCurrent.AMPERE,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_inverter_voltage",
            "Fake Inverter Voltage",
            700.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfElectricPotential.VOLT,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_load_frequency",
            "Fake Load Frequency",
            250.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfFrequency.HERTZ,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_grid_power",
            "Fake Grid Power",
            7000.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.WATT,
            None,
        ),
        FakeSumSensor(
            "fake_tuya_geyser_current_consumption",
            "Fake Current Consumption",
            5000.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.WATT,
            None,
        ),
        FakeSumSensor(
            "fake_day_grid_export",
            "Fake Day Grid Export",
            40.00,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        FakeSumSensor(
            "fake_day_grid_import",
            "Fake Day Grid Import",
            26.00,
            SensorDeviceClass.ENERGY,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.KILO_WATT,
            None,
        ),
        # battery
        FakeSumSensor(
            "fake_total_battery_charge",
            "fake total battery charge",
            50.34,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfEnergy.KILO_WATT_HOUR,
            None,
        ),
        FakeSumSensor(
            "fake_total_battery_discharge",
            "fake total battery discharge",
            25.72,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfEnergy.KILO_WATT_HOUR,
            None,
        ),
        FakeSumSensor(
            "fake_battery_soc_sensor",
            "fake_battery_soc",
            3,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            PERCENTAGE,
            None,
        ),
        FakeSumSensor(
            "fake_sunsynk_day_aux_energy",
            "Fake Day Aux Energy",
            100.0,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL,
            UnitOfPower.KILO_WATT,
            None,
        ),
    ]

    async_add_entities(
        line1_sensors
        + line2_sensors
        + temperature_sensors
        + fake_energy_sensor
        + fake_solar_sensors
        + fake_battery_sensors
        + fake_temp_sensors
        + fake_aux_sensors
        + fake_load_sensors
    )


class ExampleSensor(SensorEntity):
    """Representation of a sensor."""

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return "Temperature33"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return UnitOfTemperature.CELSIUS

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = self.hass.data[DOMAIN]["temperature"]


class FakeSensor(SensorEntity):
    """Reperesentation of a Fake sensor."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_should_poll = False

    def __init__(
        self,
        unique_id: str,
        device_name: str | None,
        state: float | str | None,
        devcie_class: SensorDeviceClass,
        state_class: SensorStateClass | None,
        unit_of_measurement: str | None,
        battery: int | None,
        options: list[str] | None = None,
        translatiopn_key: str | None = None,
    ) -> None:
        """Initialize the sensor."""
        self._attr_device_class = devcie_class
        self._attr_native_unit_of_measurement = unit_of_measurement
        self._attr_native_value = state
        self._attr_state_class = state_class
        self._attr_unique_id = unique_id
        self._attr_options = options
        self._attr_translation_key = translatiopn_key

        self._attr_devce_info = DeviceInfo(
            identifiers={(DOMAIN, unique_id)},
            name=device_name,
        )

        if battery:
            self._attr_extra_state_attributes = {ATTR_BATTERY_LEVEL: battery}


class FakeSumSensor(RestoreSensor):
    """Representation of a Fake sensor."""

    _attr_should_poll = False
    _attr_native_value: float

    def __init__(
        self,
        unique_id: str,
        device_name: str,
        five_minute_increase: float,
        device_class: SensorDeviceClass,
        state_class: SensorStateClass | None,
        unit_of_measurement: str | None,
        battery: int | None,
    ) -> None:
        """Initialize the sensor."""
        self.entity_id = f"{DOMAIN}.{unique_id}"
        self._attr_device_class = device_class
        self._attr_native_unit_of_measurement = unit_of_measurement
        self._attr_native_value = 0
        self._attr_state_class = state_class
        self._attr_unique_id = unique_id
        self._five_minute_increase = five_minute_increase

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, unique_id)},
            name=device_name,
        )

        if battery:
            self._attr_extra_state_attributes = {ATTR_BATTERY_LEVEL: battery}

    @callback
    def _async_bump_sum(self, now: datetime) -> None:
        """Bump the sum."""
        if self._attr_native_unit_of_measurement == PERCENTAGE:
            self._attr_native_value = min(
                self._attr_native_value + self._five_minute_increase, 100
            )
        else:
            self._attr_native_value += self._five_minute_increase

        self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        """Call when entity about to be added to hass."""
        await super().async_added_to_hass()
        state = await self.async_get_last_sensor_data()
        if state:
            self._attr_native_value = cast(float, state.native_value)

        self.async_on_remove(
            async_track_time_interval(
                self.hass, self._async_bump_sum, timedelta(minutes=5)
            ),
        )
