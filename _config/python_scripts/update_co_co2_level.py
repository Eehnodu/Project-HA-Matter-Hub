co2_entities = [
    "sensor.tia_fake_hub_line1_co2_1",
    "sensor.tia_fake_hub_line1_co2_2",
    "sensor.tia_fake_hub_line1_co2_3",
    "sensor.tia_fake_hub_line1_co2_4",
    "sensor.tia_fake_hub_line1_co2_5",
    "sensor.tia_fake_hub_line1_co2_6",
    "sensor.tia_fake_hub_line1_co2_7",
    "sensor.tia_fake_hub_line1_co2_8",
    "sensor.tia_fake_hub_line1_co2_9",
    "sensor.tia_fake_hub_line1_co2_10",
    "sensor.tia_fake_hub_line1_co2_11",
    "sensor.tia_fake_hub_line1_co2_12",
    "sensor.tia_fake_hub_line2_co2_1",
    "sensor.tia_fake_hub_line2_co2_2",
    "sensor.tia_fake_hub_line2_co2_3",
    "sensor.tia_fake_hub_line2_co2_4",
    "sensor.tia_fake_hub_line2_co2_5",
    "sensor.tia_fake_hub_line2_co2_6",
    "sensor.tia_fake_hub_line2_co2_7",
]

co_entities = [
    "sensor.tia_fake_hub_line1_co_1",
    "sensor.tia_fake_hub_line1_co_2",
    "sensor.tia_fake_hub_line1_co_3",
    "sensor.tia_fake_hub_line1_co_4",
    "sensor.tia_fake_hub_line1_co_5",
    "sensor.tia_fake_hub_line1_co_6",
    "sensor.tia_fake_hub_line1_co_7",
    "sensor.tia_fake_hub_line1_co_8",
    "sensor.tia_fake_hub_line1_co_9",
    "sensor.tia_fake_hub_line1_co_10",
    "sensor.tia_fake_hub_line1_co_11",
    "sensor.tia_fake_hub_line1_co_12",
    "sensor.tia_fake_hub_line2_co_1",
    "sensor.tia_fake_hub_line2_co_2",
    "sensor.tia_fake_hub_line2_co_3",
    "sensor.tia_fake_hub_line2_co_4",
    "sensor.tia_fake_hub_line2_co_5",
    "sensor.tia_fake_hub_line2_co_6",
    "sensor.tia_fake_hub_line2_co_7",
]


def get_icon(entity_id: str) -> str:
    if "co2" in entity_id.lower():
        return "mdi:molecule-co2"
    return "mdi:molecule-co"


def update_entity(entity_id, value_range):
    new_value = random.randint(value_range[0], value_range[1])
    icon = get_icon(entity_id)
    hass.states.set(
        entity_id, new_value, attributes={"unit_of_measurement": "ppm", "icon": icon}
    )


for entity_id in co2_entities:
    update_entity(entity_id, (100, 800))


for entity_id in co_entities:
    update_entity(entity_id, (10, 30))
