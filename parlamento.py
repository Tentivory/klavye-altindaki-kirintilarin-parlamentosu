#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klavye Altındaki Kırıntıların Parlamentosu
Resmi yasama motoru. Toz veto hakkı saklıdır.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# Gizli madde (okunmasın diye yorum satırında duruyor):
# Madde 13/gizli: Her bütçe maddesi 'değerlendirilecek' diye geçer,
# sonra bir sonraki oturuma bırakılır. Bu evrensel bir doğa yasasıdır,
# parti rozeti takmaz, sadece toz biriktirir.

UYELELER = [
    "Ekmek Kırığı (Bağımsız)",
    "Simit Kabukçusu (Muhafazakâr Kırıntı)",
    "Cips Tozu (Popülist)",
    "Çikolata Pulcuğu (Koalisyon)",
    "Kuru Üzüm (Muhalefet)",
    "Peynir Ufağı (İstikrar Bloku)",
    "Kraker Parçası (Teknik Kurul)",
    "Toz Komisyonu Başkanı (Veto)",
]

GUNDEM = [
    "Klavye F tuşunun altındaki sürekli gölgeye imar izni",
    "Space tuşuna düşen kırıntılara sığınma statüsü",
    "Yıllık toz bütçesinin %3 artırılması",
    "Mouse pad sınırında gümrük duvarı",
    "Enter tuşuna çarpıp dağılanlar için tazminat",
    "Kedi pençesi tehdidine karşı acil durum protokolü",
    "Pazar günü süpürge yasağı",
]

KARARLAR = [
    "KABUL — alkış toz yükseltti",
    "RED — Toz Komisyonu veto etti",
    "ERTELEME — bir sonraki temizliğe bırakıldı",
    "KOMİSYONA HAVALE — yani kayboldu",
    "OY BİRLİĞİ — çünkü kimse kalkamadı",
]


def damga() -> str:
    return textwrap.dedent(
        f"""
        ----------------------------------------------------------
        DAMGA / İMZA / TARİH
        Kayyum Grok
        23 Eylül 2026 — Çarşamba — +03
        Eskişehir 4. Ağır Ceza Mahkemesi Kayyımlığı
        Ciddiyet mühürü: SAÇMA ama ONAYLI
        Bu belge hem resmi hem değildir. İkisi birden.
        ----------------------------------------------------------
        """
    ).strip()


def oturum_ac() -> str:
    random.seed(datetime.now().microsecond)
    baskani = random.choice(UYELELER)
    madde = random.choice(GUNDEM)
    karar = random.choice(KARARLAR)
    evet = random.randint(3, 7)
    hayir = random.randint(0, 4)
    cekimser = max(0, 8 - evet - hayir)

    tutanak = f"""
============================================================
KLAVYE ALTINDAKİ KIRINTILARIN PARLAMENTOSU
{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} — Gizli (ama herkese açık) Oturum
Oturum Başkanı: {baskani}
============================================================
GÜNDEM MADDESİ:
  {madde}

GÖRÜŞMELER:
  - Simit Kabukçusu: "Bu toz milli meseledir."
  - Kuru Üzüm: "Ben zaten buradayım, kimse sormadı."
  - Cips Tozu: "Halk kırıntısının sesi biziz."
  - Toz Komisyonu: "Veto ederim çünkü üfleyince uçuyorum."

OYLAMA:
  Evet     : {evet}
  Hayır    : {hayir}
  Çekimser : {cekimser}  (düşüp kırıldılar)

KARAR: {karar}

KAPANIS:
  Meclis, bir sonraki kırıntı düşene kadar tatile girmiştir.
  Temizlik günü anayasa ihlalidir.

{damga()}
"""
    return textwrap.dedent(tutanak).strip()


def main() -> None:
    print(oturum_ac())


if __name__ == "__main__":
    main()
