FROM confluentinc/cp-kafka-connect:5.5.1

ARG MAVEN_REPOSITORY=https://repo1.maven.org/maven2
ARG MYSQL_DRIVER_VERSION=8.0.21

ADD $MAVEN_REPOSITORY/mysql/mysql-connector-java/$MYSQL_DRIVER_VERSION/mysql-connector-java-$MYSQL_DRIVER_VERSION.jar \
    /usr/share/java/kafka-connect-jdbc/

COPY connect-distributed.properties /opt/connect/config/

ENTRYPOINT [ "connect-distributed", "/opt/connect/config/connect-distributed.properties" ]