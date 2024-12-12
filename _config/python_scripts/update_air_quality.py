air_quality_entities = ["air_quality.air_quality1", "air_quality.air_quality2"]


def update_entity(entity_id, value_range):
    new_value = random.randint(value_range[0], value_range[1])
    icon = "mdi:air-filter"
    hass.states.set(
        entity_id, new_value, attributes={"unit_of_measurement": "µg/m³", "icon": icon}
    )


for entity_id in air_quality_entities:
    update_entity(entity_id, (10, 90))
