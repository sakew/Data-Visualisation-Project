import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['system-design-primer', 'public apis', 'python']

plot_dicts = [
    {'value': 100066, 'label': 'Description of system-design-primer'},
    {'value': 87818, 'label': 'public apis'},
    {'value': 77408, 'label': 'python'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')