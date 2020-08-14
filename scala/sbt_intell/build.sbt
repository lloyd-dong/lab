name := "sbt_intell"

version := "0.1"

scalaVersion := "2.12.4"

val sparkVersion = "2.4.0"
libraryDependencies += "org.apache.spark" %% "spark-core" % sparkVersion
libraryDependencies += "org.apache.spark" %% "spark-sql" % sparkVersion