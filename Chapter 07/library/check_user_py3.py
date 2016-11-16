#!/usr/bin/env python

import pwd
from ansible.module_utils.basic import AnsibleModule

class User:
    def __init__(self, user):
        self.user = user

    # Check if user exists
    def check_if_user_exists(self):
        try:
            user = pwd.getpwnam(self.user)
            success = True
            ret_msg = 'User %s exists' % self.user
        except KeyError:
            success = False
            ret_msg = 'User %s does not exists' % self.user
        return success, ret_msg

def main():
    # Parsing argument file
    module = AnsibleModule(
        argument_spec = dict(
            user = dict(required=True)
        )
    )
    user = module.params.get('user')

    chkusr = User(user)
    success, ret_msg = chkusr.check_if_user_exists()

    # Error handling and JSON return
    if success:
        module.exit_json(msg=ret_msg, uid=uid, gid=gid)
    else:
        module.fail_json(msg=ret_msg)

if __name__ == "__main__":
    main()
