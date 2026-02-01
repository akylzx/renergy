from backend.schemas import Requirement
import ee

def init_gee():
    try:
        ee.Initialize(project = "")
    except Exception:
        ee.Authenticate()
        ee.Initialize()

def analyze(req: Requirement):
    roi = ee.Geometry.Rectangle([76.7, 43.0, 77.2, 43.4])  # placeholder

    irradiance = ee.Image("NASA/POWER/SR").rename("irradiance")
    slope = ee.Terrain.slope(ee.Image("USGS/SRTMGL1_003")).rename("slope")

    image = ee.Image.cat([irradiance, slope]).clip(roi)

    samples = image.sample(
        region=roi,
        scale=5000,
        numPixels=200,
        geometries=True
    )

    sites = []
    for f in samples.getInfo()["features"]:
        props = f["properties"]
        score = (
            props.get("irradiance", 0) * req.criteria.get("solar_irradiance", 0)
            - props.get("slope", 0) * req.criteria.get("slope", 0)
        )
        lon, lat = f["geometry"]["coordinates"]
        sites.append({
            "lat": lat,
            "lon": lon,
            "score": round(score, 3),
            "features": props
        })

    return sorted(sites, key=lambda x: x["score"], reverse=True)
