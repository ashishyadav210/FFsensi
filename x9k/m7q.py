from __future__ import annotations
import os, platform, re, subprocess
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class _Z0:
    _b: str = "unknown"
    _f: str = "unknown"
    _m: str = "unknown"
    _d: str = "unknown"
    _h: str = "unknown"
    _r: str = "unknown"
    _s: str = "unknown"
    _k: str = "unknown"
    _g: float = 0.0
    _z: int = 60
    _w: int = 0
    _y: int = 0
    _p: int = 0
    _t: int = 0
    _l: int = 100
    _q: float = 0.0

    @property
    def _n(self) -> str:
        _u, _v = self._b.strip(), self._m.strip()
        if _u.lower() in ("unknown", "") and _v.lower() != "unknown":
            return _v
        if _v.lower() in ("unknown", ""):
            return _u
        return f"{_u} {_v}".strip()

    @property
    def _x(self) -> str:
        return f"{self._b} {self._m} {self._d} {self._h}".lower()

def _w0(_c: list[str]) -> str:
    try:
        _e = subprocess.run(_c, capture_output=True, text=True, timeout=8, check=False)
        return (_e.stdout or _e.stderr or "").strip()
    except (OSError, subprocess.TimeoutExpired):
        return ""

def _g1(_k: str) -> str:
    _v = _w0(["getprop", _k]) or _w0(["/system/bin/getprop", _k])
    return _v or ""

def _a2(_t: str) -> tuple[int, int]:
    _o = re.search(r"(\d{3,4})x(\d{3,4})", _t)
    return (int(_o.group(1)), int(_o.group(2))) if _o else (0, 0)

def _a3(_t: str) -> int:
    _o = re.search(r"(\d+)\s*dpi", _t, re.I)
    return int(_o.group(1)) if _o else 0

def _a4() -> float:
    try:
        with open("/proc/meminfo", encoding="utf-8") as _f:
            for _ln in _f:
                if _ln.startswith("MemTotal:"):
                    return round(int(_ln.split()[1]) / (1024 * 1024), 1)
    except OSError:
        pass
    return 0.0

def _a5() -> int:
    for _p in ("/sys/class/graphics/fb0/mode", "/sys/class/drm/sde-crtc-0/mode"):
        try:
            with open(_p, encoding="utf-8") as _f:
                _tx = _f.read().lower()
            for _hz in (144, 120, 90, 60):
                if f"{_hz}" in _tx:
                    return _hz
        except OSError:
            continue
    _ds = _w0(["dumpsys", "display"])
    for _hz in (144, 120, 90):
        if re.search(rf"\b{_hz}\s*hz\b", _ds, re.I):
            return _hz
    return 60

def _a6() -> int:
    for _p in ("/sys/class/input/input0/sampling_rate", "/sys/class/input/input1/sampling_rate"):
        try:
            with open(_p, encoding="utf-8") as _f:
                return int(float(_f.read().strip()))
        except (OSError, ValueError):
            continue
    return 0

def _a7() -> int:
    _ds = _w0(["dumpsys", "battery"])
    _m = re.search(r"level:\s*(\d+)", _ds)
    return int(_m.group(1)) if _m else 100

def _a8() -> float:
    try:
        _ld = os.getloadavg()[0]
        return round(_ld, 2)
    except (OSError, AttributeError):
        return 0.0

def _h0(_o: Optional[str] = None) -> _Z0:
    if _o:
        return _Z0(_b="manual", _f="manual", _m=_o, _d=_o.replace(" ", "_").lower())
    if not (os.path.isdir("/system") or _g1("ro.product.model")) and platform.system() == "Windows":
        return _Z0(_b="demo", _f="pc", _m=platform.node() or "pc", _s="0")
    _i = _Z0(
        _b=_g1("ro.product.brand") or _g1("ro.product.vendor.brand"),
        _f=_g1("ro.product.manufacturer"),
        _m=_g1("ro.product.model"),
        _d=_g1("ro.product.device"),
        _h=_g1("ro.hardware"),
        _r=_g1("ro.product.board"),
        _s=_g1("ro.build.version.release"),
        _k=_g1("ro.build.version.sdk"),
        _g=_a4(),
        _z=_a5(),
        _t=_a6(),
        _l=_a7(),
        _q=_a8(),
    )
    _wm = _w0(["wm", "size"]) or _w0(["/system/bin/wm", "size"])
    _i._w, _i._y = _a2(_wm)
    _dn = _w0(["wm", "density"]) or _w0(["/system/bin/wm", "density"])
    _i._p = _a3(_dn)
    return _i

def _j0(_i: _Z0) -> dict:
    return asdict(_i)
