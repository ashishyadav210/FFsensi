from __future__ import annotations
import json, os, time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
from x9k.m7q import _Z0

_R1 = 120_000_000.0
_R2 = 800.0
_R3 = 2_500_000.0

@dataclass
class _P0:
    _c: float = 0.0
    _m: float = 0.0
    _n: int = 1
    _x: float = 0.0
    _g: float = 0.0
    _t: float = 0.0
    _i: float = 0.0
    _e: str = "mid"
    _h: str = "n"
    _u: float = 0.0
    _f: float = 0.0
    _l: float = 0.0
    _b: float = 0.0

    def _d(self) -> dict[str, Any]:
        return asdict(self)

def _b1(_s: float) -> float:
    _st, _dl, _n, _op = time.perf_counter(), time.perf_counter() + _s, 123456789, 0
    while time.perf_counter() < _dl:
        _n = (_n * 1103515245 + 12345) & 0x7FFFFFFF
        _n ^= _n >> 13
        _op += 1
    return _op / max(time.perf_counter() - _st, 0.001)

def _b2(_s: float) -> float:
    _sz = 4 * 1024 * 1024
    try:
        _a, _b = bytearray(_sz), bytearray(_sz)
    except MemoryError:
        return 0.0
    _st, _dl, _tb = time.perf_counter(), time.perf_counter() + _s, 0
    while time.perf_counter() < _dl:
        _b[:] = _a
        _a[0] = (_a[0] + 1) % 256
        _tb += _sz * 2
    return (_tb / (1024 * 1024)) / max(time.perf_counter() - _st, 0.001)

def _b3(_s: float) -> float:
    _st, _dl, _acc = time.perf_counter(), time.perf_counter() + _s, 0.0
    while time.perf_counter() < _dl:
        for _i in range(64):
            _acc += (_i * 1.41421356) ** 0.5
    return _acc / max(time.perf_counter() - _st, 0.001)

def _b4() -> int:
    try:
        return os.cpu_count() or 1
    except OSError:
        return 1

def _b5() -> float:
    _mx = 0.0
    try:
        _bs = "/sys/devices/system/cpu"
        for _nm in os.listdir(_bs):
            if not _nm.startswith("cpu") or _nm == "cpufreq":
                continue
            _pt = f"{_bs}/{_nm}/cpufreq/cpuinfo_max_freq"
            if os.path.isfile(_pt):
                with open(_pt, encoding="utf-8") as _f:
                    _mx = max(_mx, int(_f.read().strip()) / 1000.0)
    except OSError:
        pass
    return _mx

def _b6(_v: float) -> str:
    if _v >= 78:
        return "flagship"
    if _v >= 58:
        return "upper_mid"
    if _v >= 38:
        return "mid"
    return "budget"

def _b7(_h: str, _r: str, _k: str) -> str:
    _pt = Path(__file__).resolve().parent / "d8f.json"
    if not _pt.is_file():
        return "mid"
    with open(_pt, encoding="utf-8") as _f:
        _ch = json.load(_f)
    _hay = f"{_h} {_r} {_k}".lower()
    _ord = ["flagship", "upper_mid", "mid", "budget"]
    _bs = "mid"
    for _cp, _tr in _ch.items():
        if _cp in _hay and _ord.index(_tr) > _ord.index(_bs):
            _bs = _tr
    return _bs

def _b8(_i: _Z0) -> float:
    _s = 50.0
    if _i._t >= 240:
        _s += 18
    elif _i._t >= 120:
        _s += 10
    if _i._z >= 120:
        _s += 8
    if _i._l >= 50:
        _s += 5
    if _i._l < 20:
        _s -= 12
    if _i._q > 4.0:
        _s -= 10
    elif _i._q > 2.5:
        _s -= 5
    return max(0.0, min(100.0, _s))

def _x0(_a: float, _b: float, _g: float, _n: int, _x: float, _gp: float, _gb: float) -> float:
    _cs = min(100.0, (_a / _R1) * 100.0)
    _ms = min(100.0, (_b / _R2) * 100.0)
    _gs = min(100.0, (_g / _R3) * 100.0)
    _cb = min(12.0, max(0, (_n - 4) * 2.5))
    _mb = min(15.0, (_x - 1500) / 50.0) if _x > 0 else 0.0
    return min(100.0, _cs * 0.42 + _ms * 0.22 + _gs * 0.12 + _cb + _mb + _gp * 0.18 + _gb * 0.06)

def _y1(_i: _Z0, _cs: float = 2.0, _ms: float = 1.2, _gs: float = 0.9, _runs: int = 3) -> _P0:
    _n, _x = _b4(), _b5()
    _ca, _ma, _ga = [], [], []
    for _ in range(max(1, _runs)):
        _ca.append(_b1(_cs))
        _ma.append(_b2(_ms))
        _ga.append(_b3(_gs))
    _c = sum(_ca) / len(_ca)
    _m = sum(_ma) / len(_ma)
    _g = sum(_ga) / len(_ga)
    _gp = _b8(_i)
    _gb = 8.0 if _i._l >= 40 and _i._q < 2.0 else 0.0
    _ix = _x0(_c, _m, _g, _n, _x, _gp, _gb)
    _c2 = _b1(0.7)
    _th = "t" if _c2 < _c * 0.72 else "n"
    if _th == "t":
        _ix *= 0.9
    _lat = max(4.0, 1000.0 / _i._t) if _i._t > 0 else 16.0
    return _P0(
        _c=round(_c, 0),
        _m=round(_m, 1),
        _n=_n,
        _x=round(_x, 0),
        _g=round(_g, 0),
        _t=round(_cs * _runs + _ms + _gs + 0.7, 1),
        _i=round(_ix, 1),
        _e=_b6(_ix),
        _h=_th,
        _u=round(_gp, 1),
        _f=round(_g / max(_c, 1) * 1000, 2),
        _l=round(_lat, 2),
        _b=round(_gb, 1),
    )

def _z1(_i: _Z0, _p: _P0) -> str:
    _sc = _b7(_i._h, _i._r, _i._x)
    _ord = ["budget", "mid", "upper_mid", "flagship"]
    return _ord[max(_ord.index(_p._e), _ord.index(_sc))]
