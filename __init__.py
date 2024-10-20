import os
from . import drop_ops
LIBRARY_TYPE = 'TRAFFIC_STREET_LIGHTS'
TRAFFIC_STREET_LIGHTS_PATH = os.path.join(os.path.dirname(__file__),'library',"Traffic and Street Lights")

TRAFFIC_STREET_LIGHTS = {"library_name": "Traffic and Street Lights",
           "library_type": "MODELS",
           "library_path": TRAFFIC_STREET_LIGHTS_PATH,
           "libary_drop_id": "blendv.drop_model"}
            
LIBRARIES = [TRAFFIC_STREET_LIGHTS]

def register():
    drop_ops.register()