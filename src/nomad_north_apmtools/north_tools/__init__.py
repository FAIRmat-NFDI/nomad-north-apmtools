from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

apmtools = NORTHTool(
    short_description='Use open source software for analyzing atom probe tomography data in NOMAD.',
    image='ghcr.io/fairmat-nfdi/nomad-north-apmtools:main',
    description="""### **apmtools**:

    [paraprobe-toolbox](https://gitlab.com/paraprobe/paraprobe-toolbox)

    [apav](https://gitlab.com/jesseds/apav)

    [compositionspace](https://github.com/eisenforschung/CompositionSpace)

    [APyT](https://github.com/sebi-85/apyt)""",
    external_mounts=[],
    file_extensions=['nxs, pos, epos, rng, rrng, apt, ato, raw, h5, hdf5, ipynb'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-apmtools/main/src/nomad_north_apmtools/north_tools/apmtools/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='apmtools',
)

#    [APTyzer](https://github.com/areichm/APTyzer)
#    [pyccapt](https://github.com/mehrpad/pyccapt)

north_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad-north-apmtools-apmtools',
    north_tool=apmtools,
)
