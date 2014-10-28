#!/usr/bin/env python

import str_case_ops


def preprocess_argv(
        source_file_path, argv, op=str_case_ops.lower_args, *args, **kwargs):

    sfp_index = -1

    # We don't want to touch the source file path and preceeding arguments.
    # Should be a small unsorted list so iterating over it shouldn't be too bad
    for i, arg in enumerate(argv):
        if arg == source_file_path:
            sfp_index = i
            break

    if sfp_index < 0:
        first = []
        rest  = argv
    else:
        first = argv[:sfp_index+1]
        rest  = argv[sfp_index+1:]

    # Operating only on keys on the LHS.
    kwargs['skip_const'] = str_case_ops.EXCLUDE_RIGHT

    return first + op(rest, *args, **kwargs)


def main():
    argv = [__file__, 'inspect_JS']

    upperfied = preprocess_argv(__file__, argv, op=str_case_ops.upper_args)
    assert upperfied == [__file__, 'INSPECT_JS']

    lowerfied = preprocess_argv(__file__, argv, op=str_case_ops.lower_args)
    assert lowerfied == [__file__, 'inspect_js']

    capified = preprocess_argv(__file__, argv, op=str_case_ops.capitalize_args)
    assert capified == [__file__, 'Inspect_js'], capified


if __name__ == '__main__':
    main()
