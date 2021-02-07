# modules, which may be used within this role (see Embedding modules and plugins in roles for more information)

#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

    fields = {
        "str1": {"required": True, "type": "str"},
        "str2": {"required": True, "type": "str" },
    }

    module = AnsibleModule(argument_spec=fields)

    str1 = module.params['str1']
    str2 = module.params['str2']

    result = "{} {}".format(str1, str2)

    module.exit_json(changed=False, meta=result)

if __name__ == '__main__':
    main()