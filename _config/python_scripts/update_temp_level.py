temp_entities = [
    "sensor.tia_fake_hub_temperature1",
    "sensor.tia_fake_hub_temperature2",
    "sensor.tia_fake_hub_temperature3",
]


def get_icon(entity_id: str) -> str:
    return "mdi:thermometer"


def update_entity(entity_id, value_range):
    new_value = random.randint(value_range[0], value_range[1])
    unit_of_measurement = "°C"
    icon = get_icon(entity_id)

    hass.states.set(
        entity_id,
        new_value,
        attributes={"unit_of_measurement": unit_of_measurement, "icon": icon},
    )


for entity_id in temp_entities:
    update_entity(entity_id, (10, 80))
