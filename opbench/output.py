import logging
from sortedcollections import SortedDict
from opbench.helper import round_up


def write_output_csv(operations, path, sort=True):
    if sort:
        operations = sorted(operations, key=lambda x: x.name)

    max_param = max([op.get_n_model_param() for op in operations])

    with open(path, "w") as ofile:
        ofile.write('"Name","Model",')
        ofile.write(
            ",".join(
                [
                    '"Param_%d_label","Param_%d_value"' % (i + 1, i + 1)
                    for i in range(max_param)
                ]
            )
        )
        ofile.write("\n")

        for op in operations:

            if op.latest_param is None:
                logging.info(
                    "Operation %s does not have parameter values, skipping" % op.name
                )
                continue

            ofile.write('"%s","%s",' % (op.get_name(), op.get_model_definition()))
            labels = op.get_model_parameter_labels()
            ofile.write(
                ",".join(
                    ['"%s",%.6e' % (i, j) for i, j in zip(labels, op.latest_param)]
                )
            )

            remaining_cells = max(0, max_param - len(op.latest_param)) * 2
            for i in range(remaining_cells):
                ofile.write(",")

            ofile.write("\n")


def write_fee_schedule(operations, path, sort=True, n_significant_figures=2):
    if sort:
        operations = sorted(operations, key=lambda x: x.name)

    group_dict = SortedDict()
    for op in operations:
        if op.group is not None and op.get_model_input_size() == 0 and op.get_n_model_param() == 1:
            if op.group not in group_dict:
                group_dict[op.group] = []

            group_dict[op.group].append(op)


    with open(path, "w") as ofile:
        ofile.write("# Fee Schedule\n")
        ofile.write("\n")
        ofile.write("| Operation | Gas cost |\n")
        ofile.write("|-----------|----------|\n")

        for op in operations:
            expr = op.get_gas_cost_expr(n_significant_figures=n_significant_figures)

            if expr is None:
                continue

            ofile.write("| `%s` | `%s` |\n" % (op.name, expr))


        if group_dict:
            ofile.write("\n")
            ofile.write("## Grouped Operations\n")
            ofile.write("\n")
            ofile.write("| Group | Maximum Gas cost |\n")
            ofile.write("|-------|------------------|\n")

            for key, ops in group_dict.items():
                # We should only get operations with 0 input variable and 1
                # parameter at this point

                max_cost = max(op.latest_param[0] for op in ops)
                expr = "{:_}".format(round_up(max_cost, n_significant_figures))

                ofile.write("| `%s` | `%s` |\n" % (key, expr))

