def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_apmtools.north_tools import apmtools

    assert (
        apmtools.id_url_safe == 'apmtools' or apmtools.id == 'nomad-north-apmtools'
    ), 'NORTHTool entry point has incorrect id or id_url_safe'
