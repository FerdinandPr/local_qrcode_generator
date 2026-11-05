#!/usr/bin/env python3
"""Wandelt einen String in einen QR-Code um und schreibt ihn als Bitmap (BMP)."""
import argparse
import os
import sys

import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

EC_LEVELS = {"L": ERROR_CORRECT_L, "M": ERROR_CORRECT_M, "Q": ERROR_CORRECT_Q, "H": ERROR_CORRECT_H}


def main() -> int:
    p = argparse.ArgumentParser(description="String -> QR-Code (BMP)")
    p.add_argument("text", nargs="?", default=os.environ.get("QR_TEXT"),
                   help="Zu kodierender String (alternativ Env QR_TEXT)")
    p.add_argument("--output-dir", default=os.environ.get("QR_OUTPUT_DIR", "/output"))
    p.add_argument("--filename", default=os.environ.get("QR_FILENAME", "qrcode.bmp"))
    p.add_argument("--box-size", type=int, default=int(os.environ.get("QR_BOX_SIZE", "10")),
                   help="Pixel pro QR-Modul")
    p.add_argument("--border", type=int, default=int(os.environ.get("QR_BORDER", "4")),
                   help="Rand in Modulen (Standard laut Spec: 4)")
    p.add_argument("--error-correction", choices=EC_LEVELS, default=os.environ.get("QR_EC", "M"))
    args = p.parse_args()

    if not args.text:
        print("Fehler: Kein String übergeben (Argument oder QR_TEXT).", file=sys.stderr)
        return 2

    if not os.path.isdir(args.output_dir):
        print(f"Fehler: Ausgabeverzeichnis {args.output_dir} existiert nicht (Mount fehlt?).",
              file=sys.stderr)
        return 3

    qr = qrcode.QRCode(
        error_correction=EC_LEVELS[args.error_correction],
        box_size=args.box_size,
        border=args.border,
    )
    qr.add_data(args.text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").get_image().convert("RGB")

    filename = os.path.basename(args.filename)  # kein Path-Traversal
    if not filename.lower().endswith(".bmp"):
        filename += ".bmp"
    target = os.path.join(args.output_dir, filename)
    img.save(target, format="BMP")

    print(f"QR-Code geschrieben: {target} ({img.width}x{img.height} px)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
