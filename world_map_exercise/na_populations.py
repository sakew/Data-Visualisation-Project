from pygal_maps_world.maps import World

world_map = World()
world_map.title = 'Populations of Countries in North America'

world_map.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

world_map.render_to_file('na_populations.svg')