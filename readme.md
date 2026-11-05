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

## größeren QR-Code erstellen
```bash
podman run --rm --userns=keep-id -e QR_BOX_SIZE=50 -e QR_TEXT="kleiner Test" -e QR_FILENAME=test.bmp -v "$(pwd)/out:/output:Z" qr-generator
```
Über den Parameter Box-Size

### Parameter
- QR_TEXT: String den man im QR-Code verstecken will
- QR_FILENAME: Dateiname, Standard qrcode.bmp
- QR_BOX_SIZE: Pixel pro Modul, Standard 10
- QR_BORDER: Rand in Modulen, Standard 4
- QR_EC: Fehlerkorrektur L, M, Q oder H, Standard M