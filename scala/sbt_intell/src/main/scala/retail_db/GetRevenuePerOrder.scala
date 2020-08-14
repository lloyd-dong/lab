package retail_db

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.DoubleType
import org.apache.spark.sql.functions._

import sys.process._

object GetRevenuePerOrder {

  def main(args: Array[String]): Unit = {
    val spark: SparkSession = SparkSession.builder.master("local").appName("calculate popularity").getOrCreate
    val sc = spark.sparkContext
    sc.setLogLevel("INFO")

    val path_popularity = "/Users/bodong/Git/portfolio/utils/venue-popularity/venue_porpularity.txt"
    val path_poi_rate = "/Users/bodong/Git/portfolio/utils/venue-popularity/poi_rate.tsv"

    val df_row_popularity = spark.read.format("csv").option("header","true")
        .option("delimiter", "\t").option("inferSchema","true")
        .load(path_popularity)

    val df_poi_rate = spark.read.format("csv").option("header","true")
      .option("delimiter", "\t").option("inferSchema","true")
      .load(path_poi_rate)
      .withColumnRenamed("pass_rate, missing one or both","pass_rate_1")
      .withColumnRenamed("pass_rate, missing both","pass_rate_2")
      .withColumn("pass_rate_2", (substring($"pass_rate_2",0, 5).cast(DoubleType)/100).as("pass_rate"))

    val popularity = df_poi_rate.join(df_row_popularity, $"business_id" === $"muid","inner")

    val output_path = "/Users/bodong/tmp/poi_popularity"
    s"rm -r -f ${"/Users/bodong/tmp/poi_popularity"}".!

    popularity.write.format("csv").option("header","true")
      .option("delimiter", "\t").save(output_path)

    val simple_result = popularity.select($"business_id",$"name", $"city", $"daily_action", $"pass_rate")
      .filter($"pass_rate_2" < 0.60).orderBy($"daily_action")

  }
}
