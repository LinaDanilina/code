#!/bin/sh
: ${WAL_LEVEL:=minimal}
: ${ARCHIVE_MODE:=off}
: ${ARCHIVE_TIMEOUT:=60}

export WAL_LEVEL
export ARCHIVE_MODE
export ARCHIVE_TIMEOUT

# PGDATA is defined in upstream postgres dockerfile

function update_conf () {
    if [ -f $PGDATA/postgresql.conf ]; then
        sed -i "s/wal_level =.*$/wal_level = $WAL_LEVEL/g" $PGDATA/postgresql.conf
        sed -i "s/archive_mode =.*$/archive_mode = $ARCHIVE_MODE/g" $PGDATA/postgresql.conf
        sed -i "s/archive_timeout =.*$/archive_timeout = $ARCHIVE_TIMEOUT/g" $PGDATA/postgresql.conf
    fi
}