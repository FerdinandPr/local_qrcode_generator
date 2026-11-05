# Beschreibung
Es wird ein lokaler Container angestartet, der dann einen QR-Code erzeugt

## Image bauen
```bash
podman build -t qr-generator -f .\Dockerfile
```

## Container anstarten
```bash
podman run --rm --userns=keep-id -e QR_TEXT="Hallo Welt" -e QR_FILENAME=hallo.bmp -v "$(pwd)/out:/output:Z" qr-generator
```

### Parameter
- QR_FILENAME: Dateiname, Standard qrcode.bmp
- QR_BOX_SIZE: Pixel pro Modul, Standard 10
- QR_BORDER: Rand in Modulen, Standard 4
- QR_EC: Fehlerkorrektur L, M, Q oder H, Standard M