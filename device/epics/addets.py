from device.devices.addetector import AdDetector
from device.devices.adpanda import AdPandA
from device.epics.ad import detector_driver, hdf_plugin, camera


async def ad_panda(prefix: str) -> AdPandA:
    driver = await detector_driver(f'{prefix}:DRV')
    hdf = await hdf_plugin(f'{prefix}:HDF')
    return AdPandA(driver=driver, hdf=hdf)


async def ad_detector(prefix: str) -> AdDetector:
    cam = await camera(f'{prefix}:CAM')
    hdf = await hdf_plugin(f'{prefix}:HDF5')
    return AdDetector(camera=cam, hdf=hdf)
