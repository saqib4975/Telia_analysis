from pyspark.shell import spark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


gsm_df = spark.read.csv("/Users/muhammadsaqib/Desktop/Teia_spark/data/gsm/year=2018/month=10/day=24/part-1.csv", header=True,sep=";").withColumn("technology", F.lit("gsm"))

umts_df = spark.read.csv("/Users/muhammadsaqib/Desktop/Teia_spark/data/lte/year=2018/month=10/day=24/part-1.csv", header=True, sep=";").withColumn("technology", F.lit("umts"))

lte_df = spark.read.csv("/Users/muhammadsaqib/Desktop/Teia_spark/data/lte/year=2018/month=10/day=24/part-1.csv", header=True, sep=";").withColumn("technology", F.lit("lte"))


# gsm_df.printSchema()
# umts_df.printSchema()
# lte_df.printSchema()
#
# gsm_df.show()
# umts_df.show()
# lte_df.show()

# Combine all cell data
all_cells_df = gsm_df.unionByName(umts_df).unionByName(lte_df)

# all_cells_df.printSchema()
# all_cells_df.show()

site_df = spark.read.csv("/Users/muhammadsaqib/Desktop/Teia_spark/data/lte/year=2018/month=10/day=24/part-1.csv", header=True,sep=";")
site_df = site_df.withColumnRenamed("frequency_band", "site_frequency_band")
# site_df.printSchema()
# site_df.show()


enriched_df = all_cells_df.join(site_df, "site_id", "left")

# enriched_df.printSchema()
# enriched_df.show()

tech_counts = enriched_df.groupBy("site_id") \
    .pivot("technology", ["gsm", "umts", "lte"]) \
    .agg(F.count("*")) \
    .fillna(0) \
    .withColumnRenamed("gsm", "site_2g_cnt") \
    .withColumnRenamed("umts", "site_3g_cnt") \
    .withColumnRenamed("lte", "site_4g_cnt")

# tech_counts.printSchema()
# tech_counts.show()

freq_bands = enriched_df \
    .select("site_id", "technology", F.col("frequency_band").alias("freq_band")) \
    .withColumn("band_name",
        F.concat(
            F.when(F.col("technology") == "gsm", "G")
             .when(F.col("technology") == "umts", "U")
             .when(F.col("technology") == "lte", "L"),
            F.col("freq_band"),
            F.lit("_by_site"))) \
    .groupBy("site_id") \
    .pivot("band_name") \
    .agg(F.count("*").alias("devices")) \
    .fillna(0)


# freq_bands.printSchema()
# freq_bands.show()

final_df = tech_counts.join(freq_bands, "site_id", "left")

final_df.printSchema()
final_df.show()