try:
    import influxdb
except Exception as err:
    print('some Python modules are missing {}'.format_map(err))

