import json

from pygal_maps_world.maps import World
from pygal.style import RotateStyle, LightColorizedStyle


from world_map_exercise.country_codes import get_country_code

# Load the data into a list.

filename = '../data/population_data.json'

# Build a dictionary of population data.

country_code_populations = {}

with open(filename) as f:
    population_data = json.load(f)

# Print the 2010 population for each country.

for population_dictionary in population_data:
    if population_dictionary['Year'] == '2010':
        country_name = population_dictionary['Country Name']
        population = int(float(population_dictionary['Value']))
        code = get_country_code(country_name)
        if code:
            country_code_populations[code] = population


# Group the countries into 3 populaton levels.

country_code_populations_1, \
country_code_populations_2, \
country_code_populations_3 = {}, {}, {}


for country_code, population in country_code_populations.items():

    if population < 10000000:
        country_code_populations_1[country_code] = population

    elif population < 1000000000:
        country_code_populations_2[country_code] = population

    else:
        country_code_populations_3[country_code] = population

# See how many countries are in each level.

print(
    len(country_code_populations_1),
    len(country_code_populations_2),
    len(country_code_populations_3)
)

world_map_style = RotateStyle('#336699', base_style=LightColorizedStyle)
world_map = World(style=world_map_style)
world_map.title = 'World Population in 2010, by Country'
world_map.add('0-10m', country_code_populations_1)
world_map.add('10m-1bn', country_code_populations_2)
world_map.add('>1bn', country_code_populations_3)


world_map.render_to_file('world_population.svg')


