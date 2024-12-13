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

aux_power_entites = [
    "sensor.tia_fake_hub_fake_sunsynk_aux_power",
    "sensor.tia_fake_hub_fake_aux_1",
    "sensor.tia_fake_hub_fake_aux_2",
    "sensor.tia_fake_hub_fake_aux_1_extra",
    "sensor.tia_fake_hub_fake_aux_2_extra",
]

load_power_entities = [
    "sensor.tia_fake_hub_fake_load1_power",
    "sensor.tia_fake_hub_fake_load2_power",
]


def update_power_entity(entity_id, value_range):
    new_value = round(random.uniform(value_range[0], value_range[1]), 2)
    hass.states.set(entity_id, new_value, attributes={"unit_of_measurement": "kW"})
    return new_value


def update_solar_ampere_entity(ampere_entity_id, power_entity_id, voltage=48):
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
    update_solar_ampere_entity(ampere_entity_id, power_entity_id)

for aux_entity_id in aux_power_entites:
    if aux_entity_id == "sensor.fake_sunsynk_aux_power":
        update_power_entity(aux_entity_id, (120, 160))
    else:
        update_power_entity(aux_entity_id, (30, 40))

for load_entity_id in load_power_entities:
    update_power_entity(load_entity_id, (30, 70))
