import os
import argparse
import toml
import traceback
import logging
import copy

import numpy as np

from opbench.types import TYPES

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description="Batch fit models to operation benchmark data"
)

parser.add_argument("input_file", help="Path to the input TOML file")


def main():
    args = parser.parse_args()

    parsed_input_dict = toml.load(args.input_file)
    config_dict = parsed_input_dict["config"]

    base_dir = os.path.dirname(args.input_file)

    degree_of_confidence = config_dict["degree_of_confidence"]
    row_limit = config_dict["row_limit"]
    plot_output_dir = os.path.join(base_dir, config_dict["plot_output_dir"])
    csv_output_dir = os.path.join(base_dir, config_dict["csv_output_path"])
    log_path = os.path.join(base_dir, config_dict["log_path"])

    if isinstance(config_dict["data_dir"], str):
        data_dir_list = [os.path.join(base_dir, config_dict["data_dir"])]
    elif isinstance(config_dict["data_dir"], list):
        data_dir_list = [os.path.join(base_dir, i) for i in config_dict["data_dir"]]

    operations = []

    for n, op_dict in enumerate(parsed_input_dict["operation"]):
        try:
            op = TYPES[op_dict["type"]]()
            op.set_name(op_dict["name"])

            if "arg_descriptions" in op_dict:
                op.set_model_variable_descriptions(op_dict["arg_descriptions"])

            if "arg_units" in op_dict:
                op.set_model_variable_units(op_dict["arg_units"])

            operations.append(op)
        except Exception as e:
            msg = "Error in operation definition:\n%s\n"%(str(op_dict))
            raise Exception(msg)
            # msg = "Exception: {}\n".format(type(e).__name__)
            # msg = "{}\n".format(e)
            # raise Exception(msg)


    if not os.path.exists(plot_output_dir):
        os.makedirs(plot_output_dir)

    max_param = max([op.get_n_model_param() for op in operations])

    log_file = open(log_path, "w")

    ofile = open(csv_output_dir, "w")
    ofile.write("\"Name\",\"Model\",")
    ofile.write(
        ",".join(
            ["\"Param_%d_label\",\"Param_%d_value\"" % (i + 1, i + 1) for i in range(max_param)]
        )
    )
    ofile.write("\n")

    for op, op_dict in zip(operations, parsed_input_dict["operation"]):

        if "used_arg_indices" in op_dict:
            used_arg_indices = op_dict["used_arg_indices"]
        else:
            used_arg_indices = None

        logging.info("Fitting model for operation: " + op.get_name())

        data_file_name = op.get_name() + ".csv"
        data_file_path_list = [os.path.join(i, data_file_name) for i in data_dir_list]

        for path in copy.deepcopy(data_file_path_list):
            if not os.path.exists(path):

                logging.warning(
                    "Benchmark data file for %s does not exist in directory %s"
                    % (op.get_name(), os.path.dirname(path))
                )
                data_file_path_list.remove(path)

        if len(data_file_path_list) == 0:
            log_file.write("%s\n" % (op.get_name()))
            continue

        # Adjust degree of confidence based on the number of input files
        adjusted_degree_of_confidence = 1 - (1 - degree_of_confidence)/len(data_file_path_list)

        n_param = op.get_n_model_param()
        bounds = [[0 for i in range(n_param)], [np.inf for i in range(n_param)]]

        op_param = op.fit_parameters(
            data_file_path_list,
            adjusted_degree_of_confidence,
            row_limit=row_limit,
            bounds=bounds,
            used_arg_indices=used_arg_indices
        )

        # for data_file_path_list
        for dir_, path in zip(data_dir_list, data_file_path_list):
            plot_path = os.path.join(plot_output_dir, op.get_name() + "__" + dir_ + ".jpg")

            op.plot_model_performance(
                op_param, path, plot_path, row_limit=row_limit, used_arg_indices=used_arg_indices
            )

        ofile.write('"%s","%s",' % (op.get_name(), op.get_model_definition()))
        labels = op.get_model_parameter_labels()
        ofile.write(",".join(['"%s",%.6e' % (i, j) for i, j in zip(labels, op_param)]))

        remaining_cells = max(0, max_param - len(op_param))*2
        for i in range(remaining_cells):
            ofile.write(",")

        ofile.write("\n")
        ofile.flush()

        # input_arr, runtime_arr = parse_benchmark_result(data_file_path, row_limit=row_limit)
        # plt.figure()
        # plt.scatter(input_arr[:,0], runtime_arr, marker='x')
        # plt.grid()
        # # plt.hist(runtime_arr)
        # plt.show()


if __name__ == "__main__":
    main()
