from __future__ import annotations
from pathlib import Path
from x9k.m7q import _Z0

_R = Path(__file__).resolve().parent.parent
_O = _R / "o0x"

def _i0(_b: str) -> list[str]:
    _x = _b.lower()
    _l: list[str] = []
    if any(_t in _x for _t in ("xiaomi", "redmi", "poco")):
        _l.append("settings put system power_mode 1 2>/dev/null || true")
        _l.append("am start -a miui.intent.action.APP_MANAGER_GAME_MAIN 2>/dev/null || true")
    elif "samsung" in _x:
        _l.append("am start -n com.samsung.android.game.gametools/.ui.MainActivity 2>/dev/null || true")
    elif "realme" in _x or "oppo" in _x:
        _l.append("am start -n com.coloros.gamespaceui/.activity.StartActivity 2>/dev/null || true")
    elif "vivo" in _x or "iqoo" in _x:
        _l.append("am start -n com.vivo.gamecube/.ui.GameCubeMainActivity 2>/dev/null || true")
    elif "oneplus" in _x:
        _l.append("am start -n com.oneplus.gamespace/.ui.GameSpaceMainActivity 2>/dev/null || true")
    return _l

def _q0(_i: _Z0) -> Path:
    _O.mkdir(parents=True, exist_ok=True)
    _p = _O / "b0x.sh"
    _bl = "\n".join(_i0(_i._b))
    _tx = f"""#!/system/bin/sh
set -e
settings put global window_animation_scale 0.0 2>/dev/null || true
settings put global transition_animation_scale 0.0 2>/dev/null || true
settings put global animator_duration_scale 0.0 2>/dev/null || true
settings put global force_gpu_rasterization 1 2>/dev/null || true
settings put global hardware_rendering 1 2>/dev/null || true
settings put system peak_refresh_rate {_i._z or 120} 2>/dev/null || true
settings put system min_refresh_rate 60 2>/dev/null || true
cmd deviceidle whitelist +com.dts.freefireth 2>/dev/null || true
cmd deviceidle whitelist +com.dts.freefiremax 2>/dev/null || true
for _pkg in com.dts.freefireth com.dts.freefiremax; do
  cmd game mode set "$_pkg" 2 2>/dev/null || true
  cmd game mode performance "$_pkg" enable 2>/dev/null || true
  cmd netd setprio "$_pkg" 1 2>/dev/null || true
done
{_bl}
echo OK
"""
    _p.write_text(_tx, encoding="utf-8", newline="\n")
    return _p

def _q1(_i: _Z0) -> Path:
    _O.mkdir(parents=True, exist_ok=True)
    _p = _O / "g0x.sh"
    _tx = f"""#!/system/bin/sh
am force-stop com.dts.freefireth 2>/dev/null || true
am force-stop com.dts.freefiremax 2>/dev/null || true
cmd activity kill-all 2>/dev/null || true
sync
echo OK
"""
    _p.write_text(_tx, encoding="utf-8", newline="\n")
    return _p
