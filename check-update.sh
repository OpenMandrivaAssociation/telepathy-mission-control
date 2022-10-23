#!/bin/sh
# 5.99 is actually a dead branch that is much older than 5.16
curl -L https://telepathy.freedesktop.org/releases/telepathy-mission-control/ 2>/dev/null |grep '\.tar\.gz"' |sed -e 's,\.tar\.gz".*,,;s,.*-,,' |grep -v 5.99 |sort -V |tail -n1
