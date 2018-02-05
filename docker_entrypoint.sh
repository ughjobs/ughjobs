#!/bin/sh


[[ "z${USER_ID}" == "z" ]] && USER_ID=$(id -u)
[[ "z${GROUP_ID}" == "z" ]] && GROUP_ID=$(id -g)

if [[ ${USER_ID} -eq 0 ]];then
    exec "$@"
else
    RUN_USER=runuser
    RUN_GROUP=$(getent group|awk -F: '$3=='${GROUP_ID}'{print $1}')

    if [ "z${RUN_GROUP}" == "z" ];then
        RUN_GROUP=rungroup
        addgroup -g ${GROUP_ID} ${RUN_GROUP}
    fi

    adduser -s /bin/sh -u ${USER_ID} -G ${RUN_GROUP} -D -S ${RUN_USER}

    # Give user write access to app files
    chown ${RUN_USER}:${RUN_GROUP} -R .

    exec sudo -E -u "${RUN_USER}" "$@"
fi
