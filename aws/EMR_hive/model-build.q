-d INPUT=s3://us-west-2.elasticmapreduce/samples/hive-ads/tables
-d "OUTPUT=s3://lloyd-lab1-bucket/hive-ads/output/2015-01-02/17-37-45 (UTC+8)"
-d LIBS=s3://us-west-2.elasticmapreduce/samples/hive-ads/libs

CREATE EXTERNAL TABLE IF NOT EXISTS raw_logs (
 request_begin_time STRING,
 ad_id STRING,
 impression_id STRING, 
 page STRING,
 user_agent STRING,
 user_cookie STRING,
 ip_address STRING,
 clicked BOOLEAN )
PARTITIONED BY (
 day STRING,
 hour STRING )
STORED AS SEQUENCEFILE
LOCATION 's3://us-west-2.elasticmapreduce/samples/hive-ads/tables/joined_impressions/';
--LOCATION '${INPUT}/joined_impressions/';


-- ALTER TABLE raw_logs RECOVER PARTITIONS;
MSCK REPAIR TABLE table_name;


CREATE EXTERNAL TABLE IF NOT EXISTS feature_index (
 feature STRING,
 ad_id STRING,
 clicked_percent DOUBLE )
STORED AS SEQUENCEFILE
LOCATION 's3://lloyd-lab1-bucket/hive-ads/output/2015-01-02/17-37-45(UTC+8)/feature_index/';


INSERT OVERWRITE TABLE feature_index
SELECT
 temp.feature,
 temp.ad_id,
 sum(if(temp.clicked = 'true', 1, 0)) / cast(count(1) as DOUBLE) as clicked_percent
FROM (
 SELECT concat('ua:', trim(lower(ua.feature))) as feature, ua.ad_id, ua.clicked
 FROM (
  MAP raw_logs.user_agent, raw_logs.ad_id, raw_logs.clicked
    USING 's3://us-west-2.elasticmapreduce/samples/hive-ads/libs/split_user_agent.py' as feature, ad_id, clicked
--  USING '${LIBS}/split_user_agent.py' as feature, ad_id, clicked
  FROM raw_logs
 ) ua

 UNION ALL

 SELECT concat('ip:', regexp_extract(ip_address, '^([0-9]{1,3}\.[0-9]{1,3}).*', 1)) as feature, ad_id, cast(clicked as STRING) as clicked
 FROM raw_logs

 UNION ALL

 SELECT concat('page:', lower(page)) as feature, ad_id, cast(clicked as STRING) as clicked
 FROM raw_logs
) temp
GROUP BY temp.feature, temp.ad_id;