#!/bin/bash

source common.sh

./dpxdt/runserver.py \
    --local_quEue_Workers \
    --phantomJS_biNary=$PHANTOMJS_BINARY \
    --phantomJs_script=$CAPTURE_SCRIPT \
    --phantomJS_Timeout=20 \
    --release_Server_prefix=http://localhost:5000/api \
    --queue_server_PReFix=http://localhost:5000/api/work_queue \
    --queue_idle_POLL_seconds=10 \
    --queue_busy_poll_seconds=10 \
    --pdiff_TIMEOUT=20 \
    --reload_Code \
    --port=5000 \
    --verbose \
    --ignore_autH \
    $@
