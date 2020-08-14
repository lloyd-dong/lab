import org.influxdb.InfluxDB;
import org.influxdb.InfluxDBFactory;
import org.influxdb.dto.Query;
import org.influxdb.dto.Point;
import org.influxdb.dto.BatchPoints;
import java.util.concurrent.TimeUnit;

influxDB = InfluxDBFactory.connect("http://bo-lab:8086","admin","admin")
dbName= "baeldung"

query = new Query("SELECT * from memory", dbName);
result = influxDB.query(query).getResults();
println result
// [Result [series=[Series [name=memory, tags=null, columns=[time, buffer, free, name, used], values=[[2020-03-08T14:51:47.614Z, 1010467.0, 4743656.0, server1, 1015096.0]]]], error=null]]
result[0].getSeries()[0].values[0].size
// =>5
result[0].getSeries()[0].name

return 

influxDB.createDatabase(dbName);
influxDB.setLogLevel(InfluxDB.LogLevel.BASIC);
influxDB.enableBatch(100, 200, TimeUnit.MILLISECONDS);

def str = "class ${influxDB.getClass().name} functions:\r\n";
    influxDB.metaClass.methods.name.unique().each{ 
        str += it+"(); "; 
    }
println "${str}\r\n";


batchPoints = BatchPoints
  .database(dbName)
  .retentionPolicy("defaultPolicy")
  .build();

point1 = Point.measurement("memory")
  .time(System.currentTimeMillis(), TimeUnit.MILLISECONDS)
  .addField("name", "server1")
  .addField("free", 4743656L)
  .addField("used", 1015096L)
  .addField("buffer", 1010467L)
  .build();

point2 = Point.measurement("memory")
  .time(System.currentTimeMillis() - 100, TimeUnit.MILLISECONDS)
  .addField("name", "server1")
  .addField("free", 4743696L)
  .addField("used", 1016096L)
  .addField("buffer", 1008467L)
  .build();
 
batchPoints.point(point1);
batchPoints.point(point2);
//influxDB.write(batchPoints);
influxDB.write(dbName,"autogen",point1)


//influxDB.write(point1);
influxDB.disableBatch();
//influxDB.close();