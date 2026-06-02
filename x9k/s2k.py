from __future__ import annotations
from typing import Any
from x9k.m7q import _Z0
from x9k.p4r import _P0, _z1

_MX = 200
_MN = 1
_K0 = ("g", "rd", "x2", "x4", "sn", "fl")
_L0 = {"g": "General", "rd": "Red Dot", "x2": "2x", "x4": "4x", "sn": "Sniper", "fl": "Free Look"}
_A0 = {"rd": 0.91, "x2": 0.83, "x4": 0.73, "sn": 0.67, "fl": 0.94}

def _c0(_v: float, _lo: int = _MN, _hi: int = _MX) -> int:
    return max(_lo, min(_hi, int(round(_v))))

def _s0(_i: _Z0) -> tuple[float, float]:
    _w, _h = _i._w, _i._y
    if _w <= 0 or _h <= 0:
        return 2400.0, 1.0
    _dg = (_w * _w + _h * _h) ** 0.5
    return _dg, (_i._p or 400) / 400.0

def _g0(_i: _Z0, _p: _P0, _tr: str) -> float:
    _an = {"budget": 98, "mid": 122, "upper_mid": 148, "flagship": 175}
    _b = _an.get(_tr, 122)
    _b += (_p._i - 50) * 0.92
    _hz = {60: 0, 90: 9, 120: 16, 144: 20}.get(_i._z or 60, 0)
    _b += _hz
    _dg, _df = _s0(_i)
    if _dg >= 2600:
        _b -= 10
    elif _dg >= 2350:
        _b -= 5
    elif _dg < 2000:
        _b += 5
    _b -= (_df - 1.0) * 11
    if _i._g > 0:
        if _i._g < 4:
            _b -= 14
        elif _i._g < 6:
            _b -= 7
        elif _i._g >= 12:
            _b += 8
    if _p._h == "t":
        _b -= 9
    if _p._x > 2800:
        _b += 7
    elif 0 < _p._x < 1800:
        _b -= 7
    if _p._l < 8.0 and _p._l > 0:
        _b += 6
    elif _p._l > 12.0:
        _b -= 4
    _b += _p._b * 0.35
    _b += _p._u * 0.12
    return _b

def _h0(_i: _Z0, _p: _P0, _tr: str) -> float:
    _hs = 0.0
    if _p._i >= 55 and _tr in ("upper_mid", "flagship"):
        _hs += 6.0
    if _p._l > 0 and _p._l <= 10.0:
        _hs += 4.0
    if _i._z >= 90:
        _hs += 3.0
    return _hs

def _k1(_i: _Z0, _p: _P0, _tr: str | None = None) -> dict[str, Any]:
    _tu = _tr or _z1(_i, _p)
    _gr = _c0(_g0(_i, _p, _tu) + _h0(_i, _p, _tu))
    _sx: dict[str, int] = {"g": _gr}
    for _k, _r in _A0.items():
        _sx[_k] = _c0(_gr * _r)
    _sx["rd"] = _c0(min(_sx["rd"], _gr - 6))
    _sx["x2"] = _c0(min(_sx["x2"], _sx["rd"] - 9))
    _sx["x4"] = _c0(min(_sx["x4"], _sx["x2"] - 11))
    _sx["sn"] = _c0(min(_sx["sn"], _sx["x4"] - 9))
    _sx["fl"] = _c0(max(_sx["fl"], _gr - 14))
    if _p._i >= 60:
        _sx["rd"] = _c0(min(_sx["rd"] + 2, _gr - 4))
    return {
        "sx": _sx,
        "tr": _tu,
        "pi": _p._i,
        "mx": _MX,
        "hs": _h0(_i, _p, _tu) > 0,
    }

def _k2(_i: _Z0, _r: dict[str, Any], _p: _P0) -> str:
    _sx = _r["sx"]
    _cr = "@ZenDesh | Developer Sandesh & @URxFF team {IG: @6_hf0 & TG/YT: @Unknown_Reason}"
    _ln = [
        "=" * 54,
        "  URxFF EXTREME SENSI ENGINE",
        f"  {_cr}",
        f"  SCALE 1-{_MX}",
        "=" * 54,
        f"DEVICE : {_i._n}",
        f"CHIP   : {_i._h} / {_i._r}",
        f"PANEL  : {_i._w}x{_i._y} @{_i._z}Hz {_i._p}dpi",
        f"RAM    : {_i._g or '?'}GB | BATT {_i._l}% | LOAD {_i._q}",
        f"TOUCH  : {_i._t or '?'}Hz | LAT {_p._l}ms",
        f"POWER  : {_p._i}/100 | GFXIDX {_p._f} | BOOST {_p._b}",
        f"TIER   : {_r['tr']} | HS_MODE {'ON' if _r['hs'] else 'OFF'}",
        "",
        "--- INGAME ---",
    ]
    for _k in _K0:
        _ln.append(f"{_L0[_k]:18}: {_sx[_k]}")
    _ln.extend(["", f"--- {_cr} ---", "=" * 54])
    return "\n".join(_ln)
