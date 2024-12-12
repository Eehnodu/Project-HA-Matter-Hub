entity_id = data.get("entity_id")
current_entity = hass.states.get(entity_id)
current_state = current_entity.state
current_source = current_entity.attributes.get("source")
current_unit_of_measurement = current_entity.attributes.get("unit_of_measurement")
current_friendly_name = current_entity.attributes.get("friendly_name")
current_icon = current_entity.attributes.get("icon")

co2value = [31, 40, 10, 99, 10, 999, 50]
choice = int(time.time()) % len(co2value)

hass.states.set(
    entity_id,
    co2value[choice],
    {
        "source": current_source,
        "unit_of_measurement": current_unit_of_measurement,
        "friendly_name": current_friendly_name,
        "icon": current_icon,
    },
    force_update=True,
)
