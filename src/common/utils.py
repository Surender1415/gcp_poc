"""
Utility Functions module
"""
import argparse
import configparser
import sys

from pyspark.sql import SparkSession
import pyspark.sql.functions as f


def get_or_create_spark_session():
    """
    Initialise spark
    :return: return existing or new Spark Session
    """
    spark = SparkSession \
        .builder \
        .appName('Test') \
        .enableHiveSupport() \
        .getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    return spark


def parse_conf(conf_file):
    """
    Function to read the config file
    :return: conf
    """
    if conf_file is None:
        print('File Error: No File provided')
        sys.exit(-1)

    conf = configparser.ConfigParser()
    conf.optionxform = str
    conf.read(conf_file)

    return conf


def process_cmdline_args():
    """
    Parse command line arguments
    :return: cmd_args
    """
    parser = argparse.ArgumentParser()
    # parser.add_argument("-p", dest="num_partitions")
    parser.add_argument("-config", dest="CONF_FILE")
    cmd_args = parser.parse_args()
    return cmd_args


def flatten_df(nested_df):
    stack = [((), nested_df)]
    columns = []

    while len(stack) > 0:
        parents, df = stack.pop()

        flat_cols = [
            f.col(".".join(parents + (c[0],))).alias("_".join(parents + (c[0],)))
            for c in df.dtypes
            if c[1][:6] != "struct"
        ]

        nested_cols = [
            c[0]
            for c in df.dtypes
            if c[1][:6] == "struct"
        ]

        columns.extend(flat_cols)

        for nested_col in nested_cols:
            projected_df = df.select(nested_col + ".*")
            stack.append((parents + (nested_col,), projected_df))

    return nested_df.select(columns)


def explode_col(col):
    return f.explode(col)
