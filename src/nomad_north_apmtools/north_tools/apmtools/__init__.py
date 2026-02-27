#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

apmtools = NORTHTool(
    image='ghcr.io/fairmat-nfdi/nomad-north-apmtools:main',
    description="""### **apmtools**:

    [paraprobe-toolbox](https://gitlab.com/paraprobe/paraprobe-toolbox)

    [apav](https://gitlab.com/jesseds/apav)

    [compositionspace](https://github.com/eisenforschung/CompositionSpace)

    [APyT](https://github.com/sebi-85/apyt)""",
    short_description='Jupyterlab with domain-specific open-source software for atom probe research',
    external_mounts=[],
    file_extensions=['nxs, pos, epos, rng, rrng, apt, ato, raw, h5, hdf5, ipynb'],
    icon='https://github.com/FAIRmat-NFDI/nomad-north-apmtools/blob/main/src/nomad_north_apmtools/north_tools/apmtools/jupyter.svg',
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

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad_north_apmtools', north_tool=apmtools
)
