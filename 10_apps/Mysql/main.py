import pymysql.cursors
import pymysql
import sshtunnel
import pandas as pd
import logging
from sshtunnel import SSHTunnelForwarder
import paramiko

k = paramiko.RSAKey.from_private_key_file("/Users/jayelms/.ssh/mw-core-temp-lon-dev")

ssh_host = 'ec2-52-56-48-193.eu-west-2.compute.amazonaws.com'
ssh_username = 'ec2-user'
ssh_password = k,
database_username = 'jay_elms'
database_password = 'ZoveED3uRgPgg3dKdm,eYeUac6MTUEg'


def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.

    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """

    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=('mw-core-live-live-aurora.cluster-c2htiq1tvezk.eu-west-2.rds.amazonaws.com', 3306)
    )

    tunnel.start()


def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection

    :return connection: Global MySQL database connection
    """

    global connection

    connection = pymysql.connect(
        host='127.0.0.1',
        user=database_username,
        passwd=database_password,
        port=tunnel.local_bind_port
    )


def run_query(sql):
    """Runs a given SQL query via the global database connection.
    :param sql: MySQL query
    :return: Pandas dataframe containing results
    """

    return pd.read_sql_query(sql, connection)


def mysql_disconnect():
    """Closes the MySQL database connection.
    """

    connection.close()


def close_ssh_tunnel():
    """Closes the SSH tunnel connection.
    """

    tunnel.close


open_ssh_tunnel()
mysql_connect()
df = run_query("SELECT primary_url FROM web.instance ORDER BY id DESC LIMIT 5")
df.head()
mysql_disconnect()
close_ssh_tunnel()
c = 0
df = pd.DataFrame(list())
for value in df.values:
    c += 1
    print(c, ": ", df.values[0])
