#!/usr/bin/env python

import pwd
from ansible.module_utils.basic import AnsibleModule

def main():
    # Parsing argument file
    module = AnsibleModule(
        argument_spec = dict(
            user = dict(required=True)
        )
    )
    user = module.params.get('user')

    # Check if user exists
    try:
        pwd.getpwnam(user)
        success = True
        ret_msg = 'User %s exists' % user
    except KeyError:
        success = False
        ret_msg = 'User %s does not exists' % user

    # Error handling and JSON return
    if success:
        module.exit_json(msg=ret_msg)
    else:
        module.fail_json(msg=ret_msg)

if __name__ == "__main__":
    main()
