import os
from gerber import PCB
from gerber.render.theme import Theme
from gerber.render.cairo_backend import GerberCairoContext
from gerber.render import RenderSettings

GERBER_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gerbers'))

# Create a new drawing context
ctx = GerberCairoContext()


COLORS = {

    'red': (1.0, 0.0, 0.0),
    'blue': (0.0, 0.0, 1.0),
    'red soldermask': (0.968, 0.169, 0.165),
}

red = Theme(name='Red',
            topmask=RenderSettings(COLORS['red soldermask'], alpha=0.8, invert=True),
            bottommask=RenderSettings(COLORS['red soldermask'], alpha=0.8, invert=True))

transparent_copper = Theme(name='Transparent',
                           background=RenderSettings((0.9, 0.9, 0.9)),
                           top=RenderSettings(COLORS['red'], alpha=0.5),
                           bottom=RenderSettings(COLORS['blue'], alpha=0.5),
                           drill=RenderSettings((0.3, 0.3, 0.3)))

# Create a new PCB instance
pcb = PCB.from_directory(GERBER_FOLDER)

# Render PCB top view
ctx.render_layers(pcb.top_layers,
                  os.path.join(os.path.dirname(__file__), 'saksham_top.png', ),
                  red, max_width=800, max_height=600)

# Render PCB bottom view
ctx.render_layers(pcb.bottom_layers,
                  os.path.join(os.path.dirname(__file__), 'saksham_bottom.png'),
                  red, max_width=800, max_height=600)

# Render copper layers only
ctx.render_layers(pcb.copper_layers + pcb.drill_layers,
                  os.path.join(os.path.dirname(__file__),
                               'pcb_transparent.png'),
                  transparent_copper, max_width=800, max_height=600)

