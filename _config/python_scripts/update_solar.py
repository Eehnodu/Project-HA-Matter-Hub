solar_power_entities = [
    "sensor.tia_fake_hub_fake_solar_power_sensor1",
    "sensor.tia_fake_hub_fake_solar_power_sensor2",
    "sensor.tia_fake_hub_fake_solar_power_sensor3",
    "sensor.tia_fake_hub_fake_solar_power_sensor4",
]

solar_ampere_entities = [
    "sensor.tia_fake_hub_fake_solar_ampere_sensor1",
    "sensor.tia_fake_hub_fake_solar_ampere_sensor2",
    "sensor.tia_fake_hub_fake_solar_ampere_sensor3",
    "sensor.tia_fake_hub_fake_solar_ampere_sensor4",
]


def update_power_entity(entity_id, value_range):
    new_value = round(random.uniform(value_range[0], value_range[1]), 2)
    hass.states.set(entity_id, new_value, attributes={"unit_of_measurement": "kW"})
    return new_value


def update_ampere_entity(ampere_entity_id, power_entity_id, voltage=48):
    power_state = hass.states.get(power_entity_id)
    if power_state:
        power_value = float(power_state.state)
        ampere_value = (power_value * 1000) / voltage
        hass.states.set(
            ampere_entity_id, ampere_value, attributes={"unit_of_measurement": "A"}
        )


for power_entity_id in solar_power_entities:
    update_power_entity(power_entity_id, (10, 50))

for ampere_entity_id, power_entity_id in zip(
    solar_ampere_entities, solar_power_entities
):
    update_ampere_entity(ampere_entity_id, power_entity_id)
