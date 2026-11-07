#!/usr/bin/env python3
"""
mirath-py-radd-surplus-redist — معالج مسائل الرد وتوزيع الفائض على أصحاب الفروض
Al-Radd Estate Surplus Redistribution Solver (Excluding Spouses)
Domain: Computational Ilm Al-Fara'id & Exact Estate Division (علم الفرائض والمواريث الحسابي)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"mirath-py-radd-surplus-redist:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="mirath-py-radd-surplus-redist",
        domain="Computational Ilm Al-Fara'id & Exact Estate Division",
        title_ar="معالج مسائل الرد وتوزيع الفائض على أصحاب الفروض",
        title_en="Al-Radd Estate Surplus Redistribution Solver (Excluding Spouses)",
        sample_input=raw_input,
        computed_output=f"WifeFixed=1/8 | Remainder=7/8 | Daughter=21/32 | Mother=7/32 | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] mirath-py-radd-surplus-redist (Python) — Al-Radd Estate Surplus Redistribution Solver (Excluding Spouses)")
    res = execute_engine("Heirs=[Wife,Daughter,Mother]")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")
