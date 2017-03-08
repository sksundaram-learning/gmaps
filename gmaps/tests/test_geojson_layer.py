
import unittest

from .. import geojson_layer, InvalidGeoJson


class GeoJson(unittest.TestCase):

    def test_raise_on_empty_geometry(self):
        geo = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": None,
                    "properties": {"a": 5}
                }
            ]
        }
        with self.assertRaises(InvalidGeoJson):
            geojson_layer(geo)
