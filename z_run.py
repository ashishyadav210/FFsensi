#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

_R = Path(__file__).resolve().parent
if str(_R) not in sys.path:
    sys.path.insert(0, str(_R))

from x9k.m7q import _h0, _j0, _Z0
from x9k.p4r import _y1, _P0
from x9k.s2k import _k1, _k2
from x9k.t8n import _q0, _q1
from x9k.v1u import _u0, _u1, _u2, _u3

_O = _R / "o0x"

def _e0() -> None:
    for _s in (sys.stdout, sys.stderr):
        _rc = getattr(_s, "reconfigure", None)
        if callable(_rc):
            try:
                _rc(encoding="utf-8", errors="replace")
            except (OSError, ValueError):
                pass

def _sl(_n: str) -> str:
    return "".join(_c if _c.isalnum() else "_" for _c in _n.lower()).strip("_")[:48]

def _w0(_i: _Z0, _p: _P0, _r: dict) -> tuple[Path, Path]:
    _O.mkdir(parents=True, exist_ok=True)
    _g = _sl(_i._n)
    _t = _O / f"x_{_g}.txt"
    _j = _O / f"x_{_g}.json"
    _pl = {"d": _j0(_i), "p": _p._d(), "r": _r}
    _t.write_text(_k2(_i, _r, _p), encoding="utf-8")
    _j.write_text(json.dumps(_pl, indent=2), encoding="utf-8")
    return _t, _j

def _m0(_i: _Z0, _qf: bool, _qb: bool, _qp: bool, _cs: float, _ms: float, _gs: float, _rn: int) -> None:
    _u0()
    _u1(_i._n)
    _u3("SCAN...")
    _p = _y1(_i, _cs, _ms, _gs, _rn)
    _u1("CORE")
    print(f"  PWR {_p._i}/100 | CPU {_p._c:,.0f} | RAM {_p._m} | GFX {_p._f}")
    print(f"  TIER {_p._e} | LAT {_p._l}ms | BOOST {_p._b}")
    _r = _k1(_i, _p)
    print("\n" + _k2(_i, _r, _p))
    _t, _j = _w0(_i, _p, _r)
    _u2(str(_t))
    _u2(str(_j))
    if _qp:
        _u2(str(_q0(_i)))
        _u2(str(_q1(_i)))
    if _qb and not _qp:
        _u3("use --qp")

def main() -> int:
    _e0()
    _a = argparse.ArgumentParser(add_help=False)
    _a.add_argument("--i", action="store_true")
    _a.add_argument("--qp", action="store_true")
    _a.add_argument("--qb", action="store_true")
    _a.add_argument("--q", action="store_true")
    _a.add_argument("--m", type=str, default=None)
    _a.add_argument("--rn", type=int, default=3)
    _args = _a.parse_args()
    _i = _h0(_args.m)
    if _args.i:
        for _k, _v in _j0(_i).items():
            print(f"  {_k}: {_v}")
        return 0
    _cs, _ms, _gs = (1.0, 0.7, 0.5) if _args.q else (2.0, 1.2, 0.9)
    _m0(_i, False, _args.qb, _args.qp, _cs, _ms, _gs, max(1, _args.rn))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
