#!/usr/bin/env python3

from datetime import datetime, timedelta

today = datetime.now()

print("Seconds since January 1, 1970:", end=' ')

epoch = datetime(1970, 1, 1)
# Calcul correct des secondes totales (pas seulement les microsecondes)
seconds_since_epoch = (today - epoch).total_seconds()
# Format avec virgules et notation scientifique
print(f"{seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation")

print(datetime.strftime(today, "%b %d %Y"))