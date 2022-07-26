"""
Main Module
"""

import src.common.utils as utils

spark = utils.get_or_create_spark_session()

df = spark.read.option("multiline", True) \
    .json("/Users/surendranathreddykudumula/PycharmProjects/gcp_poc/resources/cars_nested.json")

flat = df.select("id", "schema", utils.explode_col("data").alias("data"))

flat_array = flat.select("id", "schema", flat.data.activemode.alias("activemode"),
                         flat.data.status.alias("status"),
                         utils.explode_col(flat.data.cars).alias("c"))
final_df = flat_array.select("id", "schema", "activemode", "status", "c.name", "c.model", "c.value")
final_df.printSchema()
final_df.show(truncate=False)
