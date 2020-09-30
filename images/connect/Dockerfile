FROM confluentinc/cp-kafka-connect:6.0.0

ARG MAVEN_REPOSITORY=https://repo1.maven.org/maven2
ARG MYSQL_DRIVER_VERSION=8.0.21
ARG PGSQL_DRIVER_VERSION=42.2.16

ADD $MAVEN_REPOSITORY/mysql/mysql-connector-java/$MYSQL_DRIVER_VERSION/mysql-connector-java-$MYSQL_DRIVER_VERSION.jar \
    $MAVEN_REPOSITORY/org/postgresql/postgresql/$PGSQL_DRIVER_VERSION/postgresql-$PGSQL_DRIVER_VERSION.jar \
    /opt/connect/libs/

COPY connect-distributed.properties /opt/connect/config/

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:5.5.1

ENTRYPOINT [ "connect-distributed", "/opt/connect/config/connect-distributed.properties" ]