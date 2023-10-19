#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[ ]:


"""
open_ssh_tunnel(): Открывает SSH-туннель к удаленному серверу.
mysql_connect(): Подключается к базе данных MySQL через SSH-туннель.
run_query(sql): Выполняет SQL-запрос к базе данных и возвращает результаты в виде DataFrame pandas.
mysql_disconnect(): Закрывает соединение с базой данных MySQL.
close_ssh_tunnel(): Закрывает SSH-туннель.

"""

import logging
import sshtunnel
import pymysql
import pandas as pd

# Учетные данные для SSH и базы данных
ssh_host = '**********'
ssh_username = '*********'
ssh_password = '*********'
database_username = '******'
database_password = '******'
database_name = '*******'
localhost = '127.0.0.1'

def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    
    :param verbose: Set to True to show logging
    :return: None
    """
    
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    global tunnel
    tunnel = sshtunnel.SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username = ssh_username,
        ssh_password = ssh_password,
        remote_bind_address = ('127.0.0.1', 3306)
    )
    
    tunnel.start()

def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection.
    
    :return: None
    """
    
    global connection
    
    connection = pymysql.connect(
        host='127.0.0.1',
        user=database_username,
        passwd=database_password,
        db=database_name,
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
    
    :return: None
    """
    
    connection.close()

def close_ssh_tunnel():
    """Closes the SSH tunnel connection.
    
    :return: None
    """
    
    tunnel.close()

