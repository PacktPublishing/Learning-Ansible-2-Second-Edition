#!/bin/bash
source $1

SERVICE=$service_name

JAVA_PIDS=$(/usr/java/default/bin/jps | grep ${SERVICE} | awk '{print $1}')

if [ ${JAVA_PIDS} ]; then
    for JAVA_PID in ${JAVA_PIDS}; do
        /usr/bin/kill -9 ${JAVA_PID}
    done
    echo "failed=False msg=\"Killed all the orphaned processes for ${SERVICE}\""
    exit 0
else
    echo "failed=False msg=\"No orphaned processes to kill for ${SERVICE}\""
    exit 0
fi
