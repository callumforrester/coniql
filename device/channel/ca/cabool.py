from typing import Optional

from cothread import aioca

from device.channel.ca.channel import CaChannel
from device.channel.channeltypes.channel import DEFAULT_TIMEOUT
from device.channel.channeltypes.result import Readback


class CaBool(CaChannel[bool]):
    async def put(self, value: bool) -> Readback[bool]:
        return await super().put(int(value))

    def format_value(self, value):
        return bool(value.real)


async def connect(pv: str, rbv: Optional[str] = None,
              rbv_suffix: Optional[str] = None,
              wait: bool = True, timeout: Optional[float] = None) -> \
        CaBool:
    t_rbv = rbv or f'{pv}{rbv_suffix}' if rbv is not None else None or pv
    t_timeout = timeout or DEFAULT_TIMEOUT

    await aioca.connect([pv, t_rbv])
    channel = CaBool(pv, t_rbv, wait, t_timeout)
    return channel